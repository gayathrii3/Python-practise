# Check Palindrome Number  #1331 (first reverse the number then check if it matches with the original num)

num = int(input())                           
original = num              
rev_num = 0

if num < 0:
    print("Not a palindrome")
else:
    while num > 0:
        last_digit = num % 10
        rev_num = rev_num  * 10 + last_digit
        num = num // 10
    if original == rev_num:
        print(f"{original} is a palindrome")
    else:
        print("Not a palindrome")
     

