# Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).
# ----------------------Sample Words : red, white, black, red, green, black
# ----------------------Expected Result : black, green, red, white,red
class sortedcharacters:
    def sortCharatres(self,strings):
        strings=sorted(strings.split(" "))
        print("".join(strings))
    def sortIter(self,String):
        String=String.split(" ")
        leng=len(String)-1
        for str in range(leng):
            for cop in range(leng-str):
                if(String[cop]>String[cop+1]):
                    String[cop],String[cop+1]==String[cop+1],String[cop]
            print("".join(String[cop]),end=" ")


String="red, white, black, red, green, black,"
sortedwords=sortedcharacters()
sortedwords.sortCharatres(String)
sortedwords.sortIter(String)