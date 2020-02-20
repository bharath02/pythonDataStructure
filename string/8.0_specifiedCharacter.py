# Write a Python program to get the last part of a string before a specified character.
#---------------https://www.w3resource.com/python-exercises
#---------------https://www.w3resource.com/python
class specifiedCharacter:
    def charaterSpecial(self,String):
        print(String.rsplit('-', 1)[0])
String="https://www.w3resource.com/python-exercises"
spl=specifiedCharacter()
spl.charaterSpecial(String)