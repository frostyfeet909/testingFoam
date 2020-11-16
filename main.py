# Wrapper for all applications
import os


def main(base_path):
    print("Welcome!")
    print("\n")
    print("Choose you application:")
    print("1 - findGood")
    print("2 - generateData")
    print("3 - plotCases")
    print("4 - plotColor")
    choice = raw_input(">> ")

    if choice == "1":
        try:
            from findGood import main as app_main
        except:
            print("[!!] Could not find findGood")
            raise SystemExit

        os.chdir("findGood")

    elif choice == "2":
        try:
            from generateData import main as app_main
        except:
            print("[!!] Could not find generateData")
            raise SystemExit

        os.chdir("generateData")

    elif choice == "3":
        try:
            from plotCases import main as app_main
        except:
            print("[!!] Could not find plotCases")
            raise SystemExit

        os.chdir("plotCases")

    elif choice == "4":
        try:
            from plotColor import main as app_main
        except:
            print("[!!] Could not find plotColor")
            raise SystemExit

        os.chdir("plotColor")

    else:
        print("[!!] Bye!")
        raise SystemExit

    app_main.main()
    os.chdir(base_path)
    main(base_path)  # Recursion


if __name__ == "__main__":
    base = os.getcwd()
    main(base)
