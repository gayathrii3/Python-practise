import csv

employees = [["Name", "Age", "Job"],
             ["Gayathri", 20, "SDE"],
             ["Siri", 21, "Chef"],
             ["Bindu", 21, "Singer"],
             ["Ammulu", "16", "Student"]]

file_path = "employee_details.csv"

try:
    with open(file_path, "w") as file:
        writer = csv.writer(file)
        for employ in employees:
            writer.writerow(employ)
        print(f"csv file {file_path} is created!")

except FileExistsError:
    print(f"{file_path} not found")
