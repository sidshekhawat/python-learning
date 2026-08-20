#Python File Detection 

import os

file_path = input("Enter the file path: ")

if os.path.exists(file_path):
    print("File exists.")

    if os.path.isfile(file_path):
        print("It is a file.")

    elif os.path.isdir(file_path):
        print("It is a directory.")
    
else:
    print("File does not exist.")