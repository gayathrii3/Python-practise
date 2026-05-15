# def calc_sum(a, b):
#     sum = a + b

#     print(sum)
#     return sum

# calc_sum(2, 5)
# calc_sum(7, 90)

# -------------------------------------------------

# def calc_sum(a, b):   #function defination(parameters)
#     return a + b

# sum = calc_sum(4,8)    #function calling(i/p arguments)
# print(sum)

# -------------------------------------------------

# def name():
#     print("Gayathri")

# name()

# -------------------------------------------------
# Average of 3 numbers

# def find_avg(nums):

#     total = 0
#     count = 0

#     for n in nums:
#         total += n
#         count += 1

#         avg = total / count

#     return avg
    
# nums = [2, 7, 9, 5]

# print(find_avg(nums))

# -----------------------------------------------
# built-in functions

# print("Gayathri","Reddy", sep=" $ ")
# print("Gayathri",end='\n'"Reddy")

# -----------------------------------------------
# print length of list

# def length_of_list(num1):
#     return len(num2)

# num1 = [1, 5, 7, 9, 4, 3]
# num2 = num1.copy()

# print(length_of_list(num2))
# print(length_of_list(num1))

# ------------------------------------------------
# print the elements of a list in a single line

# def single_line(list): # ---------> even if function is not called or not returned, it doen't affect anything
#     return list

# words = ["Gayathri", "Lavanya", "Keerthi"]

# for w in words:
#     print(w,end=" ")

# ------------------------------------------------
# Factorial of n

# def factorial(n):
#     fact = 1

#     for i in range(1, n + 1):
#         fact *= i

#     return fact

# print(factorial(2))

# ------------------------------------------------
# convert USD to INR

# def currency_converter(usd_value):
#     USD = 95.7
#     INR = amt * USD

#     return INR

# print(f"₹{currency_converter(500):.2f}")

# ------------------------------------------------
# find square of a number

# def find_square(n):
#     square = n * n
#     return square   #return : gives value

# print(find_square(7))   #print : shows value

# ------------------------------------------------
# Check even or odd

# def check_even(n):

#     if n % 2 == 0:
#         return "EVEN"
#     else:
#         return "ODD"

# print(check_even(80))

# ------------------------------------------------
# Find largest of 3 numbers

# def largest_of_3(a, b, c):

#     largest = a
#     if b > largest:
#         largest = b
#     if c > largest:
#         largest = c

#     return largest

# print(largest_of_3(2, 6, 9))

# --------------------------------------------------
# Count vowels in a string

# def count_vowels(name):

#     count = 0
#     for v in name:
#         if v in "aeiou":
#             count += 1

#     return count
# print(f"vowels = {count_vowels("keerthi")}")

# ---------------------------------------------------
# Reverse a string

# def reverse_a_string(string):

#     reverse = ""

#     for ch in string:
#         reverse = ch + reverse

#     return reverse

# print(reverse_a_string("Gayathri"))

# ---------------------------------------------------
# Check palindrome

def is_palindrome(word):

    reverse = ""

    for ch in word:
        reverse = ch + reverse

    if reverse == word:
        return "Palindrome"
    else:
        return "Not Palindrome"

print(is_palindrome("MADAM"))











