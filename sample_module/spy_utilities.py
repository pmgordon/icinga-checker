"""Functions that can be spyed upon"""
import json


def load_some_json():
    """Load up some json"""
    sample_json = '{"key1" : "value1", "key2" : "value2"}'

    python_obj = json.loads(sample_json)
    return python_obj
