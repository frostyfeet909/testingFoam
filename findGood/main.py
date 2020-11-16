# Finds all the good cases for a given tolerance
import findGood
from os.path import join, isfile


def main():
    print("Good case finder!")

    # Checking for necessary resources
    if not isfile(join("..", "resources", "referenceCase", "DataSummary.csv")):
        print("[!!] Need referenceCase in here!")
        return

    if not isfile(join("..", "resources", "data.csv")):
        print("[!!] Need data.csv in here!")
        return

    print("\n")
    print("Default 1% tol - enter if want: mass pressure Umean Umax")

    # Setting error tolerance
    tol = raw_input(">> ")
    if tol == "":
        tol = 1.0
    else:
        tol = float(tol)

    findGood.main(tol)


if __name__ == "__main__":
    main()
