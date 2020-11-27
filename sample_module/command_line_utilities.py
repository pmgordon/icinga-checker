"""Test utility to show how command line
arguments can be tested"""
from sample_module import arguments
from sample_module import configs

def run_function_with_args():
    """Run a function with args"""

    args = arguments.parse_args()
    if args.required_option == "X":
        return "X was selected"

    if args.required_option == "Y":
        return "Y was selected"

    raise ValueError("No Valid CLI Argument was selected")

def run_function_with_config():
    """Runs a function with configuration"""
    config = configs.parse_config()

    if config.get("DEFAULT", "Key1") == "value1":
        return "Do Value 1 Thing"
    
    if config.get("DEFAULT", "Key1") == "OtherValue":
        return "Do Other Value thing"
    
    raise ValueError("No Valid Config Key Found")
