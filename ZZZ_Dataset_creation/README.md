# Prerequisite (installs)
- pflotran (#TODO ANLEITUNG)
- python 3.8.10 or newer (tested with this version)
- python packages: numpy, ...
- bash 5.0.17 or newer (tested with this version)

# Phd_simulation_groundtruth
builds datasets with definable number of data points; based on one pflotran.in file, varying pressure gradients in external .txt file (and varying permeability fields based on perlin_noise in external .h5 files)

## if you use this script on a new computer
- remember to copy all (!) required files (see dummy_dataset + .sh bash-script + /scripts)
- if you run the script for a varying permeability field, check that you have all required files additionally to pflotran.in in dummy_dataset: mesh.uge, north.ex, south.ex, east.ex, west.ex, heatpump_inject1.vs
    else: if one if the files is missing: run the script create_grid_unstructured.py in the folder /scripts/scripts_grid
- set the $PFLOTRAN_DIR (in ~/.zshrc or bashrc or similar)

## how to run the script
- decide on whether you want to vary the pressure and permeability field or only the pressure field
    - if you want to vary both, you need to rename the file pflotran_vary_perm.in to pflotran.in and run the bash script make_dataset_vary_perm.sh
    - if you want to vary only the pressure field, you need to rename the file pflotran_iso_perm.in to pflotran.in and run the bash script make_dataset_2.sh
- always start from the dataset-directory where your pflotran.in file is located, otherwise it does not find the respective bash files
- run script via "bash ../<name_of_script> (here <name_of_script> is make_dataset_2.sh or make_dataset_vary_perm.sh; this file should be in a parent directory of the datasets you want to simulate - or otherwise give the full path to the script) <CLA_NUMBER_DATAPOINTS> <CLA_NAME> <CLA_CASE> <CLA_VISUALISATION>" with the respective commandline arguments
    - CLA_NUMBER_DATAPOINTS is the number of data points that should be generated in this dataset OR if ..._vary_perm: CLA_NUMBER_VARIATIONS_PRESSURE and CLA_NUMBER_VARIATIONS_PERMEABILITY
    - CLA_NAME is the name of the dataset to create
    - CLA_CASE currently has two options: "1D" creates a dataset with a constant pressure field that only varies in the y-component; "2D" creates a dataset with a constant pressure field that varies in the x- and y-component
    - CLA_VISULISATION is an optional commandline argument defining whether to produce some automated pictures (selfmade in python) : if you want it, write "vis" as CLA_VISUALISATION, else leave it empty