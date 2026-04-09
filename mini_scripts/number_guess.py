import random

lowest_num = 1
highest_num = 50

answer = random.randint(lowest_num,highest_num)
guesses = 0
is_running = True

print("Python number guessing")
print(f"Select you number between {lowest_num} and {highest_num}")

while is_running:
    guess = (input("Enter your number: "))
    
    if guess.isdigit():
        num = int(guess)
        guesses += 1
        
        if num < lowest_num or num > highest_num:
            print("out of range!")
            print(f"Select you number between {lowest_num} and {highest_num}")
        elif num < answer:
            print("Too low , TRY AGAIN!")
        elif num > answer:
            print("Too high , TRY AGAIN!")
        else:
            print(f"CORRECT! The answer is {answer}")
            is_running = False
            
    else:
        print("Invalid guess!")
        print(f"Select you number between {lowest_num} and {highest_num}")

    