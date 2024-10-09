import numpy as np
from matplotlib import pyplot as plt
from pandas import DataFrame
from phonopy.units import THzToCm
from seekpath import get_explicit_k_path
import phonopy
import ase, ase.io
import os 


structure = ase.io.read('geometry.in', format='aims')
phonon = phonopy.load(supercell_filename="SPOSCAR")

structure_tuple = (structure.cell, structure.get_scaled_positions(), structure.numbers)
path = get_explicit_k_path(structure_tuple)

phonon.write_modulations()
