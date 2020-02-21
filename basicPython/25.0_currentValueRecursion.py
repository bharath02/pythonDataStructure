#  Write a Python program to get the current value of the recursion limit.
import sys
class recursionLimit:
    def limit(self):
        print("current value of System recursion value : ",sys.getrecursionlimit())
obj=recursionLimit()
obj.limit()