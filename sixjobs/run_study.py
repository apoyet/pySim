import numpy as np
import pandas as pd
import json
import sys
import os
from subprocess import call
sys.path.append('/afs/cern.ch/user/a/apoyet/public/pySim/python-toolkit/')
import parametricSimulations as pySim

def unmask(myFile, myMaskedParam, myParams, myOutMask_path):
    searchFile = open(myFile, 'r')
    myUnmaskedFile = ''
    for line in searchFile:
        for param in myMaskedParam:
            line = line.replace(param, str(myParams[param]))
        myUnmaskedFile = myUnmaskedFile+line
    text_file = open(myOutMask_path,"w")
    text_file.write(myUnmaskedFile)
    text_file.close()



# sixdesk scripts
sixDeskTool = '/afs/cern.ch/project/sixtrack/SixDesk_utilities/dev/utilities/bash/'

print('######################################################')
print('#               Environment preparation              #')
print('######################################################')


# folder of study

myStudyFolder = '/afs/cern.ch/work/a/apoyet/testStudy/test/'

# folder containing env file
envFile = 'sixjobs/sixdeskenv_masked'
myFile = myStudyFolder+envFile
myOut = myStudyFolder+'sixjobs/sixdeskenv'

# get the list of masked parameters

myMaskedParam = pySim.getMaskedParameterList(myFile, tag='%MASKED_')

myEnvParam = {}
myEnvParam.update({
    '%MASKED_workspace' : 'test',
    '%MASKED_basedir' : '/afs/cern.ch/work/a/apoyet/testStudy',
    '%MASKED_studyName' : '%MASKED_studyName'
})

unmask(myFile, myMaskedParam, myEnvParam, myOut)



print('######################################################')
print('#      Creation of the .mask files and run mad6t     #')
print('######################################################')


# Define the scans

X = [350]
Y = [350]

for x in X:
    for y in Y:
        # folder containing masked file
        maskName = 'lhc2018_ats_masked.mask'

        myMaskFolder = myStudyFolder+'/sixjobs/mask/'
        myFile = myMaskFolder+maskName

        # get the list of masked parameters

        myMaskedParam = pySim.getMaskedParameterList(myFile, tag='%MASKED_')

        # Output folder

        myOutputFolder = myStudyFolder+'sixjobs/lhc2018_ats_'+str(x)+'_'+str(y)+'_outputs/'
        os.mkdir(myOutputFolder)


        # Define the parameters (mask)

        myParams = {}
        myParams.update({
            # BEAM AND MACHINE PARAMETERS
            '%MASKED_I_MO' : 0,              #[A] MO Octupole
            '%MASKED_NPART' : 1.15e11,       #[p] per bunch
            '%MASKED_NRJ' : 6500,            #[GeV]
            '%MASKED_ON_BB_SWITCH' : 1,      # Switch to install BB
            '%MASKED_ON_WIRE' : 1,           # Switch to install wires
            '%MASKED_ON_COLLISION' : 1,      # Switch to enable crossing scheme
            '%MASKED_emittance_norm' : 2.2,  #[1e-6] nomalised emittance
            '%MASKED_mylhcbeam' : 1,         #beam to be tracked (B1!)
            '%MASKED_on_ov5' : -1.8,            # CMS bump (if on, -1.8 [mm])

            # OPTICS
            '%MASKED_opticsfile' : "db5/PROTON/opticsfile.22_ctpps2",
            '%MASKED_on_x1' : 150,
            '%MASKED_on_x5' : 150,
            '%MASKED_qprime' : 15,
            '%MASKED_qprimx0' : 15,
            '%MASKED_qprimy0' : 15,
            '%MASKED_qx0' : 62.31,
            '%MASKED_qy0' : 60.32,

            # BB ENCOUNTERS
            '%MASKED_n_insideD1' : 5,        # nb of encounters in D1, nominal 5
            '%MASKED_on_ho1' : 1,
            '%MASKED_on_ho2' : 0,
            '%MASKED_on_ho5' : 1,
            '%MASKED_on_ho8' : 0,
            '%MASKED_on_lr1l' : 1,
            '%MASKED_on_lr1r' : 1,
            '%MASKED_on_lr2l' : 0,
            '%MASKED_on_lr2r' : 0,
            '%MASKED_on_lr5l' : 1,
            '%MASKED_on_lr5r' : 1,
            '%MASKED_on_lr8l' : 0,
            '%MASKED_on_lr8r' : 0,
            # WIRE R5
            '%MASKED_x_wire_r5' : -0.00715,
            '%MASKED_y_wire_r5' : 0,
            '%MASKED_s_wire_r5' : 158.3,
            '%MASKED_I_wire_r5' : x,

            # WIRE L5
            '%MASKED_x_wire_l5' : 0.00824,
            '%MASKED_y_wire_l5' : 0,
            '%MASKED_s_wire_l5' : 158.3,
            '%MASKED_I_wire_l5' : x,

            # WIRE R1
            '%MASKED_x_wire_r1' : 0,
            '%MASKED_y_wire_r1' : -0.00739,
            '%MASKED_s_wire_r1' : 158.3,
            '%MASKED_I_wire_r1' : y,

            # WIRE L1
            '%MASKED_x_wire_l1' : 0,
            '%MASKED_y_wire_l1' : 0.00742,
            '%MASKED_s_wire_l1' : 158.3,
            '%MASKED_I_wire_l1' : y,

            # OUTPUTS
            '%MASKED_Output_Ktable_path' : myOutputFolder+'k_table.tfs',
            '%MASKED_Output_Twiss_Path' : myOutputFolder+'final_twiss.twiss',
            '%MASKED_footkey' : 0,
            '%MASKED_footprint_mydynap' : myOutputFolder+'dynap',
            '%MASKED_footprint_mydynaptune' : myOutputFolder+'dynaptune'

        })

        mySource =  myMaskFolder+maskName
        myOutMask = 'lhc2018_ats_'+str(x)+'_'+str(y)+'.mask'
        myOutMask_path = myMaskFolder+myOutMask
        unmask(mySource, myMaskedParam, myParams, myOutMask_path)

	#sixdeskenv
        envFile = 'sixjobs/sixdeskenv_masked'
        myFile = myStudyFolder+envFile
        myOut = myStudyFolder+'sixjobs/sixdeskenv'
        myMaskedParam = pySim.getMaskedParameterList(myFile, tag='%MASKED_')
        myEnvParam = {}
        myEnvParam.update({
            '%MASKED_workspace' : 'test',
            '%MASKED_basedir' : '/afs/cern.ch/work/a/apoyet/testStudy',
            '%MASKED_studyName' : myOutMask[:-5]
        })
        unmask(myFile, myMaskedParam, myEnvParam, myOut)
        call(sixDeskTool+'set_env.sh -s',shell=True)
        call(sixDeskTool+'mad6t.sh -s',shell=True)
