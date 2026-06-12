# load the details from a existing file

import json

file_path = "File Handling/Write files/student_details.json"

try:
    with open(file_path, "r" ) as file:
        read = json.load(file)
        print(f"json file {file_path} exists!")
        print(read["Grade"])

except FileExistsError:
    print("file doesn't exists!")
