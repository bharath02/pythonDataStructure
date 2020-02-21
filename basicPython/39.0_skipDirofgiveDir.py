# Write a Python program to find files and skip directories of a given directory.find files and skip directories of a given directory.
from os import listdir
from os.path import isfile, join
class listFileDir:
  def filesDir(self):
         files_list = [f for f in listdir('/home/bridgelabz/Desktop/pythonDataStructure/basicPython') if isfile(join('/home/bridgelabz/Desktop/pythonDataStructure/basicPython', f))]
         print(files_list)
listfile=listFileDir()
listfile.filesDir()