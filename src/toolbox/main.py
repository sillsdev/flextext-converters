from conversion_operations import convert
from file_picker_operations import file_picker
from json_operations import load_map_from_json, save_map_to_json
from marker_operations import define_markers, read_markers, compare_maps
from output_operations import output_flextext
from toolbox_operations import toolbox_data_parser, toolbox_file_reader, toolbox_mapping
from popup_operations import *
from tkinter import filedialog


# method to turn a marker filename into a json marker filename
def make_json_filename(marker_filename):
    name_list = marker_filename.split(".")
    name = "".join(name_list[:-1]).split("/")
    return f"json_marker_files/{name[-1]}.json"


def main():
    button_list = ["Browse for Marker File", "Browse for JSON File"]
    key_list = ["M", "J"]

    response = closed_resp("Browse for a Marker File or a previously defined"
                           " JSON File:", button_list, key_list)

    # Check the user's response
    if response == "2":
        filetypes = [("JSON files", "*.json")]

        # Open file picker dialog and allow only .json files
        json_marker_filename = filedialog.askopenfilename(
            title="Select a JSON File", filetypes=filetypes)
        if not json_marker_filename:
            quit()

        marker_map = load_map_from_json(json_marker_filename)
    else:
        filetypes = [("Marker files", "*.typ")]
        marker_filename = filedialog.askopenfilename(
            title="Select a Marker File", filetypes=filetypes)
        if not marker_filename:
            quit()

        # get raw markers
        raw_markers = read_markers(marker_filename)

        # ask user about markers
        defined_markers = define_markers(raw_markers)

        # output json markers
        json_marker_filename = make_json_filename(marker_filename)
        save_map_to_json(defined_markers, json_marker_filename)

    # toolbox files
    filetypes = [("Text files", "*.txt"), ("Toolbox files", "*.sfm")]

    toolbox_filename = filedialog.askopenfilename(
        title="Select a Toolbox File:", filetypes=filetypes)
    if not toolbox_filename:
        quit()

    heading_list = ["Marker", "Count", "Name", "Language"]

    toolbox_map = toolbox_mapping(toolbox_file_reader(toolbox_filename))

    # read in json markers
    json_map = load_map_from_json(json_marker_filename)

    markers = compare_maps(toolbox_map, json_map)

    updated_markers = table(
        "Double Click the name or language box of a marker to "
        "edit it", markers, heading_list)

    usr_input = open_resp("Input name of FieldWorks File to create\n"
                          "(to fieldworks_files Folder)")
    fieldworks_filename = f"fieldworks_files/{usr_input}"

    # get toolbox data
    toolbox_data = toolbox_data_parser(toolbox_file_reader(toolbox_filename))

    # convert data
    converted_xml = convert(toolbox_data, updated_markers)

    # output the converted data
    output_flextext(fieldworks_filename, converted_xml)


if __name__ == "__main__":
    main()
