# modifies and retrieves entries from files
from csv import writer
from fileinput import FileInput
from os.path import join


def write_data(ep_l, ep_step, ep_h, x_l, x_step, x_h):
    # Saves the computed range of data

    file_loc = join("..", "resources", "dataRanges.csv")
    with open(file_loc, 'a') as file:
        data_writer = writer(file)
        data_writer.writerow([ep_l, ep_step, ep_h, x_l, x_step, x_h])


def remove_dupes(file_name="data.csv"):
    # Removes dupes from the csv
    # This function runs way faster than I though it would

    path = join("..", "resources")
    seen = set()  # set for O(1)
    for line in FileInput(join(path, file_name), inplace=1):
        if line in seen:
            continue  # skip duplicate

        seen.add(line)
        print line,  # Standard output is now redirected to the file
