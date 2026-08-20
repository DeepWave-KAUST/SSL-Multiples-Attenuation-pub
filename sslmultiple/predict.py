import torch
import os
import numpy as np
import scipy.io as sio
import random
from scipy import signal
from model import UNet
import yaml
from train import load_config

# if you perform testing for layer model
args = load_config('./configs/config_layer.yaml')
# if you perform testing for Otway model
args = load_config('./configs/config_otway.yaml')
# if you perform testing for Field data
args = load_config('./configs/config_field.yaml')

# Select the trained model
dir_cp = f'./train_model/model.pth'

test_ids = [os.path.splitext(file)[0] for file in os.listdir(args.dir_test) 
            if not file.startswith('.')]

device = torch.device('cuda')
net = UNet(in_channels=args.in_channels, out_channels=args.out_channels).to(device)
net.eval()

print('------ Test starting -------')
for ip, cp in enumerate(args.cp_list):

    # Load corresponding model architecture and weights
    net.load_state_dict(torch.load(f'{dir_cp}{cp}.pth', map_location=device))

    dir_output = f'./test/output/epoch{cp}/'
    os.makedirs(dir_output, exist_ok=True)

    for i, fn in enumerate(test_ids):
        tar_file = os.path.join(args.dir_test, fn)
        print("\nPredicting seismic data {} ...".format(fn))
        dict = sio.loadmat(tar_file)
        inp_img = dict['shot']
        inp_img = torch.from_numpy(inp_img.copy()).unsqueeze(0).unsqueeze(1).type(torch.FloatTensor).cuda()

        with torch.no_grad():
            pred = net(inp_img)

        pred = pred.cpu().squeeze().numpy()

        sio.savemat(f'{dir_output}{fn}_out.mat', {'pred': pred})

        print("\nPredicting seismic data {} have done...".format(fn))

print('------ Test completed successfully -------')
    
