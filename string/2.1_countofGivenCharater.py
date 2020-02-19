# Write a Python program to count the number of characters (character frequency) in a string.
#----------Sample String : google.com
#----------Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
class countGivenChara:
    def contVal(self, String):
        for start in range(len(String)-1):
            count=0
            for compa in range(len(String)-1):
                if(String[start]==String[compa]):
                    count+=1
            print(String[start],":",count,end=",   ")

    def char_frequency(self,string1):
        dict = {}
        for n in string1:
            keys = dict.keys()
            if n in keys:
                dict[n] += 1
            else:
                dict[n] = 1
        return dict

String='google.com'
lenStr=countGivenChara()
lenStr.contVal(String)
print("\n",lenStr.char_frequency(String))