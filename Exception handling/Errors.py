# Exception - intrupts the flow of program

try:
    num = int(input("Enter number: "))
    print(1 / num)

except ZeroDivisionError:
    print("Can't divide by 0")
except ValueError:
    print("Enter a number IDIOT!!")
except Exception:
    print("Invalid input")

finally:   # will execute regardless of exception
    print("Done!")
    
# --------------------------------------------------------
# ZerodivisionError ----> when u try to divide a num with 0
# ---------------------------------------------------------

# a = 1 / 0

# print(a)

# ---------------------------------------------------------
# TypeError ---> when u try to perform an operation of the wrong datatype
# --------------------------------------------------------

# a = 1
# b = '1'

# print(a + b)

# ---------------------------------------------------------
# ValueError --- attempt to typecast the wrong datatype
# ---------------------------------------------------------

# a = int('Gayathri')

# print(a)

# ---------------------------------------------------------
