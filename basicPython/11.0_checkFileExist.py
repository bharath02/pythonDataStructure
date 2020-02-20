# Write a Python program to check whether a file exists.
import os.path
class fileExist:
    def checkFile(self):
        open('abc.txt', 'w')
        print(os.path.isfile('abc.txt'))
file=fileExist()
file.checkFile()