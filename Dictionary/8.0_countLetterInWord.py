# Write a Python program to create a dictionary from a string. Note: Track the count of the letters from the string.
#----------Sample string : 'w3resource'
# ---------Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
class countLetterInWords:
    def countString(self,String):
        dict={}
        for count in String:
            keys=dict.keys()
            if count in keys:
                dict[count]+=1
            else:
                dict[count]=1
        print(dict)

string='w3resource'
counting=countLetterInWords()
counting.countString(string)