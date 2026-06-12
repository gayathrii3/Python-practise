import csv

file_path = "File Handling\Write files\student_details.json"

try:

    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)
        print(f"{file_path} exists!")

except FileExistsError:
    print("File doen't exists!")
except PermissionError:
    print("No permission to access the file!")
except IndexError:
    print("Index out of range")