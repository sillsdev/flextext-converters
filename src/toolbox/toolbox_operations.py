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
        3-7-24:
            Reformat the toolbox parsing method to lists

"""

from typing import List


def toolbox_file_reader(filename):
    with open(filename, "r") as f:
        toolbox_data = f.read()

    return toolbox_data


def toolbox_data_parser(toolbox_data):

    paragraphs = toolbox_data.split(
        "\n\n"
    )  # list of all the paragraphs in toolbox_data
    final_list = []

    for paragraph in paragraphs:
        lines = paragraph.split("\n")  # list of each line in the paragraph
        paragraph_list: List[List[str]] = []
        for line in lines:
            if "\\" != line[0]:  # if line is part of the marker above
                words = line.split()
                paragraph_list[len(paragraph_list) - 1].extend(words)
            else:
                words = line.split()  # list of the words in the line
                paragraph_list.append(words)  # add list of words to paragraph list
        final_list.append(paragraph_list)  # add list of paragraphs to final list

    return final_list
