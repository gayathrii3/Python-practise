import random

options = ("rock","papaer","scissors")
playing = True

while playing:
    player = None
    computer = random.choice(options)
    while player not in options :
        
        
        player = input("Enter a choice(rock, papaer, scissors):  ")

        print(f"Player : {player}")
        print(f"Computer : {computer}")

        if player == computer:
            print("It's a Tie!")
        elif player == "rock" and computer == "scissors":
            print("You WIN!!")
        elif player == "paper" and computer == "rock":
                print("You Win!!")
        elif player == "scissors" and computer == "paper":
                print("You WIN!!")
        else:
            print("You lose!!")
            
            
        play_again = input("Play again? (y/n)")
        if play_again != "y":
            playing = False
print("thanks for playing")
        
        
            
            