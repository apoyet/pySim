from cl2pd import importData
from cl2pd import plotFunctions
from cl2pd import dotdict
from cl2pd import MDanalysis
from cl2pd import variablesDF
from cl2pd import particle
dotdict=dotdict.dotdict
pd=importData.pd     # is the pandas package
np=importData.np     # is the numpy package
cals=importData.cals # pytimber log class
import matplotlib.pyplot as plt
plt.switch_backend('agg')
mySource='/eos/user/a/apoyet/SWAN_projects/2018/simulations-tools/python-toolkit/'

# plot parameters

myTitle = 'ATS FLAT OPTICS - MD#4\nCOLLIMATORS @ 5.5 $\\sigma_{coll}$'

# Studies definition

myStudy='ho_lr_nowire'
myFolder='/eos/user/a/apoyet/SWAN_projects/2018/LHC MD/MD4/flat_footprint/'
myFile=myFolder+'temp_f_'+myStudy+'/dynaptune'

# tfs to pandas dataframe

myDynapDF = importData.tfs2pd([myFile]).iloc[0]['TABLE']

# prepare plot

x = myDynapDF['TUNX'].values
y = myDynapDF['TUNY'].values

#plot

plt.plot(x,y,'o',label=myStudy)
plt.xlim(.30,.32)
plt.ylim(.31,.33)
plt.title(myTitle)
plt.legend(loc='best', frameon=True)
plt.savefig(myStudy+'_footprint.pdf', dpi=300)
