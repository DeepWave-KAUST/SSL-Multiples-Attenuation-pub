<div align="center">

<h1><strong>Self-supervised surface-related multiple suppression with multidimensional convolution</strong></h3>

</div>

## Overview

This repository provides the official implementation of a self-supervised learning framework for surface-related multiple suppression in seismic data.

The proposed method first applies multi-dimensional convolution (MDC) to the observed seismic data to generate artificial surface-related multiples. These MDC-generated multiples are then used to construct self-supervised training pairs without requiring clean multiple-free seismic data.

The network is trained in two stages:

1. **Warm-up stage:** the MDC-generated multiples are added to the observed data to construct more strongly contaminated inputs, while the original observed data are used as pseudo-labels.
2. **Iterative Data Refinement (IDR) stage:** the network predictions are progressively used as improved pseudo-labels, allowing the model to further suppress surface-related multiples while preserving primary reflections.

The repository contains the code and experiment configurations for reproducing the three examples presented in the manuscript:

- layered-model synthetic experiment;
- Otway-model synthetic experiment;
- Mobil AVO Viking Graben Line 12 field-data experiment.

---

## Project structure

This repository is organized as follows:

```text
repository-root/
├── dataset/                         # Directory for the downloaded datasets
├── sslmultiple/
│   ├── configs/
│   │   ├── config_layer.yaml        # Configuration for the layered-model experiment
│   │   ├── config_otway.yaml        # Configuration for the Otway-model experiment
│   │   └── config_field.yaml        # Configuration for the field-data experiment
│   ├── __init__.py
│   ├── dataset.py                   # Dataset loading and preprocessing utilities
│   ├── model.py                     # Neural-network architecture
│   ├── msssimLoss.py                # Multi-scale structural similarity loss
│   ├── predict.py                   # Model inference script
│   ├── train.py                     # Model-training script
│   └── trainer.py                   # Training utilities
├── environment.yml                  # Conda environment configuration
├── install_env.sh                   # Environment installation script
└── README.md
````

Main components:

* :open_file_folder: **`dataset`**: Directory for storing the datasets downloaded from Zenodo.
* :open_file_folder: **`sslmultiple/configs`**: Configuration files for reproducing the three experiments presented in the manuscript.
* :page_facing_up: **`sslmultiple/dataset.py`**: Dataset loading and preprocessing utilities.
* :page_facing_up: **`sslmultiple/model.py`**: Neural-network architecture used for surface-related multiple suppression.
* :page_facing_up: **`sslmultiple/msssimLoss.py`**: Implementation of the multi-scale structural similarity loss.
* :page_facing_up: **`sslmultiple/train.py`**: Training script for the proposed self-supervised framework.
* :page_facing_up: **`sslmultiple/predict.py`**: Inference script for reproducing the multiple-suppression results.
* :page_facing_up: **`sslmultiple/trainer.py`**: Training procedures, including the warm-up and iterative data refinement stages.
* :page_facing_up: **`environment.yml`**: Conda environment specification.
* :page_facing_up: **`install_env.sh`**: Shell script for creating the required Conda environment.

---

## Supplementary files

To support reproducibility, the datasets and trained models used in the manuscript are provided through Zenodo:

> **DOI: [10.5281/zenodo.22036017](https://doi.org/10.5281/zenodo.22036017)**

The Zenodo record contains two compressed files:

```text
dataset.zip
train_model.zip
```

### Datasets

The file `dataset.zip` contains the datasets used in the three experiments presented in the manuscript.

After extracting `dataset.zip`, the directory structure is:

```text
dataset/
├── layer_model/
│   ├── train/
│   └── test/
├── Otway_model/
│   ├── train/
│   └── test/
└── field_data/
```

The three directories correspond to:

* **`layer_model`**: synthetic seismic data generated using the layered velocity model.
* **`Otway_model`**: synthetic seismic data generated using the Otway velocity model.
* **`field_data`**: processed Mobil AVO Viking Graben Line 12 field seismic data used in the field-data experiment.

For the layered and Otway experiments:

* **`test`** contains the original seismic shot gathers used in the experiments.
* **`train`** contains augmented versions of the data used for network training. The augmentation includes left-right and up-down flipping of the complete shot gathers.

All seismic data are stored in MATLAB `.mat` format.

Each `.mat` file contains two variables:

```text
shot
noise
```

where:

* **`shot`** is the observed seismic shot gather containing surface-related multiples.
* **`noise`** contains the artificial surface-related multiples generated from the observed seismic data using multi-dimensional convolution (MDC).

The MDC-generated multiples are used to construct the self-supervised training inputs.

### Trained models

The file `train_model.zip` contains the pretrained PyTorch models corresponding to the three experiments:

```text
trainedmodel_layer.pth
trainedmodel_otway.pth
trainedmodel_field.pth
```

The checkpoints correspond to:

* **`trainedmodel_layer.pth`**: trained model for the layered-model experiment.
* **`trainedmodel_otway.pth`**: trained model for the Otway-model experiment.
* **`trainedmodel_field.pth`**: trained model for the field-data experiment.

These pretrained models can be used with `predict.py` to reproduce the surface-related multiple suppression results presented in the manuscript without retraining the networks.

---

## Getting started :space_invader: :robot:

We recommend creating the Conda environment using the provided `environment.yml` file.

From the repository root directory, run:

```bash
./install_env.sh
```

The installation may take some time. If `Done!` appears in the terminal at the end of the installation, the environment has been successfully created.

Activate the environment using:

```bash
conda activate ssl_demultiple
```

---

## Preparing the supplementary files

Download `dataset.zip` and `train_model.zip` from:

> **DOI: [10.5281/zenodo.22036017](https://doi.org/10.5281/zenodo.22036017)**

Extract `dataset.zip` into the repository root directory so that the resulting structure is:

```text
repository-root/
├── dataset/
│   ├── layer_model/
│   │   ├── train/
│   │   └── test/
│   ├── Otway_model/
│   │   ├── train/
│   │   └── test/
│   └── field_data/
└── sslmultiple/
```

Extract `train_model.zip` into a convenient local directory, for example:

```text
repository-root/
├── trained_model/
│   ├── trainedmodel_layer.pth
│   ├── trainedmodel_otway.pth
│   └── trainedmodel_field.pth
└── sslmultiple/
```

Update the corresponding model path in `predict.py` or in the experiment configuration when necessary.

---

## Experiment configuration files

The `sslmultiple/configs` directory contains the configuration files for reproducing the three experiments:

```text
config_layer.yaml
config_otway.yaml
config_field.yaml
```

They correspond to:

| Configuration file  | Experiment                         |
| ------------------- | ---------------------------------- |
| `config_layer.yaml` | Layered-model synthetic experiment |
| `config_otway.yaml` | Otway-model synthetic experiment   |
| `config_field.yaml` | Field-data experiment              |

The configuration files define the experiment-specific training and data settings.

---

## Running the code :page_facing_up:

After downloading the supplementary files and installing the environment, move into the source-code directory:

```bash
cd sslmultiple
```

### Training

To train a model from scratch, specify the desired experiment configuration at the bottom of `train.py`.

For example, to reproduce the layered-model experiment, set:

```python
if __name__ == '__main__':
    args = load_config('./configs/config_layer.yaml')
```

Then run:

```bash
python train.py
```

For the Otway experiment, change the configuration to:

```python
args = load_config('./configs/config_otway.yaml')
```

and run:

```bash
python train.py
```

For the field-data experiment, use:

```python
args = load_config('./configs/config_field.yaml')
```

and run:

```bash
python train.py
```

The training procedure consists of the warm-up stage followed by the iterative data refinement stage described in the manuscript.

### Inference

To reproduce the results using the provided pretrained models, specify the corresponding configuration file and model checkpoint in `predict.py`.

The three pretrained checkpoints are:

```text
trainedmodel_layer.pth
trainedmodel_otway.pth
trainedmodel_field.pth
```

Use:

```text
trainedmodel_layer.pth
```

with:

```text
config_layer.yaml
```

for the layered-model experiment.

Use:

```text
trainedmodel_otway.pth
```

with:

```text
config_otway.yaml
```

for the Otway-model experiment.

Use:

```text
trainedmodel_field.pth
```

with:

```text
config_field.yaml
```

for the field-data experiment.

After setting the desired configuration and checkpoint path in `predict.py`, run:

```bash
python predict.py
```

---

## Reproducing the layered-model experiment

To reproduce the layered-model experiment from scratch:

1. Download and extract `dataset.zip`.

2. Activate the Conda environment:

```bash
conda activate ssl_demultiple
```

3. Move into the source-code directory:

```bash
cd sslmultiple
```

4. Set the configuration in `train.py` to:

```python
args = load_config('./configs/config_layer.yaml')
```

5. Train the model:

```bash
python train.py
```

Alternatively, use the provided checkpoint:

```text
trainedmodel_layer.pth
```

6. Configure `predict.py` to use `config_layer.yaml` and the layered-model checkpoint.

7. Run inference:

```bash
python predict.py
```

---

## Reproducing the Otway-model experiment

To reproduce the Otway-model experiment, use:

```text
configs/config_otway.yaml
```

for training and:

```text
trainedmodel_otway.pth
```

for inference.

To train from scratch, specify:

```python
args = load_config('./configs/config_otway.yaml')
```

in `train.py`, and run:

```bash
python train.py
```

To reproduce the results using the provided model, configure `predict.py` with the Otway configuration and checkpoint, and run:

```bash
python predict.py
```

---

## Reproducing the field-data experiment

For the field-data experiment, use:

```text
configs/config_field.yaml
```

and the pretrained checkpoint:

```text
trainedmodel_field.pth
```

To retrain the network from scratch, specify:

```python
args = load_config('./configs/config_field.yaml')
```

in `train.py`, and run:

```bash
python train.py
```

For inference, configure `predict.py` with the field-data configuration and pretrained checkpoint, and run:

```bash
python predict.py
```

---

## Reproducibility workflow

A typical workflow for reproducing the numerical experiments is as follows.

1. Clone this repository:

```bash
git clone https://github.com/DeepWave-KAUST/SSL-Multiples-Attenuation-pub.git
cd SSL-Multiples-Attenuation-pub
```

2. Create the Conda environment:

```bash
./install_env.sh
```

3. Activate the environment:

```bash
conda activate ssl_demultiple
```

4. Download the supplementary files from Zenodo:

> **DOI: [10.5281/zenodo.22036017](https://doi.org/10.5281/zenodo.22036017)**

5. Extract `dataset.zip` into the repository root directory.

6. Extract `train_model.zip` into a local model directory.

7. Move into the source-code directory:

```bash
cd sslmultiple
```

8. Select the desired experiment configuration:

```text
config_layer.yaml
config_otway.yaml
config_field.yaml
```

9. To retrain the network, specify the corresponding configuration in `train.py` and run:

```bash
python train.py
```

10. To reproduce the results using a pretrained model, specify the corresponding configuration and model checkpoint in `predict.py`.

11. Run inference:

```bash
python predict.py
```

---

## Hardware and environment

The experiments presented in the manuscript were conducted using a workstation equipped with an Intel(R) Xeon(R) CPU @ 2.10 GHz and a single NVIDIA GeForce RTX 8000 GPU with 48 GB of GPU memory.

Different hardware and software configurations may require minor adjustments.

If the available GPU memory is insufficient for the default training settings, the batch size in the corresponding configuration file can be reduced.

---

## Data availability

The datasets and trained models used to reproduce the experiments in the manuscript are available through the accompanying Zenodo record:

> **DOI: [10.5281/zenodo.22036017](https://doi.org/10.5281/zenodo.22036017)**

The source code is available at:

https://github.com/DeepWave-KAUST/SSL-Multiples-Attenuation-pub

---
