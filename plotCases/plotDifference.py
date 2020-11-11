# Expanded version of Federico's plotData.py, plots the difference between two cases - Needs some work but does work
import scipy
import numpy as np
from matplotlib import rcParams
import csv
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 22})

rcParams.update({'figure.autolayout': True})
rcParams['font.family'] = 'serif'
rcParams['font.serif'] = ['Computer Modern Roman']
rcParams['text.usetex'] = True


def main():
    plotVelocity()
    plotMass()
    plotPressure()


def plotVelocity():
    # Initialize empty arrays
    tIF = []
    tPF = []
    Umean = []
    Umax = []
    UmeanIF = []
    UmeanPF = []
    UmaxIF = []
    UmaxPF = []

    # Open file and read row by row
    with open(('referenceCase/DataSummary.csv'), 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            tIF.append(float(row[0]))
            UmeanIF.append(float(row[1]))
            UmaxIF.append(float(row[2]))

    with open(('tempCase/DataSummary.csv'), 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            tPF.append(float(row[0]))
            UmeanPF.append(float(row[1]))
            UmaxPF.append(float(row[2]))
    """
    for i in range(0, len(tIF)):
        Umax.append(abs(UmaxPF[i]-UmaxIF[i]))
        Umean.append(abs(UmeanPF[i]-UmeanIF[i]))

    # Plot
    plt.figure(figsize=(250 /25.4, 200 / 25.4))
    plt.semilogy(tIF,Umean, label='Average',linewidth=3)
    plt.semilogy(tIF,Umax, label='Max', linewidth=3)
    plt.xlabel('Time [s]')
    plt.ylabel('Magnitude of the difference in velocity magnitude [m/s]')
    #plt.title('Interesting Graph\nCheck it out')
    plt.title('Velocity Plot')
    plt.legend(frameon=False,loc='lower right')
    #plt.show()
    plt.draw()
    # Save in pdf format
    plt.savefig('Udiff.pdf')
    """
    plt.figure(figsize=(250 / 25.4, 200 / 25.4))
    plt.semilogy(tIF, UmeanIF, label='interFoam Average', linewidth=3)
    plt.semilogy(tPF, UmeanPF, label='interPhaseFieldFoam Average', linewidth=3)
    plt.semilogy(tIF, UmaxIF, label='interFoam Max', linewidth=3)
    plt.semilogy(tPF, UmaxPF, label='interPhaseFieldFoam Max', linewidth=3)
    plt.xlabel('Time [s]')
    plt.ylabel('velocity magnitude [m/s]')
    # plt.title('Interesting Graph\nCheck it out')
    plt.title('Velocity Plot')
    plt.legend(frameon=False, loc='lower right')
    # plt.show()
    plt.draw()
    # Save in pdf format
    plt.savefig('Ucomparison.pdf')


def plotMass():
    # Initialize empty arrays
    tIF = []
    tPF = []
    alpha = []
    alphaIF = []
    alphaPF = []
    # Open file and read row by row
    with open(('referenceCase/DataSummary.csv'), 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            tIF.append(float(row[0]))
            alphaIF.append(float(row[4]))

    with open(('tempCase/DataSummary.csv'), 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            tPF.append(float(row[0]))
            alphaPF.append(float(row[4]))
    """
    for i in range(0, len(tIF)):
        alpha.append(abs(alphaPF[i]-alphaIF[i]))


    # Plot
    plt.figure(figsize=(250 /25.4, 200 / 25.4))
    plt.plot(tIF,alpha, linewidth=3)
    plt.xlabel('Time [s]')
    plt.ylabel('Magnitude of the difference in Average volume fraction')
    #plt.title('Interesting Graph\nCheck it out')
    plt.title('Mass plot')
    plt.legend(frameon=False,loc='upper left')
    #plt.show()
    plt.draw()

    # Save in pdf format
    plt.savefig('massDiff.pdf')
    """
    plt.figure(figsize=(250 / 25.4, 200 / 25.4))
    plt.plot(tIF, alphaIF, label='interFoam', linewidth=3)
    plt.plot(tPF, alphaPF, label='interPhaseFieldFoam', linewidth=3)
    plt.xlabel('Time [s]')
    plt.ylabel('Average volume fraction')
    # plt.title('Interesting Graph\nCheck it out')
    plt.title('Mass Plot')
    plt.legend(frameon=False, loc='lower right')
    # plt.show()
    plt.draw()
    # Save in pdf format
    plt.savefig('massComparison.pdf')


def plotPressure():
    # Initialize empty arrays
    tIF = []
    tPF = []
    p = []
    pIF = []
    pPF = []
    # Open file and read row by row
    with open(('referenceCase/DataSummary.csv'), 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            tIF.append(float(row[0]))
            pIF.append(float(row[7]))

    with open(('tempCase/DataSummary.csv'), 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            tPF.append(float(row[0]))
            pPF.append(float(row[7]))
    """
    for i in range(0, len(tIF)):
        p.append(abs(pPF[i]-pIF[i]))

    # Plot
    plt.figure(figsize=(250 /25.4, 200 / 25.4))
    plt.plot(tIF,p, linewidth=3)
    plt.xlabel('Time [s]')
    plt.ylabel('Magnitude of the difference in Maximum pressure difference [Pa]')
    #plt.title('Interesting Graph\nCheck it out')
    plt.title('Pressure Plot')
    plt.legend(frameon=False,loc='upper left')
    #plt.show()
    plt.draw()

    # Save in pdf format
    plt.savefig('pressureDiff.pdf')
    """
    plt.figure(figsize=(250 / 25.4, 200 / 25.4))
    plt.plot(tIF, pIF, label='interFoam', linewidth=3)
    plt.plot(tPF, pPF, label='interPhaseFieldFoam', linewidth=3)
    plt.xlabel('Time [s]')
    plt.ylabel('Maximum pressure difference [Pa]')
    # plt.title('Interesting Graph\nCheck it out')
    plt.title('Pressure Plot')
    plt.legend(frameon=False, loc='lower right')
    # plt.show()
    plt.draw()
    # Save in pdf format
    plt.savefig('pressureComparison.pdf')
