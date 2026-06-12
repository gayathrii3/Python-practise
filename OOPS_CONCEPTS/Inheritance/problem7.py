class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        # self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

    # def calcpercentage(self):
    #     self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"


    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

stu1 = Student(34, 67, 89)            #attribute ki value func ke uper depend ho rahi hai-- then use @property decorator
stu2 = Student(78, 89, 94)

stu1.phy = 99
print(stu1.phy)
# stu1.calcpercentage()
print(stu1.percentage)