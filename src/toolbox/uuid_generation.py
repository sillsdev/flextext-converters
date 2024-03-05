import uuid


# Return a random UUID as a string
# Optionally test against an array of UUID values for uniqueness
def generate_uuid(string_array):
    # Return a value without checking for uniqueness
    if string_array is None:
        return str(uuid.uuid4())

    # Verify input is a list of strings
    if not isinstance(string_array, list) or not all(
        isinstance(item, str) for item in string_array
    ):
        raise TypeError("Input must be a list of strings")

    temp_uuid = str(uuid.uuid4())

    # Make sure UUID is unique
    while string_array.__contains__(temp_uuid):
        temp_uuid = str(uuid.uuid4())

    return temp_uuid
