# Write a python program to call an external command in Python.
from subprocess import call
class externalCommand:
    def commandExternal(self):
        call(["ls", "-l"])
obj=externalCommand()
obj.commandExternal()