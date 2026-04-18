#!/usr/bin/env python3
import csv
import json


def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)

        with open('data.json', 'w', newline='') as jsonfile:
            json.dump(data, jsonfile, indent=4)

        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
