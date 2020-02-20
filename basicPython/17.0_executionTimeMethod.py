# Write a program to get execution time for a Python method
import time
class pythonMethod:
    def timeMethod(self,n):
        start_time = time.time()
        s = 0
        for i in range(1,n+1):
            s = s + i
        end_time = time.time()
        print(s,"times : ",end_time-start_time)
number=5
methTime=pythonMethod()
methTime.timeMethod(number)
