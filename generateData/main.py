# Application that runs all others, gets input and calls others.
import os
from time import time
from subprocess import call
from dataInterface import remove_dupes


def main():
    print("Case generator!")
    print("Call fe41 first")

    if not os.path.isdir('baseCase'):
        print("[!!] Need baseCase in here!")
        raise SystemExit

    working_dir = ("/".join([str(x) for x in os.getcwd().split("/")[:-1]]))

    print("\n")
    print("Format: initial step_size final")  # Format is very specific
    
    print("Epsilon conditions: ")
    ep_l, ep_step, ep_h = raw_input(">> ").split(" ")
    print("X conditions: ")
    x_l, x_step, x_h = raw_input(">> ").split(" ")

    elapsed = time()
    call(["./generate.run", ep_l, ep_step, ep_h, x_l, x_step, x_h, working_dir])
    remove_dupes(working_dir)
    elapsed = time()-elapsed
    
    print("That took %s minutes" % str(round(elapsed/60)))
    print("[*] Done!")


if __name__ == "__main__":
    main()
