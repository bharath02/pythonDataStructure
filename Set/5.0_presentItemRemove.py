# Write a Python program to remove an item from a set if it is present in the set.
class removeItemPresent:
    def listRemovePresent(self,set1,set2):
         set1.discard(10)
         set2.discard('exams')
         print(set1)
         print(set2)
set1={10,20,22,33,55,20}
set2={'abs','Movie','Education','games','time','exams'}
removeList=removeItemPresent()
removeList.listRemovePresent(set1,set2)