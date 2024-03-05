# Output the converted list (any string list) to the file path described
def output_flextext(file_path, converted_list):
    try:
        with open(file_path, "w") as flextext_file:
            flextext_file.write("\n".join(converted_list))

    except FileNotFoundError:
        raise

    except PermissionError:
        raise
