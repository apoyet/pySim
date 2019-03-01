import numpy as np
import pandas as pd
import json
import sys
import os
from subprocess import call
sys.path.append('/afs/cern.ch/user/a/apoyet/public/pySim/python-toolkit/')
import parametricSimulations as pySim

sixDeskTool = '/afs/cern.ch/project/sixtrack/SixDesk_utilities/dev/utilities/bash/'

# Define the scans

X = [350]
Y = [350]


for x in X:
    for y in Y:
		myStudy='lhc2018_ats_'+str(x)+'_'+str(y)
		call(sixDeskTool+'run_six.sh -d'+myStudy+' -a -o 0',shell=True)
