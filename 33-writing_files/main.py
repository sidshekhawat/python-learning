# Python Writing Files (text files), (csv files), (json files)


#txt_data = "This is a sample text file.\nIt contains multiple lines of text.\nThis is the third line."

employees = [["Name","Age", "Job"],
             ["Spongebob",30, "Cook"],
             ["Patrick", 37, "Unemployed"],
             ["Sandy", 27, "Scientist"], 
             ["Squidward", 35, "Cashier"]]

file_path = "/Users/sss/Desktop/sample.csv"

with open(file_path, 'w') as file:         #I'm using 'w' mode to write to the file. If the file already exists, it will be overwritten.
    for row in employees:
        file.write('\t'.join(map(str, row)) + '\n')
    print(f"CSV file '{file_path}' has been created and written to.")

try:
    with open(file_path, 'x') as file:     #I'm using 'x' mode to create a new file. If the file already exists, it will raise a FileExistsError.
        for row in employees:
            file.write('\t'.join(map(str, row)) + '\n')
        print(f"CSV file '{file_path}' has been created and written to.")

except FileExistsError:#I'm catching the FileExistsError exception to handle the case where the file already exists.
    print(f"File '{file_path}' already exists. Please choose a different file name or path.")

with open(file_path, 'a') as file:         #I'm using 'a' mode to append to the file. If the file doesn't exist, it will be created.
    file.write("\nThis line is appended to the file.")
    print(f"CSV file '{file_path}' has been appended to.")
    