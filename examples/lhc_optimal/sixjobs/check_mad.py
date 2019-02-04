import numpy as np
import os
from subprocess import call


# this script aims to check if mad6t jobs ended normally
# to do so, one has to check if the output files exist

IW = [0, 105.5] #Values to compensate (4,0)-(6,0) and minimize the others
d = [5.73]

# folders paths (TO BE CHECKED)
scratchdir = '/afs/cern.ch/work/a/apoyet/first_example/scratch0'
studyName = 'lhc_optimal'

#counting the mmissing studies
count = 0
myMissingMasks = []

for current in IW:
	for distance in d:
		myMask='lhc2018_ats_'+str(current)+'_'+str(distance)
		fort2 = scratchdir+'/sixtrack_input/'+studyName+'/'+myMask+'/fort.2_1.gz'
		fort16 = scratchdir+'/sixtrack_input/'+studyName+'/'+myMask+'/fort.16_1.gz'
		fort8 = scratchdir+'/sixtrack_input/'+studyName+'/'+myMask+'/fort.8_1.gz'
		mother1 = scratchdir+'/sixtrack_input/'+studyName+'/'+myMask+'/fort.3.mother1'
		mother2 = scratchdir+'/sixtrack_input/'+studyName+'/'+myMask+'/fort.3.mother2'

		ok=True

		if(os.path.isfile(fort2)==False):
			ok=False
		if(os.path.isfile(fort16)==False):
			ok=False
		if(os.path.isfile(fort8)==False):
			ok=False
		if(os.path.isfile(mother1)==False):
			ok=False
		if(os.path.isfile(mother2)==False):
			ok=False

		if ok==False:
			count = count+1
			myMissingMasks.append(myMask)


if(count==0):
	print('All good!')
else:
	print('Oups! {} studies did not run correctly...'.format(count))
	print(myMissingMasks)

