#!/usr/bin/env python3

"""Basic serialization"""

import json


def to_json_string(my_obj):

    """Returns the JSON representation of an object (string)"""
    return json.dumps(my_obj)

    if __name__ == "__main__":
        my_obj = [1, 2, 3, 4]
    json_string = to_json_string(my_obj)
    print(json_string)
