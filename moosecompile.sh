#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 10:24:30 2018

@author: andylau

To compile moose and its submodules directly
"""

import os
import subprocess

home_dir = os.getcwd()
moose_base = os.path.join(home_dir,'moose')
moose_mol_dir = os.path.join(moose_base,'modules')


test_moose=os.path.exists(moose_base)
# add exception for if moose is clone already
if test_moose is None:
    print("MOOSE doesn't exist")
    subprocess.call("git clone git@github.com:idaholab/moose.git", shell=True)
os.chdir(moose_base)
rebuild_libmesh=subprocess.call("./scripts/update_and_rebuild_libmesh.sh", shell=True)

os.chdir(os.path.join(moose_base,'test'))
subprocess.call("make -j 4", shell=True)
subprocess.call("./run_tests -j 4", shell=True)

moduleslist=['phase_field','tensor_mechanics','xfem','heat_conduction']

for i in range(len(moduleslist)):
    os.chdir(os.path.join(moose_mol_dir,moduleslist[i]))
    subprocess.call("make -j 4", shell=True)
    subprocess.call("./run_tests -j 4", shell=True)
