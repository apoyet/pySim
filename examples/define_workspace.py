from subprocess import call

# BE CAREFUL: be in your afs/work folder
folder = !pwd
if folder[0][:18] != '/afs/cern.ch/work/':
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
