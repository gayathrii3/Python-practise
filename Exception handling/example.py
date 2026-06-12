# List Index Access

nums = [10, 15, 78, 24, 90, 16]

try:
    idx = int(input("Enter index(0-6): "))
    print(nums[idx])

except ValueError:
    print("Not a number")

except IndexError:
    print("Index outof range!")
