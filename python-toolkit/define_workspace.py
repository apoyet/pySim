import os
from subprocess import call

mySixjobsFolder = '/afs/cern.ch/user/a/apoyet/public/pySim/sixjobs/'

# BE CAREFUL: be in your afs/work folder
folder = os.getcwd()
if folder[:18] != '/afs/cern.ch/work/':
    print('###### WARNING ######')
    print('You should run that in your work afs directory')

# workspace name

myWorkspace = 'aTestWorkSpace'

# studies (don't worry, you can add others afterwards)

myStudies = ['currentScan', 'distanceScan', 'tuneScan']

for study in myStudies:
    studyFolder = myWorkspace+'/scratch0/'+study
    myLink = myWorkspace+'/'+study
    call(['mkdir','-p',studyFolder])
    call(['ln','-s','scratch0/'+study,study],cwd=myWorkspace)
    call(['cp','-r',mySixjobsFolder,'.'],cwd=myLink)
