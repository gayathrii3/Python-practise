# name = 'Gaya-thri'
# print(name[::2])

#--------------------------------------------------------------
# using credit card number

# credit_number = "1234-5678-9876"
# last_digit = credit_number[-4::]
# print(credit_number[::-1])
# print(f" your credit card number is XXXX-XXXX-{last_digit}")

#--------------------------------------------------------------
# Reverse a String

# name = "Gayathri"
# reverse = ""

# for n in range(len(name) - 1, -1, -1):
#     reverse += name[n]
    
# print(reverse)

# ---------------------------------------------------------------
# Check Palindrome String

# s = "pop"
# ss = ""

# for i in range(len(s) - 1 , -1, -1):
#     ss += s[i]
# print("Palindrome" if ss == s else "Not palindrome")

# --------------------------------------------------------------
# Count Uppercase and Lowercase Letters

# s = "GayaReddy"

# lower = 0
# upper = 0

# for i in s:
#     if i.islower():
#         lower += 1
#     elif i.upper():
#         upper += 1

# print("Lower case" , lower)
# print("Upper case" , upper)

# --------------------------------------------------------------
# Remove Spaces from a String

# s = "Gaya thri Reddy"

# result = s.replace(" ", "")

# print(result)

# --------------------------------------------------------------
# Find Length of Each Word

# s = "virtual world"
# result = s.split()

# for word in result:
#     print(word, len(word))

# -------------------------------------------------------------
# First Non-Repeated Character

# s =  "gayathri"

# freq = 1

# for ch in s:
#     if s.count(ch) == freq:
#         print(ch)
#         break

# --------------------------------------------------------------