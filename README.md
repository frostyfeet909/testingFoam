# testingFoam
Some programs I'm working on.

Requirments for each are in the respective readme and brief instruction on use.

# Main applications
findGood - Goes through all cases in the data.csv and outputs a text file with cases that performed within a certain tolerance of the referenceCase.

generateData - Generates a number of cases dependant on user input

plotCases - Plots either the promising cases found by findGood or a custom case user defined, against the referenceCase

plotColor - Plots colormaps of the data for each global variable with axis (epsilon,X)

# Additional files
data.csv - Table of data from the last-time step of the simulations, last two columns are epsilon and X respectivly.

baseCase - An fully setup case that has not yet been run.

referenceCase - An fully setup case that has been run, in this case by interFoam to act as a reference.

# Structure

folder/

    findGood/
  
      -referenceCase
    
      ...
    
    generateData/
  
      -baseCase
    
      ...
    
    plotCases/
  
      -baseCase
    
      -referenceCase
    
      ...
    
    plotColor/
  
      ...
    
    -data.csv
  
