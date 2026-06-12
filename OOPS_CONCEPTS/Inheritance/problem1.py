# Create student class that takes name & marks of 3 subjects as arguments in constructor, then create a method to find the average

class student():

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_average(self):
        sum = 0
        for mark in self.marks:
            sum += mark
        print(f"Hi {self.name} , your average is {sum/3:.2f}")

student1 = student("Han Yeri", [98,68,59])
# print(f"Name = {student1.name}\nMarks = {student1.marks}")

student2 = student("Dong-lee", [72,35,90])
print(f"Name = {student2.name}\nMarks = {student2.marks}")
        
del student2    # after deletion causes error--- not defined

student2.get_average()