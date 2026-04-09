# i = 1
# while i <= 5:
#     print("Hello")
#     i += 1

#--------------------------------------------------------------

# i = 100
# while i >= 1:
#     print(i)
#     i -= 1

#--------------------------------------------------------------

# n = int(input("Enter num:"))
# i = 1
# while i <= 10:
#     print(f"{n} * {i} = {n*i}")
#     i += 1

#-------------------------------------------------------------
# * * * *
# * * * *
# * * * *
# * * * *

# for i in range(4):
#     for j in range(4):
#         print("*",end=" ")
#     print()

#---------------------------------------------------------------
# *
# * *
# * * *
# * * * *

# for i in range(1,5):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

#-----------------------------------------------------------
# 1
# 1 2
# 1 2 3
# 1 2 3 4

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

#------------------------------------------------------------
# 1 2 3
# 1 2 3
# 1 2 3

# for i in range(3):
#     for j in range(1,4):
#         print(j, end=" ")
#     print()

#-----------------------------------------------------
#print prime numbers from 2 to n

# n = int(input())
# for i in range(2,n+1):            
#     for j in range(2,i):            
#         if i % j == 0:            
#             break                
#     else:                          
#         print(i)                    

#------------------------------------------------------
# Print a 5x5 grid of stars
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# for i in range(5):
#     for j in range(1,6):
#         print("*", end=" ")
#     print()

#----------------------------------------------------
# Print numbers in a 3x4 grid
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4

# for i in range(3):
#     for j in range(1,5):
#         print(j,end=" ")
#     print()

#---------------------------------------------------
# Print row number repeated
# 1 1 1
# 2 2 2
# 3 3 3

# for i in range(1,4):
#     for j in range(3):
#         print(i,end=" ")
#     print()

#---------------------------------------------------
# Print column number repeated
# 1 2 3
# 1 2 3
# 1 2 3

# for i in range(3):
#     for j in range(1,4):
#         print(j,end=" ")
#     print()

#----------------------------------------------------
# Print a 4x4 square of alphabets
# A B C D
# A B C D
# A B C D
# A B C D

# for i in range(4):
#     for j in range(4):
#         print(chr(65 + j),end=" ")
#     print()

#------------------------------------------------------
# Increasing triangle
# *
# **
# ***
# ****

# for i in range(5):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

#-------------------------------------------------------
# Number triangle
# 1
# 12
# 123
# 1234

# for i in range(5):
#     for j in range(1,i+1):
#          print(j,end=" ")
#     print()

#-----------------------------------------------------
# Reverse triangle
# ****
# ***
# **
# *

# for i in range(5,1,-1):
#     for j in range(1,i):
#         print("*",end=" ")
#     print()

#----------------------------------------------------increasing patterns
# A
# B B
# C C C
# D D D D

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(64 + i),end=" ")
#     print()

#-----------------------------------------------------
# Triangle of even numbers
# 2
# 2 4
# 2 4 6
# 2 4 6 8

# n = 4
# for i in range(1,n+1):
#     count = 2
#     for j in range(i):
#         print(count, end=" ")
#         count += 2
#     print()

#-------------------------------------------------------
# *
# * *
# * * *
# * * * *
# * * * * *

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*", end=" ")
#     print()

#------------------------------------------------------
# 1
# 22
# 333
# 4444
# 55555

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end="")
#     print()

#-------------------------------------------------------
# 1
# 12
# 123
# 1234
# 12345

# for i in range(1,6):
#     count = 1
#     for j in range(1,i+1):
#         print(j, end="")
#         count += 1
#     print()

#---------------------------------------------------------
# A
# AB
# ABC
# ABCD
# ABCDE

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(chr(64+j),end="")
#     print()

#----------------------------------------------------------
# 1
# 2 3
# 4 5 6
# 7 8 9 10

# count = 1
# for i in range(1,5):
#     for j in range(i):
#         print(count,end=" ")
#         count += 1
#     print()

#--------------------------------------------------------
# 5
# 5 6
# 5 6 7
# 5 6 7 8

# for i in range(1,5):
#     count = 5
#     for j in range(i):
#         print(count,end=" ")
#         count += 1
#     print()

#---------------------------------------------------------
# 2
# 2 4
# 2 4 6
# 2 4 6 8

# for i in range(1,5):
#     count = 2
#     for j in range(i):
#         print(count,end=" ")
#         count += 2
#     print()

#-------------------------------------------------------------
# *
# * *
# * * *
# * * * *

# for i in range(1,5):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

#-------------------------------------------------------------
# A
# B B
# C C C
# D D D D

# for i in range(1,5):
#     for j in range(i):
#         print(chr(64+i),end=" ")
#     print()

#-------------------------------------------------------------
# 1
# 1 3
# 1 3 5
# 1 3 5 7

# for i in range(1,5):
#     count = 1
#     for j in range(i):
#         print(count,end=" ")
#         count += 2
#     print()

#---------------------------------------------------------------
# 1
# 3 5
# 7 9 11
# 13 15 17 19

# count = 1
# for i in range(1,5):
#     for j in range(i):
#         print(count,end=" ")
#         count += 2
#     print()

#--------------------------------------------------------------
# A
# C E
# G I K
# M O Q S

# count = 65
# for i in range(1,5):
#     for j in range(i):
#         print(chr(count),end=" ")
#         count += 2
#     print()

#----------------------------------------------------------------
# 1
# 2 1
# 3 2 1
# 4 3 2 1

# for i in range(1,5):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()