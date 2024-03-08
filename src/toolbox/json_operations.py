import json


def save_map_to_json(marker_map, name):
    filename = f"./src/toolbox/json_marker_files/{name}.json"
    with open(filename, "w") as f:
        json.dump(marker_map, f)


def load_map_from_json(name):
    filename = f"./src/toolbox/json_marker_files/{name}.json"
    with open(filename, "r") as f:
        marker_map: object = json.load(f)
    return marker_map