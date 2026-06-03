# class Student:
#     name = "Gayathri"  

# s1 = Student()     #object for the class--Student
# print(s1.name)

# s2 = Student()
# print(s2.name)

# ---------------------------------------------------

# class Car:
#     colour = "Black"
#     safety_feature = "Airbags"

# car1 = Car()  #object creation
# car2 = Car()

# print(car1.colour)
# print(car2.safety_feature)

# ----------------------------------Constructor(__init__)---------------------------------------(in-built)

class Student():  #class name

    def __init__(self):  #default constructor
        pass

    def __init__(self, name, age):   #parameterized constructor
        pass

    def __init__(self, name, age):   #constructor takes the (self) parameter by default -- nothing but the new object created i.e, s1 == self
        self.name = name
        self.age = age
        print("Adding student name..")
        
s1 = Student(name="Gayathri Reddy", age=20)   #calling the object
print("Name =", s1.name, "Age =", s1.age, sep=' | ')

s2 = Student(name="Maurya Varun", age=19)
print("Name =", s2.name, "Age =", s2.age, sep=' | ')
