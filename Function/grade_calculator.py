subject = ["Maths", "English", "Social", "Science", "Hindi"]
marks = []

def calculate_marks():

    for sub in subject:
        mark = int(input(f"Enter marks for {sub:9}:"))
        marks.append(mark)

    average = sum(marks) / len(marks)
    return average


    
print("Average score : ",calculate_marks())

