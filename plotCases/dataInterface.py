# modifies and retrieves entries from files
from csv import reader
from fileinput import FileInput


def get_data(path, file_name="/data.csv"):
    # Get the data from the csv
    rows = []

    with open((path + file_name), 'r') as file:
        plots = reader(file, delimiter=',')

        for row in plots:
            rows.append(row)  # Because plots is NOT an iterable

    return rows


def remove_dupes(path):
    # Removes dupes from the csv
    # This function runs way faster than I though it would

    seen = set()  # set for O(1)
    for line in FileInput((path + "/data.csv"), inplace=1):
        if line in seen:
            continue  # skip duplicate

        seen.add(line)
        print line,  # Standard output is now redirected to the file


def get_good_data(path):
    # Get the good data from a txt file
    values = []

    with open(path, 'r') as file:
        lines = file.readlines()

    for line in lines[2:]:
        ep_temp, x_temp = line.split("    ")[0].split("x")
        values.append([ep_temp[2:], x_temp])

    return values
