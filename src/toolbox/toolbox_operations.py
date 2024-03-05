"""
    Author: Andrew Quick

    Created: March 4, 2024

    Project: Toolbox to Fieldworks Text Migration (LightSys)

    Description:


    Modification log:
        3-4-24:
            Add toolbox file reader method
            Add toolbox parsing method

"""


def toolbox_file_reader(filename):
    with open(filename, 'r') as f:
        toolbox_data = f.read()

    return toolbox_data

# toolbox_data = "\_sh v3.0  621  Text
#
# \id Freeform
# \ref
# \tx This has a translation.
# \ft It is a freeform translation.
# \nt"


def toolbox_data_parser(toolbox_data):
    m_dict = {}                                     # marker dictionary
    marker = ""
    m_data = ""                                     # marker data
    count = 0
    for i, c in enumerate(toolbox_data):
        if c == '\\':                               # get marker
            if count != 0: m_dict[marker] = m_data  # add item to dictionary
            c2 = ""
            while c2 != ' ':
                c2 = enumerate(toolbox_data)
                marker += c2

            m_data = ""
            count += 1
        else:                                       # get marker data
            m_data += c

    return m_dict
