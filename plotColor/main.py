# Application that runs all others, gets input and calls others.
import os
import plotColor
from subprocess import call


def main():
    print("Colormap creator!")
    print("Call fe41 first")

    working_dir = ("/".join([str(x) for x in os.getcwd().split("/")[:-1]]))
    if not os.path.exists(working_dir+'/data.csv'):
        print("[!!] No data.csv please make some cases first")
        raise SystemExit

    print("\n")
    print("Format: initial final")  # Format is very specific
    print("Epsilon conditions: ")
    ep_l, ep_h = raw_input(">> ").split(" ")
    print("X conditions: ")
    x_l, x_h = raw_input(">> ").split(" ")

    ep_l, ep_h, x_l, x_h = float(ep_l), float(ep_h), float(x_l), float(x_h)

    plotColor.main(working_dir, ep_l, ep_h, x_l, x_h)
    call(["./cleanup.run", working_dir, str(ep_l), str(ep_h), str(x_l), str(x_h)])

    print("[*] Done!")


if __name__ == "__main__":
    main()
