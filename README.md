# testingFoam - https://github.com/frostyfeet909/testingFoam
Some programs I'm working on. If you want to run it just navigate to this folder and: 

1. fe41
2. python main.py

Requirements for each are in the respective readme and brief instruction on use (they're very out of date). Any folders/files listed in the structure needed for execution either come packaged with it or will be generated on first run.

# Main applications
findGood - Goes through all cases in the data.csv and outputs a text file with cases that performed within a certain tolerance of the referenceCase.

generateData - Generates a number of cases dependant on user input

plotCases - Plots either the promising cases found by findGood or a custom case user defined, against the referenceCase

plotColor - Plots colormaps of the data for each global variable with axis (epsilon,X)

# Additional files
data.csv - Table of data from the last-time step of the simulations, last two columns are epsilon and X respectively.

dataRanges.csv - Table of data showing previously run 'batches' of tests.

baseCase - An fully setup case that has not yet been run. Setup by Federico Municchi with C++ function to save the data at each time-step to a csv DataSummary.csv

referenceCase - An fully setup case that has been run, in this case by interFoam to act as a reference. Setup by Federico Municchi with C++ function to save the data at each time-step to a csv DataSummary.csv

other - Folder of other useful scripts.

# Requirements
1. python 2.7
    1. matplotlib
    2. numpy
    3. seaborn?
    4. scipy
2. foam extend 4.1

# TO DO
1. Create a setup.py and migrate away from main.py for each package
2. Update readme+main.py in each sub-directory
4. Fix axis on colormaps

# Structure

    testingFoam/
        findGood/
            -dataInterface.py
            -findGood.py
            -main.py
    
        generateData/
            -dataInterface.py
            -generate.run
            -main.py
    
        plotCases/
            -cleanup.run
            -dataInterface.py
            -generate.run
            -main.py
            -plotDifference.py
    
        plotColor/
            -cleanup.run
            -dataInterface.py
            -generate.run
            -main.py
            -plotColor.py
      
        resources/
            referenceCase/
              -1/
              -DataSummary.csv
              ...
            baseCase/
              -constant/
                -transportProperties
                ...
              -plots/
                -plotData.py
              ...
              
            -data.csv
            -dataRanges.csv
            ...
      
        output/
            ...
  
        other/
            -makeGif.run
            
        -main.py
