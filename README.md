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

   It is recommended that you install the package to a virtual environment. Install Anaconda and follow any of the two methods.

* 2.1. Easy installation: If you have Anaconda installed, run the following commands.
           
    ```console
    cd dev_scripts
    source ./clean_install_all.sh
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
