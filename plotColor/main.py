# Application that runs all others, gets input and calls others.
from os.path import join, isfile
import plotColor
from subprocess import call
from dataInterface import get_data


def main():
    print("\n")
    print("Colormap creator!")
    print("Call fe41 first")
    print("\n")

    # Checking for necessary resources
    if not isfile(join("..", "resources", "referenceCase", "DataSummary.csv")):
        print("[!!] A referenceCase is required in the resources folder")
        print("\n")
        return

    if not isfile(join("..", "resources", "data.csv")):
        print("[!!] You need some results first!")
        print("\n")
        return

    print("Axis need to be squarish")
    print("Therefore it's easier if you plot the colormap using a square data set you generated data for")

    if not isfile(join("..", "resources", "dataRanges.csv")):
        print("[!] Looks like you haven't run any data ranges yourself so using this script may be a little trickier")
        print("\n")
        choice = "0"

    else:
        data_ranges = get_data("dataRanges.csv")
        print("Here are the (hopefully) square ranges you have data for: ")
        print("\n")
        for ranges in data_ranges:
            print("Option %i" % (data_ranges.index(ranges)+1))
            print("Ep: %s %s %s" % (ranges[0], ranges[1], ranges[2]))
            print("X: %s %s %s" % (ranges[3], ranges[4], ranges[5]))
            print("\n")

        print("Pick the corresponding number or attempt to make your own by entering 0: ")
        choice = raw_input(">> ")
        print("\n")

    if choice == "0":
        print("Format: initial step_size final")  # Format is very specific
        print("Epsilon conditions: ")
        ep_l, ep_step, ep_h = raw_input(">> ").split(" ")
        print("X conditions: ")
        x_l, x_step, x_h = raw_input(">> ").split(" ")
    else:
        if choice == "":
            choice = 1

        ep_l, ep_step, ep_h, x_l, x_step, x_h = data_ranges[int(choice)-1]

    plotColor.main(ep_l, ep_step, ep_h, x_l, x_step, x_h)
    call(["./cleanup.run", ep_l, ep_h, x_l, x_h])

    print("\n")
    print("[*] Done!")


if __name__ == "__main__":
    main()
