import os

from toolbox.json_operations import load_map_from_json, save_map_to_json

# Duplicated from test_marker_operations
# test_map1
sub_test_map1 = {"\\nam": "*", "\\lng": "Default", "\\mkrOverThis": "name"}
test_map1 = {"\\dt": sub_test_map1}

# test_map2
font_sub_test_map2 = {
    "\\Name": "Times New Roman",
    "\\Size": "10",
    "\\charset": "00",
    "\\rgbColor": "128,128,128",
}
sub_test_map2 = {
    "\\nam": "Reference Number",
    "\\lng": "Default",
    "\\fnt": font_sub_test_map2,
    "\\mkrOverThis": "name",
}
test_map2 = {"\\ref": sub_test_map2}


# Test that the file is actually created
def test_json_creation():
    output_path = "./output_test_files/test_json_creation.json"
    if "TOX_ENV_NAME" in os.environ:
        output_path = "./tests" + output_path[1:]
    save_map_to_json(test_map1, output_path)
    assert os.path.isfile(output_path) is True


# Test creating a .json from a simple map
def test_json_contents_simple():
    output_path = "./output_test_files/test_json_contents_simple.json"
    if "TOX_ENV_NAME" in os.environ:
        output_path = "./tests" + output_path[1:]
    save_map_to_json(test_map1, output_path)
    assert (test_map1 == load_map_from_json(output_path)) is True


# Test creating a .json from a more complex map
def test_json_contents_complex():
    output_path = "./output_test_files/test_json_contents_complex.json"
    if "TOX_ENV_NAME" in os.environ:
        output_path = "./tests" + output_path[1:]
    save_map_to_json(test_map2, output_path)
    assert (test_map2 == load_map_from_json(output_path)) is True
