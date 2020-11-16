# testingFoam - https://github.com/frostyfeet909/testingFoam
Some programs I'm working on. If you want to run it just navigate to this folder and: 

1. fe41
2. python main.py

Requirments for each are in the respective readme and brief instruction on use.

# Main applications
findGood - Goes through all cases in the data.csv and outputs a text file with cases that performed within a certain tolerance of the referenceCase.

generateData - Generates a number of cases dependant on user input

!plotCases - Plots either the promising cases found by findGood or a custom case user defined, against the referenceCase (Broken)

plotColor - Plots colormaps of the data for each global variable with axis (epsilon,X)

# Additional files
data.csv - Table of data from the last-time step of the simulations, last two columns are epsilon and X respectivly.

dataRanges.csv - Table of data showing previously run 'batches' of tests.

baseCase - An fully setup case that has not yet been run.

referenceCase - An fully setup case that has been run, in this case by interFoam to act as a reference.

# Requirements
1. python 2.7
    1. matplotlib
    2. numpy
    3. seaborn?
    4. scipy
2. foam extend 4.1

# TO DO
1. Fix plotCases (only plotting half the range on the graph???)
2. Create a setup.py and migrate away from main.py for each package

# Structure

folder/

    findGood/
    
      ...
    
    generateData/
    
      ...
    
    plotCases/
    
      ...
    
    plotColor/
  
      ...
      
    resources/
    
      -referenceCase
      
      -baseCase
    
      -data.csv
      
      -dataRanges.csv
      
      ...
      
    output/
    
      ...
  
