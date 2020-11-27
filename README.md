# Python Pytest Examples

This repository contains example use cases for various tasks that can be covered with pytest

## Installation

* Fork or Clone this repo
* Make a python virtual environment at .pyenv -> `make init`
* Source the python virtual environment `source .pyenv/bin/activate`
* Install requirements `make pipreq` 


## Test
### Run All Tests
To run all tests execute `make test`

### Coverage Report
To run all tests execute `make coverage`

## Use Cases Covered

### Types of Tests
+ Mocking API Calls
  - [Tests](tests/test_api_utilities.py)
+ Mocking Different Command Line Parameters
  - [Tests Command Line](tests/test_command_line_utilities.py)
  - [Tests Config](tests/test_command_line_utilities.py)
+ Mocking Environment Variables
  - [Tests](tests/test_command_line_utilities.py)
+ Filesystem Interaction
  - [Tests](tests/test_file_system_utilities.py)
+ Testing Exceptions
  - [Tests](tests/test_exceptions.py)
+ Spying vs. Mocking
  - [Tests](tests/test_spy_utilities.py)
+ Parameterization (Running the same test with different inputs)
  - [Tests](tests/test_parametrize.py)

## References

These YouTube Videos were super helpful for understanding pytest
+ Pytest 101: [Youtube Link](https://www.youtube.com/watch?v=etosV2IWBF0)
+ Pytest 201: [Youtube Link](https://www.youtube.com/watch?v=fv259R38gqc&app=desktop)
   - Organizing tests within a test file: [Section](https://www.youtube.com/watch?v=fv259R38gqc&t=20m0s)
   - Test for exceptions: [Section](https://www.youtube.com/watch?v=fv259R38gqc&t=7m10s)
   - Running same test with multiple parameters (Parameterize) [Section](https://www.youtube.com/watch?v=fv259R38gqc&t=13m05s)
   - Fixtures (Data Setting up Reusable Code) [Section](https://www.youtube.com/watch?v=fv259R38gqc&t=24m10s)
   - Built-In Fixture: Capture STDIN STDOUT [Section](https://www.youtube.com/watch?v=fv259R38gqc&t=29m36s )
   - Built-In Fixture: MockFunction (Monkeypatch) [Section](https://www.youtube.com/watch?v=fv259R38gqc&t=35m47s)
   - Built-In Fixture: Temp Files (Secure OS read & write of files that go away after test) [Section](https://www.youtube.com/watch?v=fv259R38gqc&t=39m27s)