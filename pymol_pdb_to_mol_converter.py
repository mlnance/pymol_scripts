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
    print "Reading %s to convert to mol format \n" %file
    path = os.path.abspath(file)
    name = path.split('/')[-1].split('.')[0]

    cmd.load(file)
    cmd.save("%s.mol" %name,name)
    cmd.do("reinitialize")

# main
def main():
    file=sys.argv[1]
    print "Here is my file name %s \n" %file
    convert_that_file_mol(file)

main()
