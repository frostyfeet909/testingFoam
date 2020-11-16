# Expanded version of Federico's plotData.py, plots the difference between two cases
import matplotlib.pyplot as plt
from dataInterface import get_data

# plt.rcParams.update({'font.size': 22})

# rcParams.update({'figure.autolayout': True})
# rcParams['font.family'] = 'serif'
# rcParams['font.serif'] = ['Computer Modern Roman']
# rcParams['text.usetex'] = True


def main():
    # Prepare the data and call functions to plot
    reference_data = get_data("referenceCase")
    temp_data = get_data("tempCase")

    t_ref = []
    umean_ref = []
    umax_ref = []
    mass_ref = []
    pressure_ref = []

    t_tmp = []
    umean_tmp = []
    umax_tmp = []
    mass_tmp = []
    pressure_tmp = []

    for data in reference_data:
        t_ref.append(float(data[0]))
        umean_ref.append(float(data[1]))
        umax_ref.append(float(data[2]))
        mass_ref.append(float(data[4]))
        pressure_ref.append(float(data[7]))

    for data in temp_data:
        t_tmp.append(float(data[0]))
        umean_tmp.append(float(data[1]))
        umax_tmp.append(float(data[2]))
        mass_tmp.append(float(data[4]))
        pressure_tmp.append(float(data[7]))

    plot_velocity(t_ref, t_tmp, umean_ref, umax_ref, umean_tmp, umax_tmp)
    plot_mass(t_ref, t_tmp, mass_ref, mass_tmp)
    plot_pressure(t_ref, t_tmp, pressure_ref, pressure_tmp)


def plot_velocity(t_ref, t_tmp, data_1_ref, data_2_ref, data_1_tmp, data_2_tmp):
    # Plots the data and adds info + saves the graph
    plt.figure(figsize=(250 / 25.4, 200 / 25.4))
    plt.semilogy(t_ref, data_1_ref, label='interFoam Average', linewidth=3)
    plt.semilogy(t_tmp, data_1_tmp, label='interPhaseFieldFoam Average', linewidth=3)
    plt.semilogy(t_ref, data_2_ref, label='interFoam Max', linewidth=3)
    plt.semilogy(t_tmp, data_2_tmp, label='interPhaseFieldFoam Max', linewidth=3)

    plt.xlabel('Time [s]')
    plt.ylabel('velocity magnitude [m/s]')
    plt.title('Velocity Plot')
    plt.legend(frameon=False, loc='lower right')
    plt.draw()

    # Save in pdf format
    plt.savefig('Ucomparison.pdf')


def plot_mass(t_ref, t_tmp, data_ref, data_tmp):
    # Plots the data and adds info + saves the graph
    plt.figure(figsize=(250 / 25.4, 200 / 25.4))
    plt.plot(t_ref, data_ref, label='interFoam', linewidth=3)
    plt.plot(t_tmp, data_tmp, label='interPhaseFieldFoam', linewidth=3)

    plt.xlabel('Time [s]')
    plt.ylabel('Average volume fraction')
    plt.title('Mass Plot')
    plt.legend(frameon=False, loc='lower right')
    plt.draw()

    # Save in pdf format
    plt.savefig('massComparison.pdf')


def plot_pressure(t_ref, t_tmp, data_ref, data_tmp):
    # Plots the data and adds info + saves the graph
    plt.figure(figsize=(250 / 25.4, 200 / 25.4))
    plt.plot(t_ref, data_ref, label='interFoam', linewidth=3)
    plt.plot(t_tmp, data_tmp, label='interPhaseFieldFoam', linewidth=3)

    plt.xlabel('Time [s]')
    plt.ylabel('Maximum pressure difference [Pa]')
    plt.title('Pressure Plot')
    plt.legend(frameon=False, loc='lower right')
    plt.draw()

    # Save in pdf format
    plt.savefig('pressureComparison.pdf')
