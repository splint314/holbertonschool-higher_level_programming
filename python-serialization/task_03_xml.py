#!/usr/bin/env python3

"""Module to convert XML data to JSON format."""
import json
import xml.etree.ElementTree as ET


def convert_xml_to_json(xml_file):
    """
    Reads an XML file and converts its content into a JSON file.

    Args:
        xml_file (str): The name of the source XML file.
    """
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        data = []
        for child in root:
            item = {elem.tag: elem.text for elem in child}
            data.append(item)

        with open("data.json", mode='w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

    except FileNotFoundError:
        print(f"Error: The file {xml_file} was not found.")
    except ET.ParseError:
        print(f"Error: The file {xml_file} is not a valid XML file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
