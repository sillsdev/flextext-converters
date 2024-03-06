from toolbox.flextext_operations import (
    make_f_line,
    make_flextext_tagline,
    make_g_line,
    make_u_line,
)

one_modifier = {"guid": "e3cb6669-59c6-4af4-9c1d-0903bbb742ea"}
two_modifiers = {"type": "title", "lang": "ext"}

tagline_plain = "<paragraphs>"
tagline_one_modifier = '<paragraph guid="e3cb6669-59c6-4af4-9c1d-0903bbb742ea">'
tagline_two_modifiers = '<item type="title" lang="ext">'
tagline_ending = "<\\paragraphs>"
u_line = '<item type="txt">This has a translation.</item>'
u_mod_line = '<item type="txt" lang="ext">This has a translation.</item>'

example_marker = {"\\nam ": "test", "\\lng ": "en"}


def test_tagline_plain():
    assert make_flextext_tagline("paragraphs", None) == tagline_plain


def test_tagline_one_modifier():
    assert make_flextext_tagline("paragraph", one_modifier) == tagline_one_modifier


def test_tagline_two_modifiers():
    assert make_flextext_tagline("item", two_modifiers) == tagline_two_modifiers


def test_tagline_ending():
    assert make_flextext_tagline("\\paragraphs", None) == tagline_ending


def test_f_line():
    assert make_f_line({}, "This has a translation.") == u_line


def test_f_mod_line():
    assert (
        make_f_line({"type": "txt", "lng": "ext"}, "This has a translation.")
        == u_mod_line
    )


def test_g_line():
    assert make_g_line({}, "This has a translation.") == u_line


def test_g_mod_line():
    assert (
        make_g_line({"type": "txt", "lng": "ext"}, "This has a translation.")
        == u_mod_line
    )


def test_u_line():
    assert make_u_line({}, "This has a translation.") == u_line


def test_u_mod_line():
    assert (
        make_u_line({"type": "txt", "lng": "ext"}, "This has a translation.")
        == u_mod_line
    )
