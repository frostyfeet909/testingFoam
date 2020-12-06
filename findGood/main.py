# Finds all the good cases for a given tolerance
import findGood
from os.path import join, isfile


def main():
    print("\n")
    print("Good case finder!")
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

    print("Default 1% tol - enter if want:")

    # Setting error tolerance
    tol = raw_input(">> ")
    if tol == "":
        tol = 1.0
    else:
        tol = float(tol)

    findGood.main(tol)

    print("\n")
    print("[*] Done!")


if __name__ == "__main__":
    main()
