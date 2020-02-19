#  Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
#------------------------Sample String : 'restart'
#------------------------Expected Result :'resta$t'
class changeFirstRep:
    def firstReptoSym(self,String):
        for i in String:
            if(i=='r'):
                i='$'
            print(i,end=" ")

    def change_char(self,str1):
        char = str1[0]
        str1 = str1.replace(char, '$')
        str1 = char + str1[1:]
        print(str1)


String='restart'
changStr=changeFirstRep()
changStr.firstReptoSym(String)
changStr.change_char(String)


