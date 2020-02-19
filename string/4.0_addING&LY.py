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
        if(len(String)-1>=5):
            String=String+'ly'
            print(String)

Str='abc'
Str1='string'
adding=addINGandLY()
adding.strAddIngAndLy(Str)
adding.strAddIngAndLy(Str1)
