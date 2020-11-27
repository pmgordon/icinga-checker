"""Test Parametrize"""
# pylint: disable=no-self-use
# pylint: disable=too-few-public-methods

import pytest

from sample_module import add_utilities

class TestParametrize():
    """Class for testing Parametrize"""
    @pytest.mark.parametrize("first_number,second_number,expected", [
        (3, 4, 7),
        (100, 101, 201),
        (2, 3, 5),
        (3, 2, 5),
    ])
    def test_add(self, first_number, second_number, expected):
        """Test the addition function"""
        assert add_utilities.add(first_number, second_number) == expected
    