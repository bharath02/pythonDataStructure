# Write a Python program to get file creation and modification date/times
import os.path, time
class creationModification:
    def fileCreateModification(self):
        print("Last modified: %s" % time.ctime(os.path.getmtime("abc.txt")))
        print("Created: %s" % time.ctime(os.path.getctime("abc.txt")))
create=creationModification()
create.fileCreateModification()