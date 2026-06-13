# List Index Access

# nums = [10, 15, 78, 24, 90, 16]

# try:
#     idx = int(input("Enter index(0-6): "))
#     print(nums[idx])

# except ValueError:
#     print("Not a number")

# except IndexError:
#     print("Index outof range!")

# ----------------------------------------------------
# Use finally to display a message regardless of exceptions

num = [1, 2, "4", 5]
sum = 0

try: 
    for n in num:
        sum += int(n)
        average = sum / len(num)

    print(average)

except TypeError:
    print("Not possible to calculate")

except ValueError:
    print("Not possible")

finally:
    print("Elements in the list should be of same type")

