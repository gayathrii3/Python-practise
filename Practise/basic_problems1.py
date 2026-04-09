# print("Bhak")

# a = int(input("Enter a value:"))
# b = int(input("Enter b value:"))
# sum = a+b
# print(f"sum is {sum} ")

# a = 23
# b = 21
# print(f"before swapping{a,b}")
# temp = a
# a = b
# b = temp
# print(f"after swapping{a,b}")

# name = input("Enter your name:")
# while name == "":
#     name = input("Enter your name:")
# print(f"Hello {name}")

# len = int(input("length ="))
# wid = int(input("width ="))
# area = 2*(len * wid)
# print(f"Area of rectangle is {area}")

# num = int(input("num ="))
# if num % 2 == 0:
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd")

# a,b,c = 21,34,78
# print(f"{max(a,b,c)} is the largest number")

# year = int(input("year = "))
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")

# marks = int(input("Enter marks:"))
# if marks >= 80:
#     print("A")
# elif marks >= 70:
#     print("B")
# else:
#     print("C")

# num = float(input("num ="))
# if num > 0:
#     print(f"{num} is a positive integer")
# elif num < 0:
#     print(f"{num} is a negative integer")
# else:
#     print("Zero")

# i = 1
# for i in range(1,11):
#     print(i)

# n = int(input("table of "))
# i = 1
# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")

# n = int(input())
# i = 1
# count = 0
# for i in range(1,n+1):
#     count =count+i
# print(count)

# num = str(23456)
# print(len(num))
    


# num = int(input("num ="))
# i = 1
# fact = 1
# for i in range(1,num+1):
#     fact = fact*i
# print(f"factorial of {num} is {fact}")

# fruits = ["Apple","Orange","Custard Apple","Dragon fruit"]
# for fruit in fruits:
#     print(fruit)

# nums = [2,8,21,34,29,54]
# # print(f"largest num is {max(nums)}, smallest num is {min(nums)}")
# large = nums[0]
# small = nums[0]
# for n in nums:
#     if n > large:
#         large = n
#     if n < small:
#         small = n
# print("largest =",large,"smallest =",small)


# name = "GAYATHRI"
# reverse = ""
# for letter in name:
#     reverse = letter + reverse
# print("reversed string:",reverse)


# word = "SavanamLakshmiGayathri"
# count = 0
# for ch in word:
#     if ch.lower() in "aeiou":
#         count += 1
# print(f"No. of vowels = {count}")


# name = "rappAr"
# if name == name[::-1]:
#     print("palindrome")
# else:
#     print("not a palindrome")


# students = {"Gayathri" : 98,
#             "Sirisha" : 79,
#             "Lavanya" : 96}
# print(students.items())


# marks = {}
# x = int(input("Eng ="))
# marks.update({"English" : x})
# y = int(input("Sci ="))
# marks.update({"Science" : y})
# z = int(input("Math ="))
# marks.update({"Maths" : z})
# print(marks)


# match expression
# word = 1
# match word:
#     case 1:
#         print("Gaya")
#     case 2:
#         print("Go")
#     case _:
#         print("End")


# i = 1
# for i in range(1,51):
#     if i % 2 == 0:
#         print(i)


# i = 1
# sum = 0
# for i in range(1,5):
#     if i % 2 != 0:
#         sum = sum + i
# print(sum)
    
    
# n = int(input())
# for i in range(1,11):
#     print(n ,"*",i,"=",n*i)


# num = 2355
# sum = 0
# while num > 0:
#     last = num % 10
#     sum = sum + last
#     num = num // 10
# print(sum)
            
        
# list = [2,3,2,3,5,4,5,6]
# num = {}
# for n in list:
#     if n in num:
#         num[n] += 1
#     else:
#         num[n] = 1
# print(num)
