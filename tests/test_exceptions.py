"""Test Various API Utilities"""
# pylint: disable=no-self-use

import pytest

from sample_module import api_utilities

class TestCatchingExceptions():
    """Tests Catching Various Exceptions"""
    def test_catch_exception(self):
        """Tests Catching an Exceptions"""

        with pytest.raises(Exception):
            api_utilities.git_clone_repo()

    def test_catch_exception_with_message(self):
        """Tests Catching an Exceptions"""

        with pytest.raises(Exception) as ex:
            api_utilities.git_clone_repo()

        assert str(ex.value) == 'GIT_USERNAME is not set'
