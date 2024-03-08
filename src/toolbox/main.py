import os

from conversion_operations import convert
from json_operations import load_map_from_json, save_map_to_json
from marker_operations import define_markers, read_markers
from output_operations import output_flextext
from toolbox_operations import toolbox_data_parser, toolbox_file_reader


def make_json_filename(toolbox_filename):
    name_list = toolbox_filename.split(".")
    name = "".join(name_list[:-1]).split("/")
    return f"{name[-1]}.json"


def main():
    print("<<< Toolbox to Converter >>>")

    # marker filename
    answer = input(
        "Is there a previously defined JSON marker file you want to use? Y/N: "
    )

    if answer.upper() == "Y":
        json_marker_filename = (
            f"json_marker_files/"
            f"{input('Input name of defined JSON marker file (in json_marker_files folder): ')}"
        )

        while not os.path.isfile(
            "json_marker_files/" + json_marker_filename
        ) or not json_marker_filename.endswith(".json"):
            json_marker_filename = input(
                "Error; invalid file. Input name of defined JSON marker file: "
            )
    else:
        marker_filename = f"marker_files/{input('Input name of marker file (in marker_files folder): ')}"

        while not os.path.isfile(marker_filename) or not marker_filename.endswith(
            ".typ"
        ):
            marker_filename = input("Error; invalid file. Input name of marker file: ")

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
    toolbox_filename = f"toolbox_files/{input('Input name of Toolbox file to convert (in toolbox_files folder): ')}"
    while not os.path.isfile(toolbox_filename):
        toolbox_filename = input(
            "Error; invalid file. Input name of Toolbox file to convert: "
        )

    fieldworks_filename = f"fieldworks_files/{input('Input name of FieldWorks file to create (to fieldworks_files folder): ')}"

    # get toolbox data
    toolbox_data = toolbox_data_parser(toolbox_file_reader(toolbox_filename))

    # convert data
    converted_xml = convert(toolbox_data, json_markers)

    # print(converted_xml)

    # output the converted data
    output_flextext(fieldworks_filename, converted_xml)

    print("<<< Converter Termination >>>")


if __name__ == "__main__":
    main()
