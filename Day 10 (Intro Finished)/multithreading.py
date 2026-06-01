#multithreading

import time
import threading

def walking_dog(first, last):
    time.sleep(7)
    print(f"You finished walking {first}{last}")

def take_trash():
    time.sleep(2)
    print("You take out the trash")

def get_mail():
    time.sleep(5)
    print("You get the mail")

job1 = threading.Thread(target=walking_dog, args=("Miki", "na"))
job1.start()

job2 = threading.Thread(target=take_trash)
job2.start()

job3 = threading.Thread(target=get_mail)
job3.start()

job1.join()
job2.join()
job3.join()

time.sleep(1)
print("All jobs finished!")