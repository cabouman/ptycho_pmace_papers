For additional information on PMACE and its latest developments, please click the provided link to the [PMACE repository](https://github.com/cabouman/ptycho_pmace).

## paper_TCI2023

This directory provides scripts for reproducing the results of the following paper:

[[arxiv]](https://arxiv.org/pdf/2303.15679.pdf) [[IEEE Xplore]](https://ieeexplore.ieee.org/iel7/6745852/6960042/10301493.pdf?casa_token=iGFsjXuyzaAAAAAA:mmuzujXHIQmlw9zjytXC9_vzaM0r7liQ8vcWE1w5dqxdxcENi-uoRcX1p8Vy517GKckqt52W)
Zhai, Qiuchen, Gregery T. Buzzard, Kevin Mertes, Brendt Wohlberg, and Charles A. Bouman. "Projected Multi-Agent Consensus Equilibrium (PMACE) With Application to Ptychography." IEEE Transactions on Computational Imaging (2023).

## Reproducibility of paper figures:
   
   We provide the parameters and data needed to reproduce our paper results for PMACE and competing approaches that are implemented for research use. These may be used as inputs to our scripts for reproducibility. Additionally, the configuration files and results of our demo and tests are available at [output link](https://drive.google.com/drive/folders/1feA5LdkEjVJhqhyFRu7ErgqwKa9Nbkxp?usp=sharing).

   To reproduce the result, please follow the instructions provided in ptycho_pmace_papers/README.md to install the required packages first. Then run the following commands:
 
1. Download the required ``ptycho_pmace`` package by running the following command:
  ```console
  cd paper_TCI2023/
  git clone -b v0.0.2 https://github.com/cabouman/ptycho_pmace.git
  ```
      
And switch to the branch
  ```console
  cd ptycho_pmace/
  git checkout 9a10e15
  cd ..
  ```

2. To reproduce the reconstructed transmittance images on synthetic data as shown in Figure 4 and 5 in paper, please follow these steps:
 
- Specify the configuration file located under 'tests/synthetic_data_experiment/config/'
- Run the script using the following command:
 
     ```console
     cd tests/synthetic_data_experiment/
     python recon_syn_data.py
     ```
 
3. To reproduce the reconstructed transmittance images on pre-processed real data as shown in Figure 11 and 12 in paper, please follow these steps:
 
- Specify the configuration file located under 'tests/real_data_experiment/config/'
- Run the script using the following command:
 
     ```console
     cd tests/real_data_experiment/
     python recon_GoldBalls_sample.py
     ```
