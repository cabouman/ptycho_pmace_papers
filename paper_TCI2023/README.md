## Paper

This directory provides scripts for reproducing the results of following paper:

[paper link](https://arxiv.org/pdf/2303.15679.pdf)
Zhai, Qiuchen, Gregery T. Buzzard, Kevin Mertes, Brendt Wohlberg, and Charles A. Bouman. "Projected Multi-Agent Consensus Equilibrium (PMACE) for Distributed Reconstruction with Application to Ptychography." arXiv preprint arXiv:2303.15679 (2023).

## Reproducibility of paper figures:
 
We provide the parameters and data needed to reproduce our paper results for PMACE and competing approaches which are implemented for research use. These may be used as inputs to our scripts for reproducibility. Additionally, the configuration files and results of our demo and tests are available at [output link](https://drive.google.com/drive/folders/1feA5LdkEjVJhqhyFRu7ErgqwKa9Nbkxp?usp=sharing).
 
 
* To reproduce the reconstructed transmittance images on synthetic data, please follow these steps:
 
  1. Specify the configuration file located under 'tests/synthetic_data_experiment/config/'
  2. Run the script using the following command:
 
     ```console
     cd tests/synthetic_data_experiment/
     python recon_syn_data.py
     ```
 
* To reproduce the reconstructed transmittance images on pre-processed real data, please follow these steps:
 
  1. Specify the configuration file located under 'tests/real_data_experiment/config/'
  2. Run the script using the following command:
 
     ```console
     cd tests/real_data_experiment/
     python recon_GoldBalls_sample.py
     ```
 
By following these instructions, you can reproduce the results presented in our paper.
