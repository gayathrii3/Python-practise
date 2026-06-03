password = "gaya3"

def check_pass():
    count = 0

    while True:
        check = input("Enter password :").lower()

        if check == password:
            print("CORRECT PASS!")
            break
        else:
            print("WRONG PASS!")
            count += 1
        
        if count == 3:
            print("TOO MANY TRIES , TRY AGAIN LATER!")
            break
check_pass()