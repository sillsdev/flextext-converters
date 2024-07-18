import uuid

import pytest

from src.toolbox.uuid_generation import generate_uuid


# Helper method to test if a UUID is valid
def is_valid_uuid(uuid_to_test):
    try:
        uuid.UUID(str(uuid_to_test))
    except ValueError:
        return False
    return True


# Tests with no input strings
def test_return_unchecked_uuid():
    assert is_valid_uuid(generate_uuid(None)) is True


# Tests with an invalid data type
def test_return_checked_uuid_invalid_input():
    with pytest.raises(TypeError):
        generate_uuid("Invalid input")


# Tests against an array of sample data types
def test_return_checked_uuid():
    sample_uuids = [
        "68b86e89-2435-5275-b08a-0030cc8ca544",
        "29d9a549-145f-5c94-972b-327363f7a888",
        "a823ec87-885f-5c8b-8641-0b4a12cc97e8",
        "45480f65-ac9b-5e2c-94e1-b1581ce33163",
        "09f0f41a-2230-5094-9b1c-f6c397a12a73",
        "8bd1bf5b-156b-5cd5-944b-007f275fcaf1",
        "a92efbab-1e2e-5b31-8125-4e34ff15b914",
        "22ecbb71-62be-5bdc-a14f-983a430f37ca",
    ]

    assert is_valid_uuid(generate_uuid(sample_uuids)) is True
