# Main application, plots color maps of all the global variables
import matplotlib.pyplot as plt
from numpy import meshgrid, linspace
from dataInterface import get_data
import subprocess
from os.path import join
from subprocess import call
from matplotlib.ticker import FormatStrFormatter

plt.rcParams.update({'font.size': 22})


class Fruit:
    # Not a vegetable
    def __init__(self):
        self.inside = "Mushy"


def main(ep_l, ep_step, ep_h, x_l, x_step, x_h):
    # Creates 3 different type of color maps per global quantity
    colors = ['Reds', 'seismic', 'tab20']
    plot(colors, ep_l, ep_step, ep_h, x_l, x_step, x_h)

    banana = Fruit()


def catalogue_data(ep_l, ep_step, ep_h, x_l, x_step, x_h):
    # Checks the cases and generates 2D arrays that works with pcolormesh
    data = get_data()
    data_ref = get_data(join("referenceCase", "DataSummary.csv"))[-1]
    mass_data = []
    umean_data = []
    umax_data = []
    pressure_data = []
    # ep = [] x = [] Need to get the exact range used by bash - I've seen some floating point errors with numpy doing
    # it so this is a dirty workaround I'll make better later
    range_temp = subprocess.Popen(['seq', ep_l, ep_step, ep_h], stdout=subprocess.PIPE)  # Don't even ask
    ep_range = format_number_list(range_temp.communicate()[0].split("\n")[:-1])
    range_temp = subprocess.Popen(['seq', x_l, x_step, x_h], stdout=subprocess.PIPE)  # Don't even ask
    x_range = format_number_list(range_temp.communicate()[0].split("\n")[:-1])
    points = []

    for ep in ep_range:
        for x in x_range:
            points.append([ep, x])

    # Pre-allocating big arrays
    for i in range(0, len(ep_range)):
        mass_data.append([])
        umean_data.append([])
        umax_data.append([])
        pressure_data.append([])
        for j in range(0, len(x_range)):
            mass_data[i].append(0)
            umean_data[i].append(0)
            umax_data[i].append(0)
            pressure_data[i].append(0)

    # Get the reference values
    umean_ref = float(data_ref[1])
    umax_ref = float(data_ref[2])
    mass_ref = float(data_ref[4])
    pressure_ref = float(data_ref[7])

    add_data(data, points, ep_range, x_range, umean_data, umax_data, mass_data, pressure_data, umean_ref, umax_ref,
             mass_ref, pressure_ref)

    # Any points that could not be found will be generated
    for point in points:
        call(["./generate.run", point[0], point[1]])
    data = get_data()

    add_data(data, points, ep_range, x_range, umean_data, umax_data, mass_data, pressure_data, umean_ref, umax_ref,
             mass_ref, pressure_ref)

    return ep_range, x_range, umean_data, umax_data, mass_data, pressure_data


def add_data(data, points, ep_range, x_range, umean_data, umax_data, mass_data, pressure_data, umean_ref, umax_ref,
             mass_ref, pressure_ref):
    # Adds data correctly to a dict for a colormap
    for sim in data:
        ep = format_number(sim[8])
        x = format_number(sim[9])

        if [ep, x] in points:
            points.remove([ep, x])
            i = ep_range.index(ep)
            j = x_range.index(x)

            umean_data[i][j] = abs(float(sim[1]) - umean_ref)
            umax_data[i][j] = abs(float(sim[2]) - umax_ref)
            mass_data[i][j] = abs(float(sim[4]) - mass_ref)
            pressure_data[i][j] = abs(float(sim[7]) - pressure_ref)


