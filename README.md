# arc-proliferation
A repository which uses OpenMC, DAGMC, and Paramak to study proliferation risks of compact FLiBe-blanketed DT tokamaks like ARC.

Fusion reactor models are generated using the parametric reactor code paramak, which meshes and exports these models into the .h5m file format which can be read by OpenMC using DAGMC. OpenMC (with the DAGMC module enabled) is then used to propagate neutrons through these models and study their fissile breeding potentials. 

## Organization

The project is organized around each reator model, so each subdirectory corresponds to a particular reactor model, with further subdirectories containing code for a specific calculation. Inside each directory is a python file which uses paramak to generate the CAD model and mesh it for use in OpenMC called `create_geometry.py`. Various Jupyter Notebooks in the directory can then be used to run OpenMC simulations and analyse the results. Most of these simulations are run in depletion mode - meaning that many OpenMC simulations are run in order to calculate how the inventory of isotopes in the model changes with time. This allows for effects like fission of bred fissile isotopes to be included. You can learn more about depletion calculations on the OpenMC website: [https://docs.openmc.org/en/stable/methods/depletion.html](https://docs.openmc.org/en/stable/methods/depletion.html)

## Installation and Setup

In order to run both the paramak code for generating the models and the OpenMC simulations in the Jupyter Notebooks, it is recommended to create two separate conda environments. One is exclusively for generating the paramak models, and basically only needs to have paramak installed. To setup this environment, simply follow the conda installation instructions on the paramak website: [https://paramak.readthedocs.io/en/main/](https://paramak.readthedocs.io/en/main/)

For OpenMC, create a separate conda environment and install the latest version which should include DAGMC capability by default. Instructions on how to do this are available on the quick install guide on the OpenMC website: [https://docs.openmc.org/en/stable/quickinstall.html](https://docs.openmc.org/en/stable/quickinstall.html)

 You'll also need to install the ipykernal and jupyter packages, which you can do with the following command:

  `conda install jupyter`

  The [neutronics_material_maker](https://github.com/fusion-energy/neutronics_material_maker) package is also required in the OpenMC conda environment, and can also be installed using conda or mamba:

  `conda install neutronics_material_maker -c conda-forge`
  or
  `mamba install neutronics_material_maker -c conda-forge`

  Other dependencies include `numpy`, `scipy`, and `matplotlib`

  ## Current Structure

  ## Arc 2018
  This model is based on the 2015 paper by Sorbom et al. and the 2018 paper by Kuang et al. It matches the specified radial build of this design very closely except for one notable exception - the thickness of the beryllium neutron multiplication layer, which is 2 cm instead of 1. This is due to a bug in paramak at the moment which means it doesn't correctly mesh layers 1 cm thick.


