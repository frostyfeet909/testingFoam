# Application that runs all others, gets input and calls others.
import os
import plotDifference
from subprocess import call
from dataInterface import get_good_data


def main():
    # Runs the whole thing
    print("Case plotter!")
    print("Call fe41 first")

    if not os.path.isdir('baseCase'):
        print("[!!] Need baseCase in here!")
        raise SystemExit

    promising = raw_input("Do you want to plot the promising [y/n]: ")
    keep = raw_input("Do you want to keep the sims [y/n]: ")

    if keep == "":
        keep = "y"

    working_dir = ("/".join([str(x) for x in os.getcwd().split("/")[:-1]]))
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
            path = working_dir + "/" + "promising" + val + str(tol) + "%.txt"

            if not os.path.isfile(path):
                print("[!] This promising doesn't exist: %s" % path)
                raw_input(">> ")
                continue

            values = get_good_data(path)

            for value in values:
                call(["./generate.run", str(value[0]), str(value[1])])
                plotDifference.main(working_dir)
                call(["./cleanup.run", working_dir, str(value[0]), str(value[1]), keep])

    elif promising == "n":
        print("Epsilon: ")
        ep = raw_input(">> ")
        print("X: ")
        x = raw_input(">> ")

        call(["./generate.run", str(ep), str(x)])
        plotDifference.main(working_dir)
        call(["./cleanup.run", working_dir, str(ep), str(x), keep])

    print("[*] Done!")


if __name__ == "__main__":
    main()
