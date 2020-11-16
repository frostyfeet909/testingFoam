# Wrapper for all applications
import os
from time import time


def main():
    print("\n")
    print("Welcome!")
    print("\n")
    print("Choose you application:")
    print("1 - findGood")
    print("2 - generateData")
    print("3 - plotCases")
    print("4 - plotColor")

    choice = 1
    base_path = os.path.dirname(os.path.realpath(__file__))

    while choice != "" and choice != "q" and choice != "exit" and choice != "stop":
        choice = raw_input(">> ")

        elapsed = time()
        if choice == "1":
            try:
                from findGood import main as app_main
                os.chdir("findGood")
                app_main.main()
            except ImportError or OSError:
                print("[!!] Could not find findGood")

        elif choice == "2":
            try:
                from generateData import main as app_main
                os.chdir("generateData")
                app_main.main()
            except ImportError or OSError:
                print("[!!] Could not find generateData")

        elif choice == "3":
            try:
                from plotCases import main as app_main
                os.chdir("plotCases")
                app_main.main()
            except ImportError or OSError:
                print("[!!] Could not find plotCases")

        elif choice == "4":
            try:
                from plotColor import main as app_main
                os.chdir("plotColor")
                app_main.main()
            except ImportError or OSError:
                print("[!!] Could not find plotColor")

        else:
            print("[!!] Bye!")
            raise SystemExit

        os.chdir(base_path)
        elapsed = time() - elapsed
        print("That took %s minutes" % str(round(elapsed / 60)))
        print("\n")


if __name__ == "__main__":
    main()
