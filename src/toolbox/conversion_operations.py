
header = ['<?xml version="1.0" encoding="utf-8"?>', '<document version="2">',
          '  <interlinear-text guid="e763856d-1baa-4f4e-9e2e-1417d56709af">']
trailer = ['  </interlinear-text>', '</document>']


def convert(toolbox_data: {}, markers: {}):
    converted_data = header + trailer

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
                text = ""

            converted_data += text

    converted_data += trailer
    return converted_data
