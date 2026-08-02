"""
Python Reading Files (text files), (csv files), (json files)

"""

import csv

file_path = "/Users/sss/Desktop/sample.csv"

try:
    with open(file_path, 'r') as file:         #I'm using 'r' mode to read the file. If the file doesn't exist, it will raise a FileNotFoundError.
        content = csv.reader(file)
        print(f"Content of the CSV file '{file_path}':")
        for line in content:
            print(line)                # I'm printing each row of the CSV file. Each row is a list of values.
except FileNotFoundError:                      #I'm catching the FileNotFoundError exception to handle the case where the file doesn't exist.
    print(f"File '{file_path}' not found. Please check the file path and try again.")
except PermissionError:                        #I'm catching the PermissionError exception to handle the case where the file cannot be accessed due to permission issues.
    print(f"Permission denied for file '{file_path}'. Please check the file permissions and try again.")