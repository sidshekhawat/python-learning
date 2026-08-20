"""Membership operators = used to test whether a value or variable is found in a sequence
                          (string, list, tuple, set, or dictionary)
                          1. in
                          2. not in
"""

word = "APPLE"

letter = input("Guess a letter in a secret word: ")

if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")



students = {"Sid", "Lak", "Dha", "Veer"}

student = input("Enter the name of the student: ")

if student in students:
    print(f"{student} is a student")
else:
    print(f"{student} was not found")


#dictionary

grades = {  "Sid":  "A",
            "Lak":  "B",
            "Dha":  "A",
            "Veer": "B",
            "Yug":  "C"  } 

student = input("Enter the name of the student: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found")