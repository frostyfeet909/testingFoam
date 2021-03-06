# Finds all the good cases and saves them in text files

from dataInterface import get_data, write_data
from os.path import join

"""
VELOCITY_MEAN_REF = 0.49415299
VELOCITY_MAX_REF = 2.2207486
MASS_REF = 0.12907008
PRESSURE_REF = 1114.6359
"""


def find_reference_values():
    # Finds the reference values from the last-line of the reference case
    data = get_data(join("referenceCase", "DataSummary.csv"))[-1]
    umean_ref = float(data[1])
    umax_ref = float(data[2])
    mass_ref = float(data[4])
    pressure_ref = float(data[7])
    return umean_ref, umax_ref, mass_ref, pressure_ref


def main(tol):
    # Find and catalogue the good cases

    data = get_data()
    u_mean_ref, u_max_ref, m_ref, p_ref = find_reference_values()
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

    write_data("mass", mass_sorted, tol, m_ref)
    write_data("pressure", pressure_sorted, tol, p_ref)
    write_data("velocity_mean", umean_sorted, tol, u_mean_ref)
    write_data("velocity_max", umax_sorted, tol, u_max_ref)
