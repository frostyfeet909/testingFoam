Place this folder in your working directory
put the baseCase inside this folder (an unrun case set to interPhaseFieldFoam)
put the referenceCase inside this folder (an completed case using interFoam)
Set the application in generate.run and the baseCase
python plotCases.py

Might need to give executable premission to .run files.
This program needs the most work, it all works its just janky
