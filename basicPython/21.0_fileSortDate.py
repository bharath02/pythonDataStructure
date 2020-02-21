# Write a Python program to sort files by date.
import glob
import os
class sortFile:
    def filesDate(self):
        files = glob.glob("*.txt")
        files.sort(key=os.path.getmtime)
        print("\n".join(files))
sorted=sortFile()
sorted.filesDate()