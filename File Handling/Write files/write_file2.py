employee = ["Gayathri", "Keerthi", "Honey", "Anila"]

file_path = "employee_data.txt"

try:
    with open(file_path, "w") as file:
        for index, employ in enumerate(employee, start=1):  #gives indices
            file.write(f"{index}. {employ}\n")
        print(f"The file {file_path} is created successfully!")

except FileExistsError:
    print("File already exists!")
    
