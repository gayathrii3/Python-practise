import time

timer = int(input("Set your time(in sec):"))
for i in range(timer,0,-1):
    seconds = i % 60
    minutes = int(i / 60) % 60
    hour = int(i / 3600)
    print(f"{hour:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP!")
