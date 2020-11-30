"""Module to automate repetative Icinga Check Tasks"""

import signal
import sys

EXIT_HASH = {
    "OK" : 0,
    "WARNING" : 1,
    "CRITICAL" : 2,
    "UNKNOWN" : 3,
}

class IcingaExit():
    """Exits and exit codes"""
    def __init__(self, exit_value, description):
        self.exit_code = self.get_exit_code(exit_value)
        self.exit_value = exit_value
        self.description = self.check_description(description)

    def get_exit_code(self, exit_value):
        """Ensure the exit code exists"""
        if exit_value not in EXIT_HASH:
            raise ValueError(f"Value '{exit_value}' not specified for exit code")

        return EXIT_HASH[exit_value]

    def check_description(self, description):
        """Ensure the description is valid"""
        return f"{self.exit_value} {description}"

class Metric():
    """Class for holding a metric"""
    def __init__(self,
                 metric_name,
                 unit_of_measure,
                 critical_threshold=None,
                 warning_threshold=None,
                 reverse_value=False):
        self.metric_name = metric_name
        self.unit_of_measure = _check_unit_of_measure(unit_of_measure)
        self.warning_threshold = warning_threshold
        self.critical_threshold = critical_threshold
        self.reverse_value = _check_boolean(reverse_value)

    def check_metric(self, value):
        """Check the Metric and get an exit value"""
        if not self.reverse_value:
            return self._check_standard(value)

        return self._check_reverse(value)

    def _check_standard(self, value):
        """Check the standard (higer is worse) running of a metric"""
        pass

    def _check_reverse(self, value):
        """Check the reverse (lower is worse) running of a metric"""
        pass



class Checker():
    """Main helper function for icinga checker"""
    def __init__(self, timeout=10):
        self.max_value = False
        self._timeout = timeout
        self._metrics = {}

    def start_timeout(self):
        """Start a countdown timer that will exit if the end is reached"""
        signal.signal(signal.SIGALRM, self._handle_timeout)
        signal.alarm(self._timeout)

    def stop_timeout(self):
        """Stop the timeout counter"""
        signal.alarm(0)

    def _handle_timeout(self, *args):
        """Hanlde a timeout"""
        icinga_exit = IcingaExit("UNKNOWN", "Check timeout exceeded")
        self.process_exit(icinga_exit)

    def process_exit(self, icinga_exit):
        """Process an Icina Exit"""
        print(icinga_exit.description)
        sys.exit(icinga_exit.exit_code)


def _check_boolean(input_object):
    """Ensure Boolean"""
    if not isinstance(input_object, bool):
        raise ValueError

    return input_object

def _check_unit_of_measure(unit_of_measure):
    """Ensure Valid Unit of Measure"""
    valid_units = set(
        "s", "ms", "us",         #Time
        "kb", "mb", "gb", "tb",  #Storage
        "KB", "MB", "GB", "TB",  #Storage Upper
        "c",                     #Continuous
        None
    )

    if unit_of_measure not in valid_units:
        raise ValueError("Invalid unit of measure")

    return unit_of_measure
