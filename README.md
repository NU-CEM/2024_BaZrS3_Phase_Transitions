### Repository for `Octahedral tilt-driven phase transitions in BaZrS3 chalcogenide perovskite`

This repository contains the data and Python code required to reproduce plots in the paper [Octahedral tilt-driven phase transitions in BaZrS3 chalcogenide perovskite](https://arxiv.org/pdf/2411.14289):

 - `Fig_xxxx.py` or `Fig_xxxx.ipynb`: Code to plot the figures in the main text.
 - `data`: Data for plotting, please see the additional README in the sub-folder.
 - `figs`: Figures which are produced
 - `models`: MLIPs (specifically [NEPs](https://gpumd.org/index.html)) trained using the HSE06 and PBEsol functionals.
 - `structures`: Structures for BaZrS3 in the orthorhombic, tetragonal and cubic phase.
 - Additional Jupyter notebooks to plot figures in the supplementary information are also provided.

Software versions used to run the above scripts/notebooks:
```
calorine  2.3.1
ase       3.22.1
phonopy   2.21.0
spglib    2.2.0
hiphive   1.3.1
GPUMD     3.9.1 
```
