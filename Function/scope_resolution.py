# variable scope --->  where a variable is visble and accessable
# scope resolution order (LEGB) ---> Local --- Enclosed --- Global --- Built-in

# (Where the variable is declared ---like the position outside the func, inside,etc) 

# ************************************************************************************

# def func1():
#     n = 1      # local variables
#     print(n)

# def func2():
#     n = 2
#     print(n)

# func1()
# func2()

# ------------------------

# def func1():

#     def func2():
#         n = 2       #Enclosed variable(checks where the variable is present)
#         print(n)
#     func2()

# func1()

# ------------------------

# def func1():

#     def func2():
#         print(n)
#     func2()

# n = 2 * 2   # global var(outside of the function)

# func1()

# -----------------------

from math import pi     # buit-in variables

def add(radius):
    circum = 2 * pi * radius
    return circum

print(f"{add(4):.2f}")