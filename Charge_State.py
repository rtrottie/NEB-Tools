#!/usr/bin/env python
'''
Automatically create VASP run directories to change the charge state of the given input
'''

import argparse
import copy
import os
import shutil
from Classes_Pymatgen import *
from Helpers import get_nelect

parser = argparse.ArgumentParser()
parser.add_argument('start', help='lowest charge value',
                    type=int)
parser.add_argument('end', help='highest charge value',
                    type=int)
parser.add_argument('-f', '--folder', help='Folder to get charge from (default : ".")',
                    type=str, default='0')
parser.add_argument('-c', '--charge', help='Charge of initial state (default : 0)',
                    type=int, default=0)
parser.add_argument('-s', '--system', help='Don\'t modify SYSTEM variable in INCAR.  By default charge state is appended to this')
args = parser.parse_args()

# Load Input files
poscar = Poscar.from_file(os.path.join(args.folder, 'CONTCAR') if os.path.exists(os.path.join(args.folder, 'CONTCAR')) and os.path.getsize(os.path.join(args.folder, 'CONTCAR')) > 0 else os.path.join(args.folder, 'POSCAR'))
potcar = Potcar.from_file(os.path.join(args.folder, 'POTCAR'))
incar = Incar.from_file(os.path.join(args.folder, 'INCAR'))
kpoints = Kpoints.from_file(os.path.join(args.folder, 'KPOINTS'))
system = incar["SYSTEM"]
base_nelect = get_nelect(os.path.join(args.folder, 'OUTCAR'))
base_sys = incar['SYSTEM'].split()

for i in range(args.start, args.end+1):
    rundir = os.path.join(str(i))
    rundir = rundir.replace('-', 'n')
    if not os.path.exists(rundir):  # check if directory has been created
        print('Setting up run in ./' + rundir)
        os.makedirs(rundir)

        # Modify the number of electrons to match the desired charge state
        incar['NELECT'] = base_nelect - i + args.charge
        if base_sys[-1] == '0':
            sys = copy.copy(base_sys)
            sys[-1] = rundir
        else:
            sys = base_sys + [rundir]

        # Write input files to run directory based on results of already converged calculation
        incar['SYSTEM'] = ' '.join(sys)
        incar.write_file(os.path.join(rundir, 'INCAR'))
        kpoints.write_file(os.path.join(rundir, 'KPOINTS'))
        poscar.write_file(os.path.join(rundir, 'POSCAR'))
        potcar.write_file(os.path.join(rundir, 'POTCAR'))
    else:  # If folder exists do not overwrite, but display an message
        print('Folder exists:  ' + rundir)