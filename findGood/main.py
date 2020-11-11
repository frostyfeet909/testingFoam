# Finds all the good cases for a given tolerance
import findGood
import os


def main():
    print("Good case finder!")

    if not os.path.isdir('referenceCase'):
        print("[!!] Need referenceCase in here!")
        raise SystemExit
    working_dir = ("/".join([str(x) for x in os.getcwd().split("/")[:-1]]))

    print("\n")
    print("Default 1% tol - enter if want: mass pressure Umean Umax")

    # Setting error tolerance
    tol = raw_input(">> ")
    if tol == "":
        tol = 1.0
    else:
        tol = float(tol)

    """
    if " " in tol:
        m, p, u_mean, u_max = tol.split(" ")
        m, p, u_mean, u_max = float(m), float(p), float(u_mean), float(u_max)
    else:
        m, p, u_mean, u_max = 1.0, 1.0, 1.0, 1.0
    """

    findGood.main(working_dir, tol)


if __name__ == "__main__":
    main()
