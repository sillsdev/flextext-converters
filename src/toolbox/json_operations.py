import json


# Take a map and file path, and save map as JSON to that file
def save_map_to_json(marker_map, file_path):
    with open(file_path, "w") as f:
        json.dump(marker_map, f)


# Take a file path, and read a .json file into a map
def load_map_from_json(file_path):
    with open(file_path, "r") as f:
        marker_map: object = json.load(f)
    return marker_map
