"""Tests For Spying
Spying keeps the functionality the same, but will
add special functions like call count or called with
"""
# pylint: disable=no-self-use
# pylint: disable=too-few-public-methods

import json

from sample_module import spy_utilities

class TestSpyFunctions():
    """Test spy functions"""
    def test_spy_with_called_with(self, mocker):
        """Test spy with called with"""
        #Setup
        sample_json = '{"key1" : "value1", "key2" : "value2"}'
        expected_obj = {
            "key1" : "value1",
            "key2" : "value2",
        }
        spy = mocker.spy(json, "loads")

        #Test
        ret_obj = spy_utilities.load_some_json()

        #Verify (Function remains you can make sure it was called with a value)
        spy.assert_called_with(sample_json)
        assert ret_obj == expected_obj
