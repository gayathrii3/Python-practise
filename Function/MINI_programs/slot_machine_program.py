import random

spining = True

def slot_machine():
    symbols = ['🍉', '🍌', '🍏', '🍒']
    attempts = 0

    while spining:
        result = []
        attempts += 1

        print("----------SPIN THE SLOT--------")

        print("symbols : 🍉 🍌 🍏 🍒")      # W + : (to get emojis)

        for symbol in range(3):
            result.append(random.choice(symbols))

        print(" | ".join(result))

        if result[0] == result[1] == result[2]:
            print("🎉 JACKPOT! 🎉")
        
        choice =  input("Try again?(y/n):").lower()


        if choice != 'y':
                print("Thanks for playing!")
                break
               
    return result
        

slot_machine()