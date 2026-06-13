# Doing multiple tasks simultaneously based on the time taken for it(for file handling , fetching data from API's)

import threading
import time

def walk_dog():
    time.sleep(5)
    print("You finished walking the Dog!🐶")

def wash_dishes():
    time.sleep(3)
    print("You completed washing the Dishes!🍽️")

def throw_trash():
    time.sleep(1)
    print("You take out the trash!🗑️")

chore1 = threading.Thread(target=walk_dog)
chore1.start()
chore2 = threading.Thread(target=wash_dishes)
chore2.start()
chore3 = threading.Thread(target=throw_trash)
chore3.start()

chore1.join()   #printing statement waits till the chores are completd
chore2.join()
chore3.join()

print("All the chores are completed👏")