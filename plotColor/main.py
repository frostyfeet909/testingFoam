# Application that runs all others, gets input and calls others.
from os.path import join, isfile
import plotColor
from subprocess import call
from dataInterface import get_data


def main():
    print("Colormap creator!")
    print("Call fe41 first")

    # Checking for necessary resources
    if not isfile(join("..", "resources", "referenceCase", "DataSummary.csv")):
        print("[!!] Need referenceCase in here!")
        return

    if not isfile(join("..", "resources", "data.csv")):
        print("[!!] Need data.csv in here!")
        return

    print("\n")

    data_ranges = get_data("dataRanges.csv")
    print("Axis need to be squarish")
    print("Here are the (hopefully) square ranges you have data for: ")
    for ranges in data_ranges:
        print("Ep: %s %s %s" % (ranges[0], ranges[1], ranges[2]))
        print("X: %s %s %s" % (ranges[3], ranges[4], ranges[5]))
        print("\n")

    print("Pick the corresponding number or attempt to make your own by entering 0: ")
    choice = raw_input(">> ")

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

    print("[*] Done!")


if __name__ == "__main__":
    main()
