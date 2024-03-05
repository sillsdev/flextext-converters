from conversion_operations import convert


def function():
    return True


def function2():
    return False


def throw_function():
    raise ValueError()


def main():
    print("<<< Toolbox to  Converter >>>")

    answer = input("Would you like to use a custom marker file? Y/N")
    marker_filename = ""
    if answer.upper() == "Y":
        marker_filename = input("Please input the marker filename.")
    else:
        marker_filename = "TODO: default_filename"


    toolbox_filename = input("Enter the name of the Toolbox file to convert: ")
    fieldworks_filename = input("Enter the name of the FieldWorks file to create: ")

    markers = ""
    toolbox_data = ""
    converted_data = convert(markers, toolbox_data)

    for line in converted_data:
        print(line)

    print("<<< Converter Termination >>>")


if __name__ == "__main__":
    main()
