# Write a Python program to get system command output.
import subprocess
class systemcommand:
    def getSystem(self):
        commOutput=subprocess.check_output("dir",shell=True,universal_newlines=True)
        print("Get System command Output : ", commOutput)
obj=systemcommand()
obj.getSystem()