import manage_priviliges
import pytest

def compose_error_message(environment):
    error_message = "\nLacking priviliges: " + str(manage_priviliges.get_missing_priviliges(environment))
    return error_message


def test_lacking_priviliges(environment):
    assert len(manage_priviliges.get_missing_priviliges(environment)) == 0, compose_error_message(environment)