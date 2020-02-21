# Write a Python program to get the users environment.
import os
class userEnvironment:
    def getUserEnvironment(self):
        print(os.environ)
obj=userEnvironment()
obj.getUserEnvironment()