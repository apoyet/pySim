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

IW = [0, 105.5] #Values to compensate (4,0)-(6,0) and minimize the others
d = [5.73]

for current in IW:
	for distance in d:
		myStudy='lhc2018_ats_'+str(current)+'_'+str(distance)
		call(sixDeskTool+'run_six.sh -d'+myStudy+' -a -o 0',shell=True)
