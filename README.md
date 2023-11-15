# ptycho_pmace_papers
Repo containing ptychography reconstruction comparisons from publications.

For additional information on PMACE and its latest developments, please click the provided link to the [PMACE repository](https://github.com/cabouman/ptycho_pmace).

## Installation
1. Download the source code:

   Move to a directory of your choice and run the following commands.

   ```console
   git clone https://github.com/cabouman/ptycho_pmace_papers.git
   cd ptycho_pmace_papers
   ```
	
2. Installation:

   It is recommended that you install the package in a virtual environment. Install Anaconda and follow any of the two methods.

* 2.1. Easy installation: If you have Anaconda installed, run the following commands.
           
    ```console
    cd dev_scripts
    yes | source ./clean_install_all.sh
    cd ..
    ```
    
* 2.2. Manual installation: Note the ``pmace`` environment needs to be activated every time you use the package.

	 - 2.2.1 Create a Virtual Environment:

		```console
		conda create --name pmace python=3.8
		conda activate pmace
		```

	 - 2.2.2 Install the dependencies:

		```console
		pip install -r requirements.txt
		```

	 - 2.2.3 Install the package:

		```console
		pip install .
		```
## paper_TCI2023

1. This directory provides scripts for reproducing the results of the following paper:
   
   [[arxiv]](https://arxiv.org/pdf/2303.15679.pdf) [[IEEE Xplore]](https://ieeexplore.ieee.org/iel7/6745852/6960042/10301493.pdf?casa_token=iGFsjXuyzaAAAAAA:mmuzujXHIQmlw9zjytXC9_vzaM0r7liQ8vcWE1w5dqxdxcENi-uoRcX1p8Vy517GKckqt52W)
Zhai, Qiuchen, Gregery T. Buzzard, Kevin Mertes, Brendt Wohlberg, and Charles A. Bouman. "Projected Multi-Agent Consensus Equilibrium (PMACE) With Application to Ptychography." IEEE Transactions on Computational Imaging (2023).

3. Reproducibility of paper figures:
   
   We provide the parameters and data needed to reproduce our paper results for PMACE and competing approaches that are implemented for research use. These may be used as inputs to our scripts for reproducibility. Additionally, the configuration files and results of our demo and tests are available at [output link](https://drive.google.com/drive/folders/1feA5LdkEjVJhqhyFRu7ErgqwKa9Nbkxp?usp=sharing).
 
* To download the required ``ptycho_pmace`` package and check out to the specific branch, run the following command:
  ```console
  cd paper_TCI2023/
  git clone -b v0.0.2 https://github.com/cabouman/ptycho_pmace.git
  git checkout 9a10e15
  ```


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
