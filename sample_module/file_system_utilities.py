"""Functions that interact with a file on the filesystem"""
import json

def get_object_from_path(file_path):
    """Return a python object from json file"""
    with open(file_path, "r") as file_contents:
        return json.load(file_contents)
