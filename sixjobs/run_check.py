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

X = [350]
Y = [350]
for x in X:
    for y in Y:
                myStudy='lhc2018_ats_'+str(x)+'_'+str(y)
                call(sixDeskTool+'set_env.sh -d'+myStudy,shell=True)
                sixdeskdb.SixDeskDB.from_dir('./studies/'+myStudy+'/').check_results(update_work=True)
                call(sixDeskTool+'run_six.sh -i',shell=True)