def plot(colors, ep_l, ep_step, ep_h, x_l, x_step, x_h):
    # Plots the colormaps
    ep, x, umean_data, umax_data, mass_data, pressure_data = catalogue_data(ep_l, ep_step, ep_h, x_l, x_step, x_h)

    ticks_x, tick_labels_x = set_axis(ep, rounding=3, max_ticks=6)
    ticks_y, tick_labels_y = set_axis(x)

    x, y = meshgrid(format_number_list(ep), format_number_list(x))

    if len(x) > 1 and len(y) > 1:
        for color in colors:
            plt.figure(figsize=(250 / 25.4, 200 / 25.4))
            plt.xticks(ticks_x, tick_labels_x)
            plt.yticks(ticks_y, tick_labels_y)
            # Axis swap - through testing could see that this is required
            plt.pcolormesh(y, x, umean_data, cmap=plt.cm.get_cmap(color), shading='auto')
            plot_velocity_mean(color)

            plt.figure(figsize=(250 / 25.4, 200 / 25.4))
            plt.xticks(ticks_x, tick_labels_x)
            plt.yticks(ticks_y, tick_labels_y)
            plt.pcolormesh(y, x, umax_data, cmap=plt.cm.get_cmap(color), shading='auto')
            plot_velocity_max(color)

            plt.figure(figsize=(250 / 25.4, 200 / 25.4))
            plt.xticks(ticks_x, tick_labels_x)
            plt.yticks(ticks_y, tick_labels_y)
            plt.pcolormesh(y, x, mass_data, cmap=plt.cm.get_cmap(color), shading='auto')
            plot_mass(color)

            plt.figure(figsize=(250 / 25.4, 200 / 25.4))
            plt.xticks(ticks_x, tick_labels_x)
            plt.yticks(ticks_y, tick_labels_y)
            plt.pcolormesh(y, x, pressure_data, cmap=plt.cm.get_cmap(color), shading='auto')
            plot_pressure(color)
    else:
        print("[!] Not enough data points to plot maps")


def format_number_list(num_list):
    new_num_list = []

    for num in num_list:
        new_num = format_number(num)
        new_num_list.append(new_num)

    return new_num_list


def format_number(num):
    num = str(num)
    if "." in num:
        relevant = False
        new_num = ""
        for i in num[::-1]:
            if i != "0":
                relevant = True

            if relevant:
                new_num += i

        new_num = new_num[::-1]
        if new_num[-1] == ".":
            new_num = new_num[:-1]
    else:
        new_num = num

    return new_num


def set_axis(ax, rounding=2, max_ticks=10, min_ticks=3):
    num_ticks = round(len(ax) / 3)
    tick_labels = []

    if num_ticks < min_ticks:
        num_ticks = min_ticks
    elif num_ticks > max_ticks:
        num_ticks = max_ticks

    ticks = list(linspace(0, len(ax)-1, num_ticks))

    for i in range(0, len(ticks)):
        ticks[i] = int(round(ticks[i]))
        tick_labels.append(round(float(ax[ticks[i]]), rounding))

    return ticks, tick_labels


def plot_velocity_mean(color):
    # Finds the right data and adds info + saves the graph
    plt.colorbar(label='Difference in velocity magnitude [m/s]', spacing='proportional')
    plt.xlabel('Epsilon - Interface Thickness')
    plt.ylabel('X - Mobility Factor')
    plt.title('Velocity at the last time step')

    # Save in pdf format
    plt.savefig('Umean' + color + '.pdf')


def plot_velocity_max(color):
    # Finds the right data and adds info + saves the graph
    plt.colorbar(label='Difference in velocity magnitude [m/s]', spacing='proportional')
    plt.xlabel('Epsilon - Interface Thickness')
    plt.ylabel('X - Mobility Factor')
    plt.title('Velocity at the last time step')

    # Save in pdf format
    plt.savefig('Umax' + color + '.pdf')


def plot_mass(color):
    # Finds the right data and adds info + saves the graph
    plt.colorbar(label='Difference in Average volume fraction', spacing='proportional')
    plt.xlabel('Epsilon - Interface Thickness')
    plt.ylabel('X - Mobility Factor')
    plt.title('Mass at the last time step')

    # Save in pdf format
    plt.savefig('alphaOsc' + color + '.pdf')


def plot_pressure(color):
    # Finds the right data and adds info + saves the graph
    plt.colorbar(label='Difference in Maximum pressure difference [Pa]', spacing='proportional')
    plt.xlabel('Epsilon - Interface Thickness')
    plt.ylabel('X - Mobility Factor')
    plt.title('Pressure at the last time step')

    # Save in pdf format
    plt.savefig('pressure' + color + '.pdf')
