# Application that runs all others, gets input and calls others.
from os.path import isfile, join
import plotDifference
from subprocess import call
from dataInterface import get_good_data


def main():
    # Runs the whole thing
    print("Case plotter!")
    print("Call fe41 first")

    # Checking for necessary resources
    if not isfile(join("..", "resources", "referenceCase", "DataSummary.csv")):
        print("[!!] Need referenceCase in here!")
        return

    promising = raw_input("Do you want to plot the promising [y/n]: ")
    keep = raw_input("Do you want to keep the sims [y/n]: ")

    if keep == "":
        keep = "y"

    print("\n")

    if promising == "y" or promising == "":
        print("Default mass promising - enter m or p or umean or umax (or any combination):")

        val_names = []
        names = raw_input(">> ")
        if names != "":
            names = names.split(" ")
            for name in names:
                name_prepped = name.lower().strip()
                if name_prepped == "m":
                    val_names.append("mass")
                if name_prepped == "p":
                    val_names.append("pressure")
                if name_prepped == "umean":
                    val_names.append("velocity_mean")
                if name_prepped == "umax":
                    val_names.append("velocity_max")
        else:
            val_names.append("mass")

        print("Default 1% tol - enter if want:")
        tol = raw_input(">> ")

        if tol == "":
            tol = 1.0
        else:
            tol = float(tol)

        for val in val_names:
            path = join("..", "resources", ("promising" + val + str(tol) + "%.txt"))

            if not isfile(path):
                print("[!] This promising doesn't exist: %s" % path)
                raw_input(">> ")
                continue

            values = get_good_data(path)

            for value in values:
                call(["./generate.run", str(value[0]), str(value[1])])
                plotDifference.main()
                call(["./cleanup.run", str(value[0]), str(value[1]), keep])

    elif promising == "n":
        print("Epsilon: ")
        ep = raw_input(">> ")
        print("X: ")
        x = raw_input(">> ")

        call(["./generate.run", str(ep), str(x)])
        plotDifference.main()
        call(["./cleanup.run", str(ep), str(x), keep])

    print("[*] Done!")


if __name__ == "__main__":
    main()
