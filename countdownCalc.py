import time


def count(t):
    for x in range (0,t):
        second = t % 60
        minute = int(t / 60) % 60
        hour = int(t / 3600)
        print(f"{hour:02}:{minute:02}:{second:02}", end="\r")
        t = t - 1
        time.sleep(1)
    print("TIME'S UP")



my_time = int(input("Enter time in seconds: "))
count(my_time)