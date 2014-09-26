#!/usr/bin/python

import sys, time, os
import glob
import re

import __main__
__main__.pymol_argv =[ 'pymol','-qc']
from time import sleep
import pymol
pymol.finish_launching()

from pymol import cmd

def convert_that_file_mol(file):
    'Takes a chemical structure file and uses pymol to save it as a mol file'
    try:
        print "Reading %s to convert to mol format \n" %file
        path = os.path.abspath(file)
        name = path.split('/')[-1].split('.')[0]

        cmd.load(file)
        cmd.save("%s.mol" %name,name)
        cmd.do("reinitialize")
    except:
        print "I can't open pymol or convert the file"

def compare_results(good,new):
    import filecmp
    filecmp.cmp(good,new)

def test():
    test_file="/home/mlance/pymol_scripts/tests/1a99_main_chain.pdb.ligand"
    good_file="/home/mlnance/pymol_scripts/tests/output.test"
    try: 
        convert_that_file_mol(test_file)
        compare_results(good_file,"1a99_main_chain.mol")    
    except:
        print "I tried to work correctly, but I don't... DONT USE ME!"

# main
def main():
#    test()
    file=sys.argv[1]
    print "Here is my file name %s \n" %file
    convert_that_file_mol(file)

main()
