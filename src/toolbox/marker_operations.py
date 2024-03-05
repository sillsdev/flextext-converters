def read_markers(file):
    markerfile = open(file)
    # Holds keys of marker
    map1 = {}
    map2 = {}
    map3 = {}
    while markerfile != "":
        line = markerfile.readline()
        for word in line:
            split_line = line.split(word, 1)
            if word == "\+mkr":
                # Marker designation
                markerkey = split_line[2]
                next_line = markerfile.readline()
                split_next_line = next_line.split(word, 1)
                # Holds variables of the marker
                while word != "\-mkr":
                    # Variable designation for marker
                    variable = split_line[2]
                    if word == "\+fnt":
                        while word != "\-fnt":
                            next_line = markerfile.readline()
                            split_next_line = next_line.split(word, 1)
                            # Font variable designation for marker
                            fontvar = split_line[2]
                            map3["fnt"] = fontvar
                        map2[word] = map3
                    map2[word] = variable
                map1[markerkey] = map2
    return map1

# def define_markers(map):
