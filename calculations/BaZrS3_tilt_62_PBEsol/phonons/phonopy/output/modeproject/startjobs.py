import os 
from ase.io import read
import ase

for i in range(1,82):
	os.chdir('calc_%s'%i)
	if not os.path.exists('aims.out'):
		os.system('pwd') 
		os.system('cp ../run.slm .')
		os.system('cp ../control.in .')
		os.system('sbatch run.slm')
	os.chdir('../')
