#!/usr/bin/env python


import argparse
import os
import shutil
from Classes_Pymatgen import *

parser = argparse.ArgumentParser()
parser.add_argument('start', help='magmom to check values from',
                    type=int, default=0)
parser.add_argument('end', help='magmom to check values to (inclusive)',
                    type=int, nargs='?')
parser.add_argument('-r', '--radius', help='Number of values to check around (default = 4 (9 jobs)) Only used if two values aren\'t specified',
                    type=int, default=4)
parser.add_argument('-s', '--system', help='Don\'t modify SYSTEM variable in INCAR.  By default NUPDOWN is prepended to this')
parser.add_argument('-w', '--wavecar', help='Copy WAVECAR file',
                    action='store_true')
args = parser.parse_args()

poscar = Poscar.from_file('CONTCAR' if os.path.exists('CONTCAR') and os.path.getsize('CONTCAR') > 0 else 'POSCAR')
potcar = Potcar.from_file('POTCAR')
incar = Incar.from_file('INCAR')
kpoints = Kpoints.from_file('KPOINTS')
system = incar["SYSTEM"]

if not os.path.exists('nupdown'):
    os.makedirs('nupdown')

if args.end:
    start = args.start if args.start < args.end else args.end
    end = args.end + 1 if args.start < args.end else args.start + 1
else:
    start = args.center - args.radius
    end = args.center + args.radius + 1

for i in range(start, end):
    dir = os.path.join('nupdown', str(i).zfill(3))
    print('Setting up run in ./' + dir)
    if not os.path.exists(dir):
        os.makedirs(dir)

    incar['NUPDOWN'] = i
    incar['SYSTEM'] = str(i) + ' ' + system
    incar.write_file(os.path.join(dir, 'INCAR'))
    kpoints.write_file(os.path.join(dir, 'KPOINTS'))
    poscar.write_file(os.path.join(dir, 'POSCAR'))
    potcar.write_file(os.path.join(dir, 'POTCAR'))
    if args.wavecar and os.path.exists('WAVECAR'):
        shutil.copy('WAVECAR', os.path.join(dir,'WAVECAR'))
        if os.path.exists('CHGCAR'):
            shutil.copy('CHGCAR', os.path.join(dir, 'CHGCAR'))