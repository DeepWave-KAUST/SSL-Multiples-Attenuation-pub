**<div align="center">

<h1><strong>Self-supervised surface-related multiple suppression with multidimensional convolution</strong></h1>

<h4>Shijun Cheng, Ning Wang, and Tariq Alkhalifah</h3>

<h4><em>DeepWave Consortium, King Abdullah University of Science and Technology (KAUST)</em></h4>

<p><em>Corresponding author: Shijun Cheng (<a href="mailto:sjcheng.academic@gmail.com">sjcheng.academic@gmail.com</a>)</em></p>

</div>**

# Project structure
This repository is organized as follows:

* :open_file_folder: **sslmultiple**: python library containing routines for Self-supervised free-surface multiple attenuation;
* :open_file_folder: **data**: folder to store dataset

## Supplementary files
To ensure reproducibility, we provide the the data set for our tests and our trainined model.

* **Data set:**
Download our data set [here](https://kaust.sharepoint.com/:u:/r/sites/M365_Deepwave_Documents/Shared%20Documents/Restricted%20Area/REPORTS/DW0085/dataset.zip?csf=1&web=1&e=QS5ZVw). Then, use `unzip` to extract the contents.

**Note:** The link contains all the data sets, including layered model, Otway model, and field data. After you download the zip file `dataset.zip`, you can use `unzip` to extract all the data sets, which are located in folders `layer_model`, `Otway_model`, and `field_data`. 

* **Trained model:**
Download our trained model [here](https://kaust.sharepoint.com/:u:/r/sites/M365_Deepwave_Documents/Shared%20Documents/Restricted%20Area/REPORTS/DW0085/train_model.zip?csf=1&web=1&e=jNwULQ). Then, extract the contents.

**Note:** The link contains all the tests, including layered model, Otway model, and field data. After you download the zip file `train_model.zip`, you can use `unzip` to extract all the model file, namely `trainedmodel_layer.pth`, `trainedmodel_otway.pth`, and `trainedmodel_field.pth`. 

## Getting started :space_invader: :robot:
To ensure reproducibility of the results, we suggest using the `environment.yml` file when creating an environment.

Simply run:
```
./install_env.sh
```
It will take some time, if at the end you see the word `Done!` on your terminal you are ready to go. 

Remember to always activate the environment by typing:
```
conda activate ssl_demultiple
```

## Running code :page_facing_up:
When you have downloaded the supplementary files and have installed the environment, you can run the training and inference code. 

For traning, you need to specify which config file you want to load at the bottom of the `train.py` file, and then run:
```
python train.py
```

For inference, you also need to specify which config file you want to load at the top of the `predict.py` file, and then run:
```
python predict.py
```

**Disclaimer:** All experiments have been carried on a Intel(R) Xeon(R) CPU @ 2.10GHz equipped with a single NVIDIA GEForce RTX 8000 GPU. Different environment configurations may be required for different combinations of workstation and GPU.

## Cite us 
DW0085 - Cheng et al. (2025) Self-supervised free-surface multiple suppression.

