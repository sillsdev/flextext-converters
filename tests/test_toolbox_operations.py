"""
    Author: Andrew Quick

    Created: March 4, 2024

    Project: Toolbox to FieldWorks Text Migration (LightSys)

    Description:
        testing file for toolbox operations
"""

from unittest import TestCase

from src.toolbox.toolbox_operations import toolbox_data_parser, toolbox_file_reader


def test_toolbox_file_reader():
    toolbox_test_data = (
        "\\_sh v3.0  621  Text\n\n\\id toolbox_test\n\\ref\n"
        "\\tx This has a translation.\n"
        "\\ft It is a freeform translation.\n\\nt"
    )
    # file = "tests/example_test_files/toolbox_test.sfm"
    file = "example_test_files/toolbox_test.sfm"
    assert toolbox_file_reader(file) == toolbox_test_data


def test_toolbox_file_reader1():
    toolbox_test_data = (
        "\\_sh v3.0  213  Text\n\n\\id toolbox_test1\n\\ref\n"
        "\\tx This is some test data\n\\ge this is some test data\n"
        "\n\\ft\n\\nt"
    )
    # file = "tests/example_test_files/toolbox_test1.sfm"
    file = "example_test_files/toolbox_test1.sfm"
    assert toolbox_file_reader(file) == toolbox_test_data


def test_toolbox_file_reader2():
    toolbox_test_data = (
        "\\_sh v3.0  543  Text\n\n\\id toolbox_test2\n\\ref\n"
        "\\tx Awesome method is doing its job\n"
        "\\ft Super cool method is working.\n"
        "\n\\tx keep up the good work.\n"
        "\\mg doing great\n"
        "\n\\tx this\nis a\ncool\nmessage\n"
        "\\mg nice, what about the other things\n"
        "\n\\nt"
    )
    # file = "tests/example_test_files/toolbox_test2.sfm"
    file = "example_test_files/toolbox_test2.sfm"
    assert toolbox_file_reader(file) == toolbox_test_data


def test_toolbox_data_parser():
    toolbox_test_data = (
        "\\_sh v3.0  621  Text\n\n\\id toolbox_test\n\\ref\n"
        "\\tx This has a translation.\n"
        "\\ft It is a freeform translation.\n\\nt"
    )
    toolbox_test_data_list = [
        [["\\_sh", "v3.0", "621", "Text"]],
        [
            ["\\id", "toolbox_test"],
            ["\\ref"],
            ["\\tx", "This", "has", "a", "translation", "."],
            ["\\ft", "It", "is", "a", "freeform", "translation", "."],
            ["\\nt"],
        ],
    ]
    print("\nMethod List:\n", toolbox_data_parser(toolbox_test_data))
    print("\nTest List:\n", toolbox_test_data_list)
    TestCase().assertTrue(
        toolbox_data_parser(toolbox_test_data) == toolbox_test_data_list
    )


def test_toolbox_data_parser1():
    toolbox_test_data = (
        "\\_sh v3.0  213  Text\n\n\\id toolbox_test1\n\\ref\n"
        "\\tx This is some test data\n\\ge this is some test data\n"
        "\n\\ft\n\\nt"
    )
    toolbox_test_data_list = [
        [["\\_sh", "v3.0", "213", "Text"]],
        [
            ["\\id", "toolbox_test1"],
            ["\\ref"],
            ["\\tx", "This", "is", "some", "test", "data"],
            ["\\ge", "this", "is", "some", "test", "data"],
        ],
        [["\\ft"], ["\\nt"]],
    ]
    print("\nMethod List:\n", toolbox_data_parser(toolbox_test_data))
    print("\nTest List:\n", toolbox_test_data_list)
    TestCase().assertTrue(
        toolbox_data_parser(toolbox_test_data) == toolbox_test_data_list
    )


def test_toolbox_data_parser2():
    toolbox_test_data = (
        "\\_sh v3.0  543  Text\n\n\\id toolbox_test2\n\\ref\n"
        "\\tx Awesome method is doing its job\n"
        "\\ft Super cool method is working.\n"
        "\n\\tx keep up the good work.\n"
        "\\mg doing great\n"
        "\n\\tx this\nis a\ncool\nmessage\n"
        "\\mg nice, what about the other things\n"
        "\n\\nt"
    )
    toolbox_test_data_list = [
        [["\\_sh", "v3.0", "543", "Text"]],
        [
            ["\\id", "toolbox_test2"],
            ["\\ref"],
            ["\\tx", "Awesome", "method", "is", "doing", "its", "job"],
            ["\\ft", "Super", "cool", "method", "is", "working", "."],
        ],
        [
            ["\\tx", "keep", "up", "the", "good", "work", "."],
            ["\\mg", "doing", "great"],
        ],
        [
            ["\\tx", "this", "is", "a", "cool", "message"],
            ["\\mg", "nice", ",", "what", "about", "the", "other", "things"],
        ],
        [["\\nt"]],
    ]
    print("\nMethod List:\n", toolbox_data_parser(toolbox_test_data))
    print("\nTest List:\n", toolbox_test_data_list)
    TestCase().assertTrue(
        toolbox_data_parser(toolbox_test_data) == toolbox_test_data_list
    )
