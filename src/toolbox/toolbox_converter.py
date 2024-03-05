import os

from conversion_operations import convert


def main():
    print("<<< Toolbox to  Converter >>>")

    # marker filename
    answer = input("Would you like to use a custom marker file? Y/N")
    marker_filename = ""
    if answer.upper() == "Y":
        marker_filename = input("Input name of marker file.")

        while not os.path.isfile(marker_filename):
            marker_filename = input("Error; invalid file. Input name of marker file: ")
    else:
        marker_filename = "TODO: default_filename"

    # toolbox filename
    toolbox_filename = input("Input name of Toolbox file to convert: ")
    while not os.path.isfile(toolbox_filename):
        toolbox_filename = input(
            "Error; invalid file. Input name of Toolbox file to convert: "
        )

    # fieldworks_filename = input("Input name of FieldWorks file to create: ")

    markers = ""
    toolbox_data = ""
    converted_data = convert(markers, toolbox_data)

    for line in converted_data:
        print(line)

    print("<<< Converter Termination >>>")


if __name__ == "__main__":
    main()
