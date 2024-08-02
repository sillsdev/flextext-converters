import os
import stat

import pytest

from toolbox.output_operations import output_flextext

# import tox


simple_sample_string = """This is a simple list of strings
These strings are in simple in nature
These strings are offended by your belittling of them
So you found me. Congratulations. Was it worth it?"""

# Duplicate of a version of Freeform.flextext
complex_sample_string = """<?xml version="1.0" encoding="utf-8"?>
<document version="2">
  <interlinear-text guid="e763856d-1baa-4f4e-9e2e-1417d56709af">
    <item type="title" lang="ext">Freeform</item>
    <paragraphs>
      <paragraph guid="e3cb6669-59c6-4af4-9c1d-0903bbb742ea">
        <phrases>
          <phrase guid="b54f36e5-b75b-4cc2-b9e9-893857d62cfc">
            <item type="txt" lang="ext">This has a translation.</item>
            <item type="segnum" lang="en">1</item>
            <words>
              <word guid="e91a7bd6-a79a-4d2c-9e70-2659fc183065">
                <item type="txt" lang="ext">This</item>
                <morphemes>
                  <morph>
                    <item type="txt" lang="ext">this</item>
                  </morph>
                </morphemes>
                <item type="gls" lang="en">this</item>
              </word>
              <word guid="c9f72821-7fa5-4132-97bb-f461936273de">
                <item type="txt" lang="ext">has</item>
              </word>
              <word guid="535b6edb-9f96-4cde-b430-4501808cb277">
                <item type="txt" lang="ext">a</item>
              </word>
              <word guid="fbf7a9f7-3818-44de-b326-8adcdde10b5e">
                <item type="txt" lang="ext">translation</item>
              </word>
              <word>
                <item type="punct" lang="ext">.</item>
              </word>
            </words>
            <item type="gls" lang="en">It is a freeform translation.</item>
            <item type="lit" lang="en"></item>
          </phrase>
        </phrases>
      </paragraph>
    </paragraphs>
    <languages>
      <language lang="ext" font="Charis SIL" vernacular="true" />
      <language lang="en" font="Times New Roman" />
    </languages>
  </interlinear-text>
</document>"""


# Tests that files are created
def test_file_creation():
    output_path = "./output_test_files/test_file_creation.flextext"
    if "TOX_ENV_NAME" in os.environ:
        output_path = "./tests" + output_path[1:]
    output_flextext(output_path, simple_sample_string)
    assert os.path.isfile(output_path) is True


# Test that output in file matches input with a simple string list
def test_file_contents_simple():
    output_path = "./output_test_files/test_file_contents_simple.flextext"
    if "TOX_ENV_NAME" in os.environ:
        output_path = "./tests" + output_path[1:]
    output_flextext(output_path, simple_sample_string)

    with open(output_path, "r") as file:
        file_contents = file.read()

    assert (file_contents == simple_sample_string) is True


# Test that output in file matches input with a complex & realistic string list
def test_file_contents_complex():
    output_path = "./output_test_files/test_file_contents_complex.flextext"
    if "TOX_ENV_NAME" in os.environ:
        output_path = "./tests" + output_path[1:]
    output_flextext(output_path, complex_sample_string)

    with open(output_path, "r") as file:
        file_contents = file.read()

    assert (file_contents == complex_sample_string) is True


# Test that an exception is thrown when an invalid path is provided
def test_invalid_file_path():
    output_path = "./fake_folder/fake_file.flextext"
    if "TOX_ENV_NAME" in os.environ:
        output_path = "./tests" + output_path[1:]
    with pytest.raises(FileNotFoundError):
        output_flextext(output_path, simple_sample_string)


# Test that an exception is thrown when the file is un-writeable
def test_no_write_perms():
    # Create the file first
    output_path = "./output_test_files/test_no_write_perms.flextext"
    if "TOX_ENV_NAME" in os.environ:
        output_path = "./tests" + output_path[1:]
    with open(output_path, "w") as f:
        f.write("This file shouldn't have been modified.")

    # Change its permissions to be read-only
    os.chmod(output_path, stat.S_IREAD)

    # Now run the function that should raise a PermissionError
    with pytest.raises(PermissionError):
        output_flextext(output_path, simple_sample_string)

    # Change its permissions to allow writing so future tests don't fail
    os.chmod(output_path, stat.S_IWRITE)
