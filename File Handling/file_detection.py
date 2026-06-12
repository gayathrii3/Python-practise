# file detection

import os

file_path = "Strings\strings.py"

if os.path.exists(file_path):
    print(f"The location {file_path} exists")

    if os.path.isfile(file_path):
        print("That's a file")
    elif os.path.isdir(file_path):
        print("That's a directory")

else:
    print("The location doesn't exists")

