import json
import numpy as np 
import pandas as pd 

def createStudiesList(template, X, Y):
    # Build the list of studies

    myStudies = []
    for x in X:
        for y in Y:
            myStudies.append(template+str(x)+'_'+str(y))
            
    # dump list in json file
    with open('myStudies.json', 'w') as outfile:
        json.dump(myStudies, outfile)


# Template name

myTemplate = 'lhc2018_ats_'

# Define the X,Y scan

X = [0, 50, 100, 150, 200, 250, 300, 350]
Y = [6, 7, 8, 9, 10]


createStudiesList(myTemplate, X, Y)