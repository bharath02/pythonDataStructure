# Write a Python program to convert a list into a nested dictionary of keys.
class convertListToDic:
    def listToNestedDict(self,List):
        current={}
        nestedDict=current
        for name in List:
            current[name] = {}
            current = current[name]
        print(nestedDict)
list=[1,2,3,4,5,22,33,10]
set=convertListToDic()
set.listToNestedDict(list)