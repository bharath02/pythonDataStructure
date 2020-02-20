# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
#----------------Sample String : 'abc'
#----------------Expected Result : 'abcing'
#----------------Sample String : 'string'
#----------------Expected Result : 'stringly'
class addINGandLY:
    def strAddIngAndLy(self,String):
        if(len(String)==3):
            String=String+'ing'
            print(String)
    def strAddLy(self,String1):
        if(String1[-3:]=='ing'):
            String1=String1+'ly'
            print(String1)

Str='abc'
Str1='string'
adding=addINGandLY()
adding.strAddIngAndLy(Str)
adding.strAddLy(Str1)
