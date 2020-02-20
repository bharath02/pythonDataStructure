# Write a python program to access environment variables
import os
class environmentVariable:
    def accessVariableEnvi(self):
        print("Environments : ",os.environ)
        print("Environments Variable HOME : ",os.environ['HOME'])
        print("Environments Variable PATH : ",os.environ['PATH'])
enviAccessVari=environmentVariable()
enviAccessVari.accessVariableEnvi()