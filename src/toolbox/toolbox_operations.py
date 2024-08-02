"""
    Author: Andrew Quick

    Created: March 4, 2024

    Project: Toolbox to FieldWorks Text Migration (LightSys)

    File: toolbox_operations.py

    Description:
        File has three methods one for reading a toolbox file and one for parsing the read data,
        and a helper method for separating the punctuation from words

    Modification log:
        3-4-24:
            Add toolbox file reader method
            Add toolbox parsing method
        3-5-24:
            Reformat the toolbox parsing method
        3-7-24:
            Reformat the toolbox parsing method to lists
        3-8-24:
            Add punctuation parsing method

"""

import unicodedata
from typing import Any, Dict, List


def toolbox_file_reader(filename):  # read in toolbox file
    with open(filename, "r", encoding="iso8859_5") as f:
        toolbox_data = f.read()

    return toolbox_data


def toolbox_mapping(toolbox_data):
    map1: Dict[str, Dict[str, Any]] = {}
    lines = toolbox_data.split("\n")
    for line in lines:
        if line == "":
            continue
        if "\\" == line[0]:
            mkr = line.split()[0]
            if mkr in map1.keys():
                map1[mkr]["Count"] = map1[mkr]["Count"] + 1
            else:
                map1[mkr] = {}
                map1[mkr]["\\lng"] = ""
                map1[mkr]["\\nam"] = ""
                map1[mkr]["Count"] = 1
    return map1


def toolbox_data_parser(toolbox_data):
    # list of all the paragraphs in toolbox_data
    paragraphs = toolbox_data.split("\n\n")
    final_list = []

    for paragraph in paragraphs:
        lines = paragraph.split("\n")  # list of each line in the paragraph
        paragraph_list: List[List[str]] = []
        for line in lines:
            if line == "":  # if line is empty
                continue
            if "\\" != line[0]:  # if line is part of the marker above
                words = line.split()
                words = punctuation_parser(words)
                paragraph_list[len(paragraph_list) - 1].extend(words)
            else:
                words = line.split()  # list of the words in the line
                mkr = words[0]  # save marker
                words = punctuation_parser(
                    words[1:]
                )  # parse the rest of the list for punctuation
                words.insert(0, mkr)  # add marker back to the beginning
                paragraph_list.append(words)  # add list of words to paragraph list
        final_list.append(paragraph_list)  # add list of paragraphs to final list

    return final_list


def punctuation_parser(
    w_list,
):  # separate punctuation from words, and make it its own "word"
    parsed_line = []

    for word in w_list:
        # check if the last character in punctuation using Unicode category
        if unicodedata.category(word[-1])[0] == "P":
            parsed_line.append(word[:-1])  # Append word without punctuation
            parsed_line.append(word[-1])  # Append the punctuation as a separate "word"
        else:
            parsed_line.append(word)  # Append the word as is

    return parsed_line
