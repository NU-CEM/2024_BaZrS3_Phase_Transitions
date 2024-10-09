import os 
from ase.io import read
import ase

for i in range(1,82):
	imported_crystal = read("MPOSCAR-%03d"%i)
	os.mkdir('calc_%s'%i)
	os.chdir('calc_%s'%i)
	ase.io.write('geometry.in',imported_crystal, scaled=True)
	os.chdir('../')
