# Application that runs all others, gets input and calls others.
from os.path import join, isdir
from subprocess import call
from dataInterface import remove_dupes, write_data


def main():
    print("Case generator!")
    print("Call fe41 first")

    # Checking for necessary resources
    if not isdir(join("..", "resources", "baseCase")):
        print("[!!] Need baseCase in here!")
        return

    print("\n")
    print("Format: initial step_size final")  # Format is very specific
    
    print("Epsilon conditions: ")
    ep_l, ep_step, ep_h = raw_input(">> ").split(" ")
    print("X conditions: ")
    x_l, x_step, x_h = raw_input(">> ").split(" ")

    write_data(ep_l, ep_step, ep_h, x_l, x_step, x_h)

    call(["./generate.run", ep_l, ep_step, ep_h, x_l, x_step, x_h])
    remove_dupes()
    remove_dupes("dataRanges.csv")

    print("[*] Done!")


if __name__ == "__main__":
    main()
