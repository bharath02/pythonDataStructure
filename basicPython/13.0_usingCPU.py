# Write a Python program to find out the number of CPUs using.
import multiprocessing
class countCPU:
    def usingCPU(self):
        print(multiprocessing.cpu_count())
work=countCPU()
work.usingCPU()
