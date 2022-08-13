# arc-proliferation
A repository which uses OpenMC, DAGMC, and Paramak to study proliferation risks of compact FLiBe-blanketed DT tokamaks like ARC.

Fusion reactor models are generated using the parametric reactor code paramak, which meshes and exports these models into the .h5m file format which can be read by OpenMC using DAGMC. OpenMC (with the DAGMC module enabled) is then used to propagate neutrons through these models and study their fissile breeding potentials. 

## Organization

The project is organized around each reator model, so each subdirectory corresponds to a particular reactor model. Inside each directory is a python file which uses paramak to generate the CAD model and mesh it for use in OpenMC called `create_geometry.py`. Various Jupyter Notebooks in the directory can then be used to run OpenMC simulations and analyse the results. Most of these simulations are run in depletion mode - meaning that many OpenMC simulations are run in order to calculate how the inventory of isotopes in the model changes with time. This allows for effects like fission of bred fissile isotopes to be included. You can learn more about depletion calculations on the OpenMC website: 

## Installation and Setup

In order to run both the paramak code for generating the models and the OpenMC simulations in the Jupyter Notebooks, it is recommended to create two separate conda environments. One is exclusively for generating the paramak models, and basically only needs to have paramak installed. To setup this environment, simply follow the conda installation instructions on the paramak website:

For OpenMC, create a separate conda environment and install the latest version which should include DAGMC capability by default. You'll also need to install the ipykernal and jupyter packages, which you can do with the following command:
