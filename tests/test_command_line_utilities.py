"""Test Setting Specific Command Line Arguments"""
# pylint: disable=no-self-use
# pylint: disable=too-few-public-methods

import argparse # pylint: disable=unused-import
import configparser # pylint: disable=unused-import
import pytest

from sample_module import command_line_utilities


class TestSettingCLIValues():
    """Tests related to setting cli arguments"""

    def test_setting_value_x(self, mocker):
        """Test with CLI Argument 'x'"""

        #Setup
        mock_argument_parser = mocker.patch('argparse.ArgumentParser.parse_args')
        mock_argument_parser.return_value.required_option = "X"

        #Test
        output = command_line_utilities.run_function_with_args()

        #Verify
        mock_argument_parser.assert_called_once()
        assert output == "X was selected"

    def test_setting_value_y(self, mocker):
        """Test with CLI Argument 'Y'"""

        #Setup
        mock_argument_parser = mocker.patch('argparse.ArgumentParser.parse_args')
        mock_argument_parser.return_value.required_option = "Y"

        #Test
        output = command_line_utilities.run_function_with_args()

        #Verify
        mock_argument_parser.assert_called_once()
        assert output == "Y was selected"

    def test_value_value_not_set(self, mocker):
        """Test with No valid CLI"""

        #Setup
        mock_argument_parser = mocker.patch('argparse.ArgumentParser.parse_args')
        mock_argument_parser.return_value.required_option = "Invalid Option"

        with pytest.raises(ValueError) as ex:
            command_line_utilities.run_function_with_args()

        #Verify
        assert str(ex.value) == "No Valid CLI Argument was selected"


class TestSettingConfigValues():
    """Tests related to setting cli arguments"""

    def test_setting_value_1(self, mocker):
        """Test Config with value1"""

        #Test
        mock_config_parser = mocker.patch('configparser.ConfigParser.get',
                                          return_value="value1")

        output = command_line_utilities.run_function_with_config()

        #Verify
        mock_config_parser.assert_called_with("DEFAULT", "Key1")
        assert output == "Do Value 1 Thing"

    def test_setting_other_value(self, mocker):
        """Test with Config with Argument 'OtherVlaue'"""

        #Test
        mock_config_parser = mocker.patch('configparser.ConfigParser.get',
                                          return_value="OtherValue")

        output = command_line_utilities.run_function_with_config()

        #Verify
        mock_config_parser.assert_called_with("DEFAULT", "Key1")
        assert output == "Do Other Value thing"

    def test_value_value_not_set(self, mocker):
        """Test with Config with no value set"""

        #Test
        mocker.patch('configparser.ConfigParser.get',
                     return_value="SomeBadKey")

        #Verify
        with pytest.raises(ValueError) as ex:
            command_line_utilities.run_function_with_config()

        assert str(ex.value) == "No Valid Config Key Found"
