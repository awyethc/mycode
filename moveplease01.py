#!/usr/bin/env python3

#import the code needed to make this file mover/renamer work
import shutil
import os

# force the program to 'start'in the home user directory
os.chdir("/home/student/mycode")

# move the raynor.obj with shutil.move to ceph_storage folder
shutil.move('raynor.obj', 'ceph_storage/') # THIS WILL DELETE ANY FILE NAMED 'raynor.obj' IN THE DESTINATION FOLDER.

# prompt user for a new name for the kerrigan.obj file
xname = input("What is the new name for kerrigan.obj? ")

# rename the current kerrigan.obj file
shutil.move("ceph_storage/kerrigan.obj", "ceph_storage/" + xname)


