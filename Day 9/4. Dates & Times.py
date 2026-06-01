import datetime

date = datetime.date(2025,5,14)
today = datetime.date.today()

time = datetime.time(12, 30, 3)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S %d-%m-%Y")                 # strftime = to modify how you see the time

print(date)
print(now)
print()

target_datetime = datetime.datetime(2020, 2, 5, 12, 24, 5)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has not passed")