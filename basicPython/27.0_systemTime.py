# Write a Python program to get the system time
import time
class systemTime:
    def getSysTime(self):
        print(time.ctime())

obj=systemTime()
obj.getSysTime()