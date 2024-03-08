from conversion_operations import convert
from file_picker_operations import file_picker
from json_operations import load_map_from_json, save_map_to_json
from marker_operations import define_markers, read_markers
from output_operations import output_flextext
from toolbox_operations import toolbox_data_parser, toolbox_file_reader


# method to turn a marker filename into a json marker filename
def make_json_filename(marker_filename):
    name_list = marker_filename.split(".")
    name = "".join(name_list[:-1]).split("/")
    return f"json_marker_files/{name[-1]}.json"


def main():
    print("<<< Toolbox to FieldWorks File Converter >>>\n")

    # marker filename
    answer = input(
        "Is there a previously defined JSON marker file you want to use? Y/N: "
    )

    if answer.upper() == "Y":
        print("Select a defined JSON marker file")
        json_marker_filename = file_picker()

        while json_marker_filename == "" or not json_marker_filename.endswith(".json"):
            print("Error; invalid file. Select a defined JSON marker file")
            json_marker_filename = file_picker()
    else:
        print("Select a marker file")
        marker_filename = file_picker()

        while marker_filename == "" or not marker_filename.endswith(".typ"):
            print("Error; invalid file. Select a marker file")
            marker_filename = file_picker()

        # get raw markers
        raw_markers = read_markers(marker_filename)

        # ask user about markers
        defined_markers = define_markers(raw_markers)

        # output json markers
        json_marker_filename = make_json_filename(marker_filename)
        save_map_to_json(defined_markers, json_marker_filename)

    # read in json markers
    json_markers = load_map_from_json(json_marker_filename)

    # toolbox filename
    print("Select a Toolbox file to convert")
    toolbox_filename = file_picker()
    while toolbox_filename == "":
        print("Error; invalid file. Select a Toolbox file to convert")
        toolbox_filename = file_picker()

    # fieldworks filename
    fieldworks_filename = f"fieldworks_files/{input('Input name of FieldWorks file to create (to fieldworks_files folder): ')}"

    # get toolbox data
    toolbox_data = toolbox_data_parser(toolbox_file_reader(toolbox_filename))

    # convert data
    converted_xml = convert(toolbox_data, json_markers)

    # output the converted data
    output_flextext(fieldworks_filename, converted_xml)

    print(f'Converter successful\nFieldWorks file located at: "{fieldworks_filename}"')
    print("\n<<< Converter Termination >>>")


if __name__ == "__main__":
    main()
