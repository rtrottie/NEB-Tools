#!/bin/bash
#SBATCH -J {{ J }}
#SBATCH --time={{ hours }}:00:00
#SBATCH -N {{ nodes }}
#SBATCH --ntasks-per-node {{ nntasks_per_node }}
#SBATCH -o {{ logname }}-%j.out
#SBATCH -e {{ logname }}-%j.err
#SBATCH --qos=normal

module load python/anaconda-2.0.1
module load fftw/fftw-3.3.3_openmpi-1.4.5_intel-12.1.0_double_ib
module load intel/intel-12.1.6;
module load openmpi/openmpi-1.4.5_intel-12.1.6_ib;
PYTHONPATH=$PYTHONPATH:/home/rytr1806/NEB-Tools

python -c "

import sys
import os
import shutil
from custodian.vasp.jobs import *
from custodian.vasp.handlers import *
from custodian.custodian import *
import pymatgen
from pymatgen.io.vaspio.vasp_input import *
from pymatgen.io.vaspio_set import *
from Classes import *


vaspjob = [NEBJob(['mpirun', '-np', '{{ tasks }}', '/projects/musgravc/apps/red_hat6/vasp5.3.3/tst/gamma/vasp.5.3/vasp'], '{{ logname }}', gamma_vasp_cmd='/projects/musgravc/apps/red_hat6/vasp5.3.3/tst/gamma/vasp.5.3/vasp',auto_npar=False)]
handlers = [WalltimeHandler({{ hours }}*60*60)]
c = Custodian(handlers, vaspjob, max_errors=10)
c.run()"