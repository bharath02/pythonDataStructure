# Write a Python program to get the difference between the two lists.
class differenceTwoList:
    def diffLists(self,List1,List2):
        val=set(List1)-set(List2)
        print(list(val))
List1=[1,2,3,4,5,6]
List2=[0,9,8,7,6,5]
difLst=differenceTwoList()
difLst.diffLists(List1,List2)