import numpy as np
import pandas as pd
import json
import sys
import os
from subprocess import call
sys.path.append('/afs/cern.ch/user/a/apoyet/public/pySim/python-toolkit/')
import parametricSimulations as pySim

print('######################################################')
print('#           Preparation of the sequence              #')
print('######################################################')


# folder of study

myStudyFolder = '/afs/cern.ch/user/a/apoyet/public/pySim/sixjobs/'

# folder containing masked file

mySequenceFolder = myStudyFolder+'sequences/'
myFile = mySequenceFolder+'sequence_maker_masked.mask'

# get the list of masked parameters

myMaskedParam = pySim.getMaskedParameterList(myFile, tag='%MASKED_')

# print the list of masked parameters

print('========= List of parameters =========')
print(myMaskedParam)

# Define the parameters

myParams = {}
myParams.update({
    # BEAM AND MACHINE PARAMETERS
    '%MASKED_I_MO' : 0,              #[A] MO Octupole
    '%MASKED_NPART' : 1.15e11,       #[p] per bunch
    '%MASKED_NRJ' : 6500,            #[GeV]
    '%MASKED_ON_BB_SWITCH' : 1,      # Switch to install BB
    '%MASKED_ON_COLLISION' : 1,      # Switch to enable crossing scheme
    '%MASKED_emittance_norm' : 2.2,  #[1e-6] nomalised emittance
    '%MASKED_mylhcbeam' : 1,         #beam to be tracked (B1!)
    '%MASKED_on_ov5' : 0,            # CMS bump (if on, -1.8 [mm])

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

    # paths
    '%MASKED_sixjobsPath' : '/afs/cern.ch/user/a/apoyet/public/pySim'
})


#====================================================================================#
#                                 IMPORTANT CHECK                                    #
#====================================================================================#
# We want to be sure every paramter is defined

if len(myMaskedParam)==len(myParams):
    print('#====================================================================================#')
    print('Congrats, you can proceed!!')
    print('#====================================================================================#')
    pySim.unmaskSequenceMaker(myFile, myMaskedParam, myParams, mySequenceFolder)
    myInput = mySequenceFolder+'sequence_maker.madx'
    call('madx<sequence_maker.madx',shell=True)
else:
    print('#====================================================================================#')
    print('WARNING!!!! {} parameter(s) is/are not defined!! Please define everything!'.format(len(myMaskedParam)-len(myParams)))
    print('#====================================================================================#')
