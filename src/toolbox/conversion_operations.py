from flextext_operations import (
    make_f_line,
    make_flextext_tagline,
    make_g_line,
    make_u_line,
)
from uuid_generation import generate_uuid


def convert(toolbox_data, markers):

    # make header
    header = [
        make_flextext_tagline("?xml", {"version": "1.0", "encoding": '"utf-8"?'}),
        make_flextext_tagline("interlinear-text", {"guid": f"{generate_uuid(None)}"}),
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
                text = make_f_line(markers[td_key], toolbox_data[td_key])
            elif text_type == "G":
                text = make_g_line(markers[td_key], toolbox_data[td_key])
            elif text_type == "U":
                text = make_u_line(markers[td_key], toolbox_data[td_key])

            converted_data += text

    converted_data += trailer

    print(converted_data)
    return converted_data
