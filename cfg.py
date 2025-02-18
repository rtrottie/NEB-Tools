# a general cfg file if you use scripts which change atoms, make sure these values fit your own i.e. have a
# cfg.py file before this one on your python path.  If an atom you want to use is missing just let me know
# and I can add it.  Variables at the end of this file should be declared in your .bashrc (or .my.bashrc on janus)

INCAR = {
    'LDAUL': {'default': -1,
              'Fe': 2,
              'Co': 2,
              'Ni': 2,
              'Cu': 2,
              'Mn': 2,
              'Ti': 2,
              'Cr': 2,
              'V': 2,
              'Sc': 2,
              'Zn': 2,
              'Ru': 2
              },
    'LDAUU': {'default': 0,
              'Fe': 4.09,
              'Co': 4.26,
              'Ni': 2.277,
              'Cu': 5,
              'Mn': 1.844,
              'Ti': 3.5,
              'Cr': 3.24,
              'V': 2.5,
              'Sc': 3,
              'Zn': 0,
              'Ru': 3
              },

    'MAGMOM': {'default': 0,
               'Sc': 1,
               'Ti': 2,
               'V': 3,
               'Cr': 4,
               'Mn': 5,
               'Fe': 4,
               'Co': 3,
               'Ni': 2,
               'Cu': 1,
               'Zn': 0,
               'Ru': 0
               }
}

INCAR_format = [
    ('SYSTEM', ['SYSTEM']),
    ('ALGORITHM - GENERAL', ['NPAR', 'NSIM', 'NCORE', 'KPAR', 'LREAL', 'IDIPOL', 'LDIPOL', 'LPLANE']),
    ('ALGORITHM - ELECTRONIC',
     ['GGA', 'METAGGA', 'ALGO', 'IALGO', 'PREC', 'ENCUT', 'NELMIN', 'NELM', 'NELMDL', 'EDIFF', 'NELECT', 'WEIMIN',
      'ADDGRID']),
    ('ELECTRONIC STRUCTURE', ['ISPIN', 'MAGMOM', 'NUPDOWN', 'NBANDS', 'ISMEAR', 'SIGMA']),
    ('DFT+U', ['LDAU', 'LDAUTYPE', 'LDAUL', 'LDAUU', 'LMAXMIX', 'LDAUPRINT']),
    ('HSE', ['LHFCALC', 'HFSCREEN', 'PRECFOCK', 'AEXX', 'NKRED']),
    ('ALGORITHM - IONIC', ['IBRION', 'NSW', 'POTIM', 'EDIFFG', 'ISIF', 'ISYM']),
    ('INPUT', ['ISTART', 'ICHARG', 'KSPACING']),
    ('OUTPUT', ['NWRITE', 'LORBIT', 'LAECHG', 'LWAVE', 'LCHARG', 'LVTOT', 'LOPTICS', 'LVHAR', 'LPEAD']),
    ('NEB', ['IMAGES', 'SPRING']),
    ('VTST', ['ICHAIN', 'IOPT', 'LCLIMB', 'LNEBCELL']),
    ('SETUP',
     ['REQUIRE', 'AUTO_TIME', 'AUTO_NODES', 'AUTO_MEM', 'AUTO_GAMMA', 'AUTO_CORES', 'AUTO_QUEUE', 'STAGE_NUMBER',
      'STAGE_NAME', 'STAGE_FILE'])  # must be last

]
