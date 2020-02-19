# write a Program to Copy or Clone a list
class listCopyOrClone:
    def aCopyOrClone(self,List):
        copyList=List
        print("copy List : ",copyList)
    def cloneList(self,List):
        cloneLst=List[:]
        print("cloneList : ", cloneLst)
List=(1,2,3,4,5,6,7,8,9,10)
copyList=listCopyOrClone()
print("Original List : ",List)
copyList.aCopyOrClone(List)
copyList.cloneList(List)