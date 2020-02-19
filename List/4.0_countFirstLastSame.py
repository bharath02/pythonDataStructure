#  Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
#--------------Sample List : ['abc', 'xyz', 'aba', '1221']
#--------------Expected Result : 2
class countFirstLast:
    def sameStartEndWord(self,list):
        count=0
        for word in list:
            val=len(word)-1
            if(word[0]==word[val]):
                count+=1
        print("Result of same words in first and last : ",count)

lis=['abc','xyz','aba','1221']
countSame=countFirstLast()
countSame.sameStartEndWord(lis)