# Output the converted list (any string list) to the file path described
def output_flextext(file_path, converted_string):
    try:
        with open(file_path, "w") as flextext_file:
            flextext_file.write(converted_string)

    except FileNotFoundError:
        raise

    except PermissionError:
        raise
