import numpy as np
import pandas as pd
import json
import sys
import os
from subprocess import call
sys.path.append('/afs/cern.ch/user/a/apoyet/public/pySim/python-toolkit/')
import parametricSimulations as pySim
sixDeskTool='/afs/cern.ch/project/sixtrack/SixDesk_utilities/dev/utilities/bash/'
sixdb_path='/afs/cern.ch/project/sixtrack/SixDesk_utilities/dev/utilities/externals/SixDeskDB/'
sys.path.append(sixdb_path)
import sixdeskdb

myOutputForder = 'DA_out'
call('mkdir '+myOutputForder, shell=True)

IW = [0, 105.5] #Values to compensate (4,0)-(6,0) and minimize the others
d = [5.73]

for current in IW:
        for distance in d:
            myStudy='lhc2018_ats_'+str(current)+'_'+str(distance)
            call('rm -rf '+myStudy+'.db dares_'+myStudy, shell=True)
            call(sixdb_path+'sixdb studies/'+myStudy+' load_dir', shell=True)
            da_data = myStudy
            call('rm -rf ./'+myOutputForder+'/'+myStudy+'.txt', shell=True)
            call(sixdb_path+'sixdb '+myStudy+'.db da > ./'+myOutputForder+'/'+myStudy+'.txt', shell=True)
