#  Write a Python program to check multiple keys exists in a dictionary.
class multipleKeysDict:
    def checkKeyDict(self,data):
        print(data.keys()>={'class','name'})
        print(data.keys()>={'india','run'})
        print(data.keys()>={'color','name'})
        print(data.keys()>={'color'})
        print(data.keys() >= {'class'})
        print(data.keys() >= {'bharath'})
        print(data.keys() >= {'name','color','class'})
data={'name':'india', 'color':'red','class':'X'}
keysExist=multipleKeysDict()
keysExist.checkKeyDict(data)