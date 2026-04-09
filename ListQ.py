# list = [2,91,8,78,92,35]
# list.append(10)
# list.sort(reverse=False)
# list.pop(1)
# list2 = list.copy()
# list.remove(8)
# list.reverse()
# list = list.index(2)
# list.insert(0,23)
# print(list)

#------------------------------------------
# Create a list of 5 numbers and print each number using a loop.

# list = [1,2,3,4,5]
# for num in list:
#     print(num,end=" ")

#---------------------------------------------
# Add an element in the list

# list = [1,2,3,'gaya']
# list.append('thri')

# print(list)

#---------------------------------------------
# Insert an element at index 2.

# list = [1,2,3,'gaya']
# list.insert(2,'lakshmi')

# print(list)

#----------------------------------------------
# length of the list

# list = [1,2,3,'gaya']
# print(len(list))

#---------------------------------------------
# print the largest and smallest number

# list = [3,8,9,23,87,25,16]
# print(f"largest number is {max(list)} and smallest number is {min(list)}")

#-----------------------------------------------
# check if a number exist in list

# list = [1,7,15,18,19,20,2]
# for num in list:
#     if num == 19:
#         print(f"{num} exists at index {list.index(num)}")
#     else:
#         print(num)

#------------------------------------------------
# count the number of times an element appears using dictionary

# list = [2,5,8,3,5,8,9,2]
# nums = {}

# for i in list:
    # if i in nums:
    #     nums[i] += 1
    # else:
    #     nums[i] = 1
# print(nums)

#------------------------------------------------
# Take a list of integers and print all elements greater than the average of the list.

# list = [2,6,39,34,28,14]
# avg = sum(list)/len(list)

# for num in list:
#     if num > avg: 
#         print(num,end=" ")
# print(f"are the elements greater than {avg:.2f}")

#---------------------------------------------------------
# Given a list, reverse it without using reverse() or slicing ([::-1]).

# list = [2,6,39,34,28,14]  #rev each num in the list
# reverse_list = []

# for num in list:
#     rev = 0
#     while num > 0:
#         digit = num % 10
#         rev = rev * 10 + digit
#         num//=10
#     reverse_list.append(rev)
    
# print(reverse_list)

#----------------------------------------
# list = [2,6,39,34,28,14]  #rev each num in the list
# reverse_list = []
# num = len(list) - 1

# while num >= 0:
#     reverse_list.append(list[num])
#     num -= 1
# print(reverse_list)
    
#--------------------------------------------------------
# Find the second largest element without using max() or sort().

# list = [2,6,12,45,23,78]
# largest = list[0]
# sec_largest = list[0]

# for num in list:
#     if num > largest:
#         sec_largest = largest
#         largest = num
#     elif num > sec_largest and num != largest:
#         sec_largest = num
        
# print(f"second largest number is:{sec_largest}")

#-----------------------------------------------------------
# Count how many duplicate elements are present in the list.

# list = [2,3,2,4,6,6,7,3,9,6,2,2]
# dup = {}

# for num in list:
#     if num not in dup:
#         dup[num] = 1
#     else:
#         dup[num] += 1
        
# print(dup)

#-------------------------------------------------------------
#Remove all occurrences of a specific number from the list without using remove().

# list = set([2,3,2,4,6,6,7,3,9,6,2,2])
# print(list)
    
# Given a list, move all zeros to the end while keeping other elements in order.

# list = [2,0,5,8,0,0,4,3,0]
# new_list = []

# for num in list:
#     if num != 0:
#         new_list.append(num)
# count = 0
# for num in list:
#     if num == 0:
#         count += 1
#         new_list.append(0)
        
# print(new_list)

#---------------------------------------------------------------
# find the largest number in a list.

# list = [23,45,67,58,64]
# large = 0

# for n in list:
#     if n > large:
#         large = n
# print(f"largest number among {list} is {large}")
    
#-----------------------------------------------------------------
# Remove all duplicates from a list.

# list = set([23,45,23,45,78,43,90,12])
# print(list)

#-----------------------------------------------------------------
# Count how many times a number appears in a list.

# list = [2,3,4,3,5,4,6,5,5,5,6]
# new_list = {}
# for n in list:
#     if n not in new_list: 
#         new_list[n] = 1
#     else:
#         new_list[n] += 1
# print(new_list)

#----------------------------------------------------------------
# Given a list of numbers, separate into even and odd lists.

# list = [2,3,43,56,78,91,39,71,13,23,41,10]
# odd = []
# even = []

# for n in list:
#     if n % 2 == 0:
#         even.append(n)
#     else:
#         odd.append(n)
# print(even,odd)

#---------------------------------------------------------------
# Merge two sorted lists into one sorted list.

# list = [2,5,7,3,21,8,45,20,76]
# list2 = [21,32,23,54,87]
# list.extend(list2)

# print(sorted(list))

# Flatten a nested list
# Example: [[1,2], [3,4], [5]] → [1,2,3,4,5]

# Rotate a list by n positions
# Example: [1,2,3,4,5] rotate by 2 → [4,5,1,2,3]
        

        
