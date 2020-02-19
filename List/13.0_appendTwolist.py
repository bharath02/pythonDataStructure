# Write a Python program to append a list to the second list.
class appedLists:
    def listCopy(self,List1):
        List2=[]
        for val in List1:
            List2.append((val))
        print(List2)
Lst=[1,2,3,"Bharath",5,6,"student",7,8,9,'hi']
lstCopy=appedLists()
lstCopy.listCopy(Lst)