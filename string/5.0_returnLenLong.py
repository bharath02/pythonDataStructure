# Write a Python function that takes a list of words and returns the length of the longest one.
class retLongLen:
    def wordLngLnth(self,String):
        wordLen = []
        for n in String:
            wordLen.append((len(n), n))
        wordLen.sort()
        print(wordLen[-1][1])
String=['abc','abcde','abcdefg','whatAreYouDoing']
lenthWord=retLongLen()
lenthWord.wordLngLnth(String)

