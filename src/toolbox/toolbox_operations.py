"""
    Author: Andrew Quick

    Created: March 4, 2024

    Project: Toolbox to Fieldworks Text Migration (LightSys)

    File: toolbox_operations.py

    Description:
        File has two methods one for reading a toolbox file and one for parsing the read data

    Modification log:
        3-4-24:
            Add toolbox file reader method
            Add toolbox parsing method
        3-5-24:
            Reformat the toolbox parsing method

"""


def toolbox_file_reader(filename):
    with open(filename, "r") as f:
        toolbox_data = f.read()

    return toolbox_data


def toolbox_data_parser(toolbox_data):
    m_dict = {}  # marker dictionary
    lines = toolbox_data.split("\n")  # list of each line in the toolbox_data
    for line in lines:
        marker, sep, m_data = line.partition(" ")  # get marker and marker data
        m_dict[marker] = m_data  # add item to dictionary

    del m_dict[""]  # dictionary has an extra item, this line deletes it
    return m_dict
