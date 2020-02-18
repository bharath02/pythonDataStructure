# Write a Python program to remove item(s) from set
class removeItemList:
    def listRemove(self,set1,set2):
        setRemove=set1-set2
        print(setRemove)
set1=set(["Hi","!", "Hello","How","are","you","?","u"])
set2=set(["Hello","u"])
removeList=removeItemList()
removeList.listRemove(set1,set2)