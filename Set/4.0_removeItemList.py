# Write a Python program to remove item(s) from set
class removeItemList:
    def listRemove(self,set1,set2):
        set1.discard(10)
        set2.discard('abs')
        print(set1)
        print(set2)
set1=set([10,20,22,33,55,20])
set2={'abs','Movie','Education','games','time','exams'}
removeList=removeItemList()
removeList.listRemove(set1,set2)