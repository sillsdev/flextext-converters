def marker_file_reader(filename):
    with open(filename, "r") as f:
        marker_data = f.read()

    return marker_data


def read_markers(inputfile):
    marker_file_string = marker_file_reader(inputfile)
    marker_file = marker_file_string.split("\n")
    # Holds keys of marker
    map1 = {}
    list_index = 0
    while list_index < len(marker_file):
        line = marker_file[list_index]
        list_index += 1
        split_line = line.split(" ", 1)
        # Marker name
        word = split_line[0]
        if word == "\\+mkr":
            # Holds keys variables of marker
            map2 = {}
            # Marker designation
            markerkey = split_line[1]
            markerkey = "\\" + markerkey
            next_line = marker_file[list_index]
            list_index += 1
            split_next_line = next_line.split(" ", 1)
            word2 = split_next_line[0]
            # Holds variables of the marker
            while word2 != "\\-mkr":
                if word2 == "\\+fnt":
                    # Holds keys used for font
                    map3 = {}
                    next_line = marker_file[list_index]
                    list_index += 1
                    split_next_line = next_line.split(" ", 1)
                    while split_next_line[0] != "\\-fnt":
                        word3 = split_next_line[0]
                        # Font variable designation for marker
                        fontvar = split_next_line[1]
                        map3[word3] = fontvar
                        next_line = marker_file[list_index]
                        list_index += 1
                        split_next_line = next_line.split(" ", 1)
                    next_line = marker_file[list_index]
                    list_index += 1
                    split_next_line = next_line.split(" ", 1)
                    map2["\\fnt"] = map3
                    word2 = split_next_line[0]
                else:
                    # Variable designation for marker
                    variable = split_next_line[1]
                    map2[word2] = variable
                    next_line = marker_file[list_index]
                    list_index += 1
                    split_next_line = next_line.split(" ", 1)
                    word2 = split_next_line[0]
            map1[markerkey] = map2
    return map1


def combine_maps(map1, map2):
    for key in map1.keys():
        if key in map2:
            map1[key].update(map2[key])
    return map1
