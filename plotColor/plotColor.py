# Main application, plots color maps of all the global variables
import matplotlib.pyplot as plt
from numpy import meshgrid
from dataInterface import get_data
import subprocess
from os.path import join

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
    ep_range = range_temp.communicate()[0].split("\n")[:-1]
    range_temp = subprocess.Popen(['seq', x_l, x_step, x_h], stdout=subprocess.PIPE)  # Don't even ask
    x_range = range_temp.communicate()[0].split("\n")[:-1]

    """
    for sim in data:
        ep_temp = float(sim[8])
        x_temp = float(sim[9])

        # element = [ep_temp, x_temp]
        if ep_temp not in ep:
            if ep_l <= ep_temp <= ep_h:
                ep.append(ep_temp)
        if x_temp not in x:
            if x_l <= x_temp <= x_h:
                x.append(x_temp)
    """

    # The methods I'm working on to stop the colormaps looking clustered when there is a high concentration of data in
    # part of the domain I'm interested in, attempt 2 which is currently in use can cause blank spaces in the graph but
    # it works. Attempt 4 will be same as attempt 3 but it will find c_ep and c_x itself this could still have problems
    # where c values just don't line up right so another fix could be for the user to define the step size of ep and x,
    # as it would guarantee a square grid and all values would exist but this would get annoying fast. I suppose I could
    # leave this as an option to the user, computer picks and hopefully does good or user spends some time to get a
    # perfect one, oooh I could also return how many values are found and ask the user is okay, if not try a different
    # method - I think I'll try this.
    # The reason is that the concentration of data across all ep and x varies as all cases are stored in the dataset so
    # the graph can look a little funny, trying to fix this by making a square grid for the required range.
    # The old plotColor works because datasets were always square as that's how I designed the ep, x values whenever I
    # made a new one.
    """
    # Attempt 1
    if len(x) < len(ep):
        close = []
        for sim in data:
            x_temp = float(sim[9])
            if x_temp not in x:
                if x_l <= x_temp <= x_h:
                    pass
                else:
                    close.append(x_temp)

        while len(x) < len(ep):
            x.append(min(close, key=lambda y: abs(y - (x_h-x_l))))
            if not close:
                raw_input(">> Could not balance lists")
                break

    elif len(x) > len(ep):
        close = []
        for sim in data:
            ep_temp = float(sim[9])
            if ep_temp not in ep:
                if ep_l <= ep_temp <= ep_h:
                    pass
                else:
                    close.append(ep_temp)

        while len(x) > len(ep):
            ep.append(min(close, key=lambda y: abs(y - (ep_h-ep_l))))
            if not close:
                raw_input(">> Could not balance lists")
                break
    """

    """
    # Attempt 2

    # Reduce size of longer variable until they match
    while len(x) < len(ep):
        ep.remove(max(ep, key=lambda y: abs(y - (ep_h - ep_l))))

    while len(x) > len(ep):
        x.remove(max(x, key=lambda y: abs(y - (x_h - x_l))))
    # Stab randomly and hope it works
    """

    """
    # Attempt 3
    if [c_ep, c_x] not in board_initial:
        print("[!!] No centre!")
        raise SystemExit
    else:
        ep_i = ep.index(c_ep)
        x_i = x.index(c_x)
        board_final.add([ep_i, x_i])

    for i in range(0, min(len(ep) - ep_i, ep_i - len(ep), len(x) - x_i, x_i - len(x))):
        conditions = {[ep[ep_i + i], x[x_i]], [ep[ep_i - i], x[x_i]], [ep[ep_i], x[x_i + i]], [ep[ep_i], x[x_i - i]],
                      [ep[ep_i + i], x[x_i + i]], [ep[ep_i - i], x[x_i - i]], [ep[ep_i + i], x[x_i - i]],
                      [ep[ep_i - i], x[x_i + i]]}
        if all(condition in board_initial for condition in conditions):
            board_final.update(conditions)

    # Resizing ep and x
    ep = []
    x = []
    for element in board_final:
        if element[0] not in ep:
            ep.append(element[0])
        if element[1] not in x:
            x.append(element[1])

    ep.sort()
    x.sort()
    """

    """
    # Attempt 4
    if [c_ep, c_x] not in board_initial:
        print("[!!] No centre!")
        raise SystemExit
    else:
        ep_start = ep.index(ep_l)
        x_start = x.index(x_l)
        ep_end = ep.index(ep_h)
        x_end = x.index(x_h)
        # board_final.add([ep_l, ])

    i = 0
    current = [ep_start + i, x_start + i]
    while current[0] <= ep_end and current[1] <= x_end:
        for j in range(0, min(len(ep) - ep_i, ep_i - len(ep), len(x) - x_i, x_i - len(x))):
            pass
        i += 1
        current = [ep_start + i, x_start + i]
    """

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

    # Make the arrays
    umean_ref = float(data_ref[1])
    umax_ref = float(data_ref[2])
    mass_ref = float(data_ref[4])
    pressure_ref = float(data_ref[7])

    for sim in data:
        ep_temp = sim[8]
        x_temp = sim[9]

        if ep_temp in ep_range and x_temp in x_range:
            i = ep_range.index(ep_temp)
            j = x_range.index(x_temp)

            umean_data[i][j] = abs(float(sim[1])-umean_ref)
            umax_data[i][j] = abs(float(sim[2])-umax_ref)
            mass_data[i][j] = abs(float(sim[4])-mass_ref)
            pressure_data[i][j] = abs(float(sim[7])-pressure_ref)

    return ep_range, x_range, umean_data, umax_data, mass_data, pressure_data


def plot(colors, ep_l, ep_step, ep_h, x_l, x_step, x_h):
    # Plots the colormaps
    ep, x, umean_data, umax_data, mass_data, pressure_data = catalogue_data(ep_l, ep_step, ep_h, x_l, x_step, x_h)
    x, y = meshgrid(ep, x)

    if len(x) > 1 and len(y) > 1:
        for color in colors:
            plt.figure(figsize=(250 / 25.4, 200 / 25.4))
            plt.pcolormesh(x, y, umean_data, cmap=plt.cm.get_cmap(color), shading='auto')
            plot_velocity_mean(color)

            plt.figure(figsize=(250 / 25.4, 200 / 25.4))
            plt.pcolormesh(x, y, umax_data, cmap=plt.cm.get_cmap(color), shading='auto')
            plot_velocity_max(color)

            plt.figure(figsize=(250 / 25.4, 200 / 25.4))
            plt.pcolormesh(x, y, mass_data, cmap=plt.cm.get_cmap(color), shading='auto')
            plot_mass(color)

            plt.figure(figsize=(250 / 25.4, 200 / 25.4))
            plt.pcolormesh(x, y, pressure_data, cmap=plt.cm.get_cmap(color), shading='auto')
            plot_pressure(color)
    else:
        print("[!] Not enough data points to plot maps")


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
