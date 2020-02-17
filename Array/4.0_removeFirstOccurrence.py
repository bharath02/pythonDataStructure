# Write a Python program to remove the first occurrence of a specified element from an array.
class removeFirstOccurrence:
    def mostRepeateRemove(self,List):
        for i in range(len(List)-1):
            for j in range(i+1,len(List)-1):
                if(List[j]==List[i]):
                    List.remove(List[j])
lis=[1,2,5,6,9,1,1,9,5]
obj=removeFirstOccurrence()
obj.mostRepeateRemove(lis)
print(lis)