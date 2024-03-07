import os

from conversion_operations import convert
from marker_operations import read_markers
from output_operations import output_flextext
from toolbox_operations import toolbox_data_parser, toolbox_file_reader


def make_json_filename(toolbox_filename):
    name_list = toolbox_filename.split(".")
    return f"{name_list[:-1]}.json"


def main():
    print("<<< Toolbox to  Converter >>>")

    using_defined_json = False

    # marker filename
    answer = input("Would you like to use a custom marker file? Y/N")
    if answer.upper() == "Y":
        custom_answer = input(
            "Is there a previously defined marker file you want to use? Y/N"
        )

        if custom_answer.upper() == "Y":
            json_marker_filename = input(
                "Input name of previously defined marker JSON file."
            )

            while not os.path.isfile(json_marker_filename):
                json_marker_filename = input(
                    "Error; invalid file. Input name of previously defined marker JSON file."
                )
            using_defined_json = True
        else:
            marker_filename = input("Input name of marker file.")

            while not os.path.isfile(marker_filename):
                marker_filename = input(
                    "Error; invalid file. Input name of marker file: "
                )

            json_marker_filename = make_json_filename(marker_filename)
    else:
        marker_filename = "standard_markers.typ"
        json_marker_filename = make_json_filename(marker_filename)

    # toolbox filename
    toolbox_filename = input("Input name of Toolbox file to convert: ")
    while not os.path.isfile(toolbox_filename):
        toolbox_filename = input(
            "Error; invalid file. Input name of Toolbox file to convert: "
        )

    fieldworks_filename = input("Input name of FieldWorks file to create: ")

    if not using_defined_json:
        # get raw markers
        markers = read_markers(marker_filename)

        # ask user about markers
        defined_markers = markers  # TODO call define_markers(markers)

        # output json markers
        # TODO json_marker_filename

    # input json markers
    json_markers = markers  # TODO json_marker_filename

    # get toolbox data
    toolbox_data = toolbox_data_parser(toolbox_file_reader(toolbox_filename))

    # convert data
    converted_data = convert(json_markers, toolbox_data)

    for line in converted_data:
        print(line)

    # output the converted data
    output_flextext(fieldworks_filename, converted_data)

    print("<<< Converter Termination >>>")


if __name__ == "__main__":
    main()
