import time

timer = int(input("Enter you timer (s):"))

for x in range(timer, 0, -1):
    seconds = x % 60
    minutes = (x // 60) % 60
    hours = (x // 3600) % 60
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time's UP!")