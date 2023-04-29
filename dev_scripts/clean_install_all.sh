#!/bin/bash

# Clean out old installation
cd ..
/bin/rm -r build
/bin/rm -r ptycho_pmace.egg-info
/bin/rm -r ptycho_pmace_papers.egg-info
cd dev_scripts

# Create conda environment and install package
source install_conda_env.sh