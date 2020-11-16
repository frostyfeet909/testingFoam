# testingFoam - https://github.com/frostyfeet909/testingFoam
Some programs I'm working on. If you want to run it just navigate to this folder and: 

1. fe41
2. python main.py

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

# TO DO

1. Fix plotColor.py properly
2. Make a common folder for things they need like baseCase, referenceCase, dataInterface.py
3. Change dataInterface.py to default path to the current WD
4. Fix relative imports
5. Create a setup.py and migrate away from main.py for each package
6. Update plotColor to use the difference instead of absolute value

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
  
