#!/usr/bin/env python3
"""Module to convert CSV data to JSON format."""
import csv
import json


def convert_csv_to_json(csv_file):
    """
    Reads a CSV file and converts its content into a JSON file.

    Args:
        csv_file (str): The name of the source CSV file.

    Returns:
        bool: True if the conversion was successful, False otherwise.
    """
    try:
        # Lecture du fichier CSV
        with open(csv_file, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            # Conversion de l'itérateur en liste de dictionnaires
            data = [row for row in reader]

        # Écriture du fichier JSON
        with open("data.json", mode='w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

        return True

    except FileNotFoundError:
        print(f"Error: The file {csv_file} was not found.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False
