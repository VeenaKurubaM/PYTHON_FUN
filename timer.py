"""time function"""
import time
my_time=input("enter time in seconds: ")
my_time=int(my_time)
time.sleep(my_time)
print("2 seconds time is finished")

"""print all numbers within the given time"""
for x in range(0,my_time):
    print(x)
    time.sleep(my_time)
print("Given time is finished")

"""print backward time"""
for x in range(my_time,0,-1):
    print(x)
print("Its time now")

"""print with reversed backward time"""
for x in reversed(range(0,my_time)):
    print(x)
print("Its time now by using reversed")