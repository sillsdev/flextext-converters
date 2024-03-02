import pytest

from toolbox.toolbox_converter import function, function2, throw_function


def test_init():
    assert function() is True


def test_init2():
    assert function2() is False


def test_init3():
    with pytest.raises(ValueError):
        throw_function()
