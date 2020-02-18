# Write a Python program to count number of items in a dictionary value that is a list.
class numberItemsDict:
    def listCountNumber(self, data):
        values=sum(map(len,data.values()))
        print(values)
data={1:["a","b","c","d"],2:[10,11,12]}
itemDict=numberItemsDict()
itemDict.listCountNumber(data)