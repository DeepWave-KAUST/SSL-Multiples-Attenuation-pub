import  torch, os
import torch.nn.functional as F
import  numpy as np
import torch.nn as nn
from  model import UNet
import random
from msssimLoss import MSSSIM

dir_checkpoints = './checkpoints/'
os.makedirs(dir_checkpoints, exist_ok=True)

class Base_trainer():
    def __init__(self, args, train=True):
        self.args = args
        self.epoch = 0
        self.cur_iter = -1
        self.device = torch.device('cuda')
        self.net = torch.nn.SyncBatchNorm.convert_sync_batchnorm(UNet(in_channels=self.args.in_channels, 
                            out_channels=self.args.out_channels)).to(self.device)
        self.define_loss()
        self.set_optimizer()
        self.set_scheduler()
        if train:
            self.net.train()

    def preprocess(self, data):
        raw = data['raw']
        multiple = data['multiple']
        self.labels = raw
        self.inputs = raw + multiple

    def define_loss(self):
        if self.args.loss_type == 'l1':
            self.criterion = nn.L1Loss()
        if self.args.loss_type == 'l2':
            self.criterion = nn.MSELoss()
        self.msssim = MSSSIM()
        return

    def set_optimizer(self):
        if self.args.optimizer == 'Adam':
            self.optimizer = torch.optim.Adam(self.net.parameters(), lr=self.args.lr, weight_decay=self.args.wd)
        if self.args.optimizer == 'AdamW':
            self.optimizer = torch.optim.AdamW(self.net.parameters(), lr=self.args.lr, weight_decay=self.args.wd)
        return

    def set_scheduler(self):
        if self.args.schedule == 'cosine':
            self.scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(self.optimizer, T_max=self.args.total_epoch)
        if self.args.schedule == 'multistep':
            self.scheduler = torch.optim.lr_scheduler.MultiStepLR(self.optimizer, milestones=self.args.milestones, gamma=self.args.gamma)
        return

    def update_lr_scheme(self):
        self.scheduler.step()

    def optimize_parameters(self):
        self.optimizer.zero_grad()
        self.output = self.net(self.inputs)
        loss1 = self.criterion(self.output, self.labels)
        loss2 = self.msssim(self.output, self.labels)
        loss = loss1 + self.args.epsilon*loss2
        loss.backward()
        self.optimizer.step()
        self.print_iter_info(loss)
        return loss

    def print_iter_info(self, loss):
        self.cur_iter += 1
        if self.cur_iter % self.args.print_freq == 0 or self.epoch == self.args.total_epoch:
            print('Iteration ', self.cur_iter, '----> loss =', loss.item(), 'Lr = ', self.optimizer.param_groups[0]['lr'])

    def save_model(self):
        if (self.epoch + 1) % self.args.save_state_freq == 0 or self.epoch == self.args.total_epoch:
            torch.save(self.net.state_dict(), dir_checkpoints+f'CP_epoch{self.epoch + 1}.pth')
            print(f'Epoch {self.epoch + 1} model save')

class Base_fastIDR(Base_trainer):
    def __init__(self, args, train=True):
        super(Base_fastIDR, self).__init__(args, train)

        self.net_copy = UNet(in_channels=1, out_channels=1).to(self.device).eval()
        self.net_copy_epoch = self.epoch

    def preprocess(self, data):
        raw = data['raw']
        multiple = data['multiple']

        self.labels = raw

        if self.epoch >= self.args.warmup_epoch:
            if self.net_copy_epoch < self.epoch:
                self.net_copy_epoch = self.epoch
                self.net_copy.load_state_dict(self.net.state_dict())

            with torch.no_grad():
                self.labels = self.net_copy(self.labels)

        if self.epoch < self.args.warmup_epoch:
            scale_level = random.uniform(self.args.level_warmup[0], self.args.level_warmup[1])
        if self.epoch >= self.args.warmup_epoch:
            scale_level = random.uniform(self.args.level_idr[0], self.args.level_idr[1])

        self.inputs = self.labels + scale_level * multiple
