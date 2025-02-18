#!/usr/bin/env python
"""
Script to split CHGCAR into its components along the axes
"""
import argparse
from pymatgen.io.vasp.outputs import *

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', type=str, default='CHGCAR')
parser.add_argument('-d', '--derivative', action='store_true')
args = parser.parse_args()

c = Chgcar.from_file(args.file)
basename = args.file.lower() if not args.derivative else args.file.lower() + '.d'

# iterate over each axis
for v in range(3):
    with open(basename + '.' + str(v) + '.txt', 'w') as file_to_write:
        if args.derivative:
            f = c.get_average_along_axis(v)
            h = c.get_axis_grid(v)[1]
            length = len(f)

            # get spherical charge data
            lines = [(-f[(x + 2) % length] + 8 * f[(x + 1) % length] - 8 * f[x - 1] + f[x - 2]) / 12 / h for x in
                     range(length)]

            # write file
            file_to_write.writelines([str(x) + '\n' for x in lines])
        else:
            file_to_write.writelines([str(x) + '\n' for x in c.get_average_along_axis(v)])
