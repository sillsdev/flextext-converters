from conversion_operations import convert
from file_picker_operations import save_file
from json_operations import load_map_from_json, save_map_to_json
from marker_operations import compare_maps
from output_operations import output_flextext
from popup_operations import select_file_window, table
from toolbox_operations import toolbox_data_parser, toolbox_file_reader, toolbox_mapping


# method to turn a marker filename into a json marker filename
def make_json_filename(marker_filename):
    name_list = marker_filename.split(".")
    name = "".join(name_list[:-1]).split("/")
    return f"json_marker_files/{name[-1]}.json"


def main():
    # Get the name of the marker/json (if one is selected) and toolbox file
    marker_filename, toolbox_filename = select_file_window()

    # Create a dictionary holding data like name and language
    toolbox_map = toolbox_mapping(toolbox_file_reader(toolbox_filename))

    # Check if a marker file was selected
    if marker_filename:
        if marker_filename.endswith(".json"):
            json_marker_filename = marker_filename

        else:
            # Convert to a JSON file
            json_marker_filename = make_json_filename(marker_filename)

        # Create JSON dictionary with data
        json_map = load_map_from_json(json_marker_filename)

        # Compare and combine the two dictionaries
        markers = compare_maps(toolbox_map, json_map)
    else:
        markers = toolbox_map
        json_marker_filename = "new_json_markers"

    heading = "Double Click the name or language box of a marker to edit it"
    heading_list = ["Marker", "Count", "Name", "Language"]

    # Create the UI table where the user can update the marker information
    updated_markers = table(heading, markers, heading_list)

    # output json markers
    save_map_to_json(updated_markers, json_marker_filename)

    flextext_filename = save_file("Input Name of Flextext File to Create")
    if not flextext_filename:
        quit()
    if not flextext_filename.endswith(".flextext"):
        flextext_filename += ".flextext"

    # get toolbox data
    toolbox_data = toolbox_data_parser(toolbox_file_reader(toolbox_filename))

    # convert data
    converted_xml = convert(toolbox_data, updated_markers)

    # output the converted data
    output_flextext(flextext_filename, converted_xml)


if __name__ == "__main__":
    main()
