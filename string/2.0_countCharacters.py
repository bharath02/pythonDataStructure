# Write a Python program to count the number of characters (character frequency) in a string.
class countCharacters:
    def countNumChar(self,string):
        count=0
        for chars in range(len(string)-1):
            if(string[chars]!=' '):
                count+=1
        print("Count of characters : ", count )
string="hi this is for checking length of a string"
cont=countCharacters()
cont.countNumChar(string)
