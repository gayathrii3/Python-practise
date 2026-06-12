import json

Student = {
    "Name" : "Cha se-gye",
    "Marks" : 59,
    "Age" : 20,
    "Grade" : "C"
}

file_path = "student_details.json"

try:
    with open(file_path, "w") as file:
        json.dump(Student, file, indent=3)

        print(f"{file_path} created successfully!")

except FileExistsError:
    print(f"{file_path} doesn't exists")


