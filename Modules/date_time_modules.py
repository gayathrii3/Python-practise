import datetime

date = datetime.date(2026, 2, 1)  #2026-02-01
today = datetime.date.today()   #2026-06-13

time = datetime.time(23, 12, 34)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S  %m-%d-%Y")
# print(date)
# print(today)   

print(now)
