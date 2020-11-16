# modifies and retrieves entries from files
from csv import reader, writer
from os.path import join


def get_data(file_name="data.csv"):
    # Get the data from the csv
    rows = []
    path = join("..", "resources")

    with open(join(path, file_name), 'r') as file:
        plots = reader(file, delimiter=',')

        for row in plots:
            rows.append(row)  # Because plots is NOT an iterable

    return rows


def write_data(val_name, values, per, ref, path=join("..")):
    # Write the good cases in text files and csv for referencing
    info = "There are " + str(len(values)) + " values " + str(per) + "% from " + str(ref)
    name_txt = join(path, "output", ("promising" + val_name + str(per) + "%.txt"))
    name_csv = join(path, "resources", ("promising" + val_name + str(per) + "%.csv"))

    with open(name_txt, 'w') as file:
        file.write(info)
        file.write("\n")
        file.write("\n")
        for i in values:
            file.write(str(i[0]) + "    " + str(i[1]))
            file.write("\n")

    with open(name_csv, 'w') as file:
        data_writer = writer(file)
        for i in values:
            ep_temp, x_temp = str(i[0]).split("x")
            data_writer.writerow([str(i[1]), ep_temp[2:], x_temp])
