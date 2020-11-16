# modifies and retrieves entries from files
from csv import reader
from os.path import join


def get_data(file_name="data.csv"):
    # Get the data from the csv
    rows = []
    path = join("..", "resources")
    file_loc = join(path, file_name)

    with open(file_loc, 'r') as file:
        plots = reader(file, delimiter=',')

        for row in plots:
            rows.append(row)  # Because plots is NOT an iterable

    return rows
