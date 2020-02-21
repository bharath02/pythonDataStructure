# Write a Python program to get the current username
import getpass
class currentUserName:
    def userName(self):
        print(getpass.getuser())
nameUser=currentUserName()
nameUser.userName()