#!/usr/bin/env python
# Starts two relaxations from opposite ends of the saddle point.  Uses the Fire Method, which should relax into
# local minima so subsequent runs should be done with the VTST code.  Files can be found in mins/min{1,2}

# usage:  Dim_Check.py
import os
import cfg
import shutil
import sys
from Classes_Pymatgen import *

def check_dimer(directory, runP=True):
    os.chdir(directory)
    os.system(os.path.join(cfg.VTST_DIR, 'dimmins.pl'))
    for m in ['min1', 'min2']:
        dir = os.path.join(directory, 'mins', m)
        shutil.copy(os.path.join(directory, 'WAVECAR'), dir)
        incar = Incar.from_file(os.path.join(dir,'INCAR'))
        incar['EDIFF'] = 1e-5
        incar['EDIFFG'] = -5e-2
        incar.pop('ICHAIN')
        incar['IOPT'] = 7
        incar.write_file(os.path.join(dir,'INCAR'))
        if runP:
            os.chdir(dir)
            os.system('VTST_Custodian.py ' + reduce(lambda x,y: str(x)+' '+str(y), sys.argv[1:], ''))
            os.chdir(directory)

if os.path.basename(sys.argv[0]) == 'Dim_Check.py':
    check_dimer(os.path.abspath(os.curdir))