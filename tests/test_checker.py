"""Checks for the checker"""
import time
import pytest
from icinga_checker import checker


class TestIcingaExit():
    """Test Exit Class"""
    @pytest.mark.parametrize("code,expected",
                             [
                                 ("OK", 0),
                                 ("WARNING", 1),
                                 ("CRITICAL", 2),
                                 ("UNKNOWN", 3),
                             ])
    def test_exit_codes(self, code, expected):
        """Test valid exit codes"""
        this_exit = checker.IcingaExit(code, "Some Description")

        assert this_exit.exit_code == expected

    def test_invalid_exit_code(self):
        """Test an invalid exit code"""
        bad_exit_code = 1
        expected_error_message = f"Value '{bad_exit_code}' not specified for exit code"

        with pytest.raises(ValueError) as err:
            checker.IcingaExit(bad_exit_code, "Some Description")

        assert str(err.value) == expected_error_message

    def test_exit_description(self):
        """Test an invalid exit code"""
        example_description = "This is my description"
        exit_value = "OK"
        expected_description = "OK This is my description"

        returned_description = checker.IcingaExit(exit_value, example_description).description

        assert returned_description == expected_description


class TestTimeouts():
    """Test the checker module"""
    def test_function_timeout(self):
        """Ensure the program exits when a long running script is executed"""
        timeout_before_return = 1
        my_check = checker.Checker(timeout=timeout_before_return)
        long_running_result = None

        with pytest.raises(SystemExit):
            my_check.start_timeout()
            long_running_result = get_two_second_result()
            my_check.stop_timeout()

        assert long_running_result is None

    def test_function_success(self):
        """Ensure the program exits when a long running script is executed"""
        timeout_after_return = 3
        my_check = checker.Checker(timeout=timeout_after_return)

        my_check.start_timeout()
        long_running_result = get_two_second_result()
        my_check.stop_timeout()

        expected = "I've returned"
        assert long_running_result == expected

    def test_function_alarm_off(self):
        """Ensure the program exits when a long running script is executed"""
        timeout_after_return = 3
        my_check = checker.Checker(timeout=timeout_after_return)

        my_check.start_timeout()
        long_running_result = get_two_second_result()
        my_check.stop_timeout()

        ##Add some more time to ensure timeout stopped
        get_two_second_result()
        get_two_second_result()

        expected = "I've returned"
        assert long_running_result == expected

def get_two_second_result():
    """This is a long running function"""
    time.sleep(2)
    return "I've returned"
