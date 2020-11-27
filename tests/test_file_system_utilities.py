"""Test Various Filesystem Utilities"""
# pylint: disable=no-self-use
import json
import pytest

from sample_module import file_system_utilities

class TestFileSystem():
    """Tests for filesystem interaction"""
    def test_get_object_from_path(self, tmpdir):
        """Gets a json object from a json file"""

        #Setup
        temp_json_file = tmpdir.join('some_json.json')
        temp_json_file.write('{"hello" : "world"}')
        tmp_json_file_path = str(temp_json_file)

        #Test
        ret_obj = file_system_utilities.get_object_from_path(tmp_json_file_path)

        #Verify
        assert ret_obj['hello'] == 'world'

    def test_get_object_from_path_with_invalid(self, tmpdir):
        """Verifies an error from json load"""

        #Setup
        temp_json_file = tmpdir.join('some_json.json')
        temp_json_file.write('{"hello"" : "world"}')
        tmp_json_file_path = str(temp_json_file)

        #Test
        with pytest.raises(json.JSONDecodeError) as ex:
            file_system_utilities.get_object_from_path(tmp_json_file_path)

        #Verify
        assert str(ex.value) == "Expecting ':' delimiter: line 1 column 9 (char 8)"
