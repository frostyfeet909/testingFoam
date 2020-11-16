# Plot the content of a csv file
import scipy
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 22})
from matplotlib import rcParams
from matplotlib.ticker import MaxNLocator
import csv
import seaborn as sns

rcParams.update({'figure.autolayout': True})
rcParams['font.family'] = 'serif'
rcParams['font.serif'] = ['Computer Modern Roman']
rcParams['text.usetex'] = True

def plotVelocity():
    # Initialize empty arrays
    t = []
    Umean = []
    Umax = []

    # Open file and read row by row
    with open('../DataSummary.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            t.append(float(row[0]))
            Umean.append(float(row[1]))
            Umax.append(float(row[2]))


    # Plot
    plt.figure(figsize=(250 /25.4, 200 / 25.4))
    plt.semilogy(t,Umean, label='Average',linewidth=3)
    plt.semilogy(t,Umax, label='Max', linewidth=3)
    plt.xlabel('Time [s]')
    plt.ylabel('velocity magnitude [m/s]')
    #plt.title('Interesting Graph\nCheck it out')
    plt.title('Velocity Plot')
    plt.legend(frameon=False,loc='lower right')
    #plt.show()
    plt.draw()
    # Save in pdf format
    plt.savefig('sprsU.pdf')

def plotMass():
    # Initialize empty arrays
    t = []
    alpha = []
    # Open file and read row by row
    with open('../DataSummary.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            t.append(float(row[0]))
            alpha.append(float(row[4]))


    # Plot
    plt.figure(figsize=(250 /25.4, 200 / 25.4))
    plt.plot(t,alpha, linewidth=3)
    plt.xlabel('Time [s]')
    plt.ylabel('Average volume fraction')
    #plt.title('Interesting Graph\nCheck it out')
    plt.title('Mass plot')
    plt.legend(frameon=False,loc='upper left')
    #plt.show()
    plt.draw()

    # Save in pdf format
    plt.savefig('alphaOsc.pdf')

def plotPressure():
    # Initialize empty arrays
    t = []
    p = []
    # Open file and read row by row
    with open('../DataSummary.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            t.append(float(row[0]))
            p.append(float(row[7]))


    # Plot
    plt.figure(figsize=(250 /25.4, 200 / 25.4))
    plt.plot(t,p, linewidth=3)
    plt.xlabel('Time [s]')
    plt.ylabel('Maximum pressure difference [Pa]')
    #plt.title('Interesting Graph\nCheck it out')
    plt.title('Pressure Plot')
    plt.legend(frameon=False,loc='upper left')
    #plt.show()
    plt.draw()

    # Save in pdf format
    plt.savefig('pressure.pdf')


plotVelocity()
plotMass()
plotPressure()
#plt.show()
