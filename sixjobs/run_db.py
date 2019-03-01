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

X = [350]
Y = [350]

for x in X:
    for y in Y:
        myStudy='lhc2018_ats_'+str(x)+'_'+str(y)
        call('rm -rf '+myStudy+'.db dares_'+myStudy, shell=True)
        call(sixdb_path+'sixdb studies/'+myStudy+' load_dir', shell=True)
        da_data = myStudy
        call('rm -rf ./'+myOutputForder+'/'+myStudy+'.txt', shell=True)
        call(sixdb_path+'sixdb '+myStudy+'.db da > ./'+myOutputForder+'/'+myStudy+'.txt', shell=True)
