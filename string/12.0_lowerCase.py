# Write a Python program to lowercase first n characters in a string.
class lowerCase:
    def nLowercases(self,String,n=4):
        print(String[:4].lower()+String[4:])
String="BHARATH"
low=lowerCase()
low.nLowercases(String)