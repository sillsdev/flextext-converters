from flextext_operations import make_flextext_tagline, make_tx_line


def convert(toolbox_data, markers):

    # make header
    header = [
        make_flextext_tagline("?xml", {"version": "1.0", "encoding": '"utf-8"?'}),
        make_flextext_tagline("interlinear-text", {"guid": "TODO:QUID"}),
    ]

    # make trailer
    trailer = [
        make_flextext_tagline("/interlinear-text", None),
        make_flextext_tagline("/document", None),
    ]

    converted_data = header

    marker_keys = markers.keys()
    for td_key in toolbox_data.keys():

        if td_key == "id":
            if marker_keys.__contains__(td_key):
                pass

        if marker_keys.__contains__(td_key):
            text_type = markers[td_key]["text_type"]

            text = ""
            if text_type == "F":
                text = ""
            elif text_type == "G":
                text = ""
            elif text_type == "U":
                text = make_tx_line(markers[td_key], toolbox_data[td_key])

            converted_data += text

    converted_data += trailer

    print(converted_data)
    return converted_data
