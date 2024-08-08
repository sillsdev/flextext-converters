import json
import os


# Take a map and file path, and save map as JSON to that file
def save_map_to_json(marker_map, file_path):
    field_path = find_folder("fieldworks_files")
    base_name = os.path.basename(file_path)
    field_path = field_path + "/" + base_name
    if not field_path.endswith(".json"):
        field_path += ".json"
    with open(field_path, "w") as f:
        json.dump(marker_map, f)


# Take a file path, and read a .json file into a map
def load_map_from_json(file_path):
    with open(file_path, "r") as f:
        marker_map: object = json.load(f)
    return marker_map


def find_folder(folder):
    for base, directories, files in os.walk(os.getcwd()):
        if folder in directories:
            return os.path.join(base, folder)
    return None
