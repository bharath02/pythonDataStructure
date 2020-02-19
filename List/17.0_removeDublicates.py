# Write a Python program to remove duplicates from a list of lists.
#-------------Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
#-------------New List : [[10, 20], [30, 56, 25], [33], [40]]
class listDuplicateRemove:
    def removeDuplicate(self,List):
        final_list=[]
        for Lst in List:
            if Lst not in final_list:
                final_list.append(Lst)
        print(final_list)
List=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
dupRem=listDuplicateRemove()
dupRem.removeDuplicate(List)