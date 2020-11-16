# modifies and retrieves entries from files
from csv import reader
from os.path import join


def get_data(case):
    # Get the data from the csv
    rows = []
    file_name = "DataSummary.csv"
    path = join("..", "resources")
    file_loc = join(path, case, file_name)

    with open(file_loc, 'r') as file:
        plots = reader(file, delimiter=',')

        for row in plots:
            rows.append(row)  # Because plots is NOT an iterable

    return rows


def get_good_data(path):
    # Get the good data from a txt file
    rows = []

    with open(path, 'r') as file:
        plots = reader(file, delimiter=',')

        for row in plots:
            rows.append(row)  # Because plots is NOT an iterable

    return rows
