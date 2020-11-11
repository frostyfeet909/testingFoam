# Finds all the good cases and saves them in text files

# from operator import itemgetter
from dataInterface import get_data

"""
VELOCITY_MEAN_REF = 0.49415299
VELOCITY_MAX_REF = 2.2207486
MASS_REF = 0.12907008
PRESSURE_REF = 1114.6359
"""


def main(working_dir, tol):
    # Runs the rest of the program

    # os.chdir(working_dir)
    catalogue_data(working_dir, tol)


def find_reference_values(working_dir):
    # Finds the reference values from the last-line of the reference case
    data = get_data(working_dir+"/findGood/referenceCase", "/DataSummary.csv")[-1]
    umean_ref = float(data[1])
    umax_ref = float(data[2])
    mass_ref = float(data[4])
    pressure_ref = float(data[7])
    return umean_ref, umax_ref, mass_ref, pressure_ref


def write_data(working_dir, val_name, values, per, ref):
    # Write the good cases in text files
    info = "There are " + str(len(values)) + " values " + str(per) + "% from " + str(ref)
    name = working_dir + "/promising" + val_name + str(per) + "%.txt"

    with open(name, 'w') as file:
        file.write(info)
        file.write("\n")
        file.write("\n")
        for i in values:
            file.write(str(i[0]) + "    " + str(i[1]))
            file.write("\n")


def catalogue_data(working_dir, tol):
    # Find and catalogue the good cases

    data = get_data(working_dir)
    u_mean_ref, u_max_ref, m_ref, p_ref = find_reference_values(working_dir)
    mass_data = {}
    umean_data = {}
    umax_data = {}
    pressure_data = {}

    for sim in data:
        key_name = "ep" + str(sim[8]) + "x" + str(sim[9])

        m_l = (1.0 - (tol / 100.0)) * m_ref
        m_h = (1.0 + (tol / 100.0)) * m_ref
        m_value = float(sim[4])
        if m_l <= m_value <= m_h:
            mass_data[key_name] = m_value

        p_l = (1.0 - (tol / 100.0)) * p_ref
        p_h = (1.0 + (tol / 100.0)) * p_ref
        p_value = float(sim[7])
        if p_l <= p_value <= p_h:
            pressure_data[key_name] = p_value

        u_mean_l = (1.0 - (tol / 100.0)) * u_mean_ref
        u_mean_h = (1.0 + (tol / 100.0)) * u_mean_ref
        u_mean_value = float(sim[1])
        if u_mean_l <= u_mean_value <= u_mean_h:
            umean_data[key_name] = u_mean_value

        u_max_l = (1.0 - (tol / 100.0)) * u_max_ref
        u_max_h = (1.0 + (tol / 100.0)) * u_max_ref
        u_max_value = float(sim[2])
        if u_max_l <= u_max_value <= u_max_h:
            umax_data[key_name] = u_max_value

    # Apparently python2 dictionaries are unordered so....

    # Sort in ascending order of value
    # mass_sorted = sorted(mass_data.items(), key=itemgetter(1))
    # pressure_sorted = sorted(pressure_data.items(), key=itemgetter(1))
    # umean_sorted = sorted(umean_data.items(), key=itemgetter(1))
    # umax_sorted = sorted(umax_data.items(), key=itemgetter(1))

    # Sort on proximity to the reference value
    mass_sorted = sorted(mass_data.items(), key=lambda x: abs(m_ref-x[1]))
    pressure_sorted = sorted(pressure_data.items(), key=lambda x: abs(p_ref-x[1]))
    umean_sorted = sorted(umean_data.items(), key=lambda x: abs(u_mean_ref-x[1]))
    umax_sorted = sorted(umax_data.items(), key=lambda x: abs(u_max_ref-x[1]))

    write_data(working_dir, "mass", mass_sorted, tol, m_ref)
    write_data(working_dir, "pressure", pressure_sorted, tol, p_ref)
    write_data(working_dir, "velocity_mean", umean_sorted, tol, u_mean_ref)
    write_data(working_dir, "velocity_max", umax_sorted, tol, u_max_ref)
