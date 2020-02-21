# Write a Python program to add leading zeroes to a string.
class addLeadingZero:
    def leadingZero(self,number):
        print(number.ljust(8,'0'))
        print(number.ljust(10,'0'))
num='122.3.3'
obj=addLeadingZero()
obj.leadingZero(num)