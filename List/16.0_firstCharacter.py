# Write a Python program to split a list based on first character of word.
class splitList:
    def firstCharacter(self,listWord):
        character = listWord.split(" ")
        for word in character:
            print(word[0],end="   ")
list1="Hi! are you going to college, if. Please see My Bench"
words=splitList()
words.firstCharacter(list1)