# Write a Python program to get an absolute file path.
import os
class filePathAbsolute:
    def absoluteFilePath(self,path_fname):
        print(os.path.abspath('path_fname'))

obj=filePathAbsolute()
obj.absoluteFilePath("test.txt")