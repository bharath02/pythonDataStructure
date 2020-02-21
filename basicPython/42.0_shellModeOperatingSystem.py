# Write a Python program to determine if the python shell is executing in 32bit or 64bit mode on operating system.
import struct
class modelOperatingSystem:
    def shellExecuting(self):
        print(struct.calcsize("P") * 8)
obj=modelOperatingSystem()
obj.shellExecuting()