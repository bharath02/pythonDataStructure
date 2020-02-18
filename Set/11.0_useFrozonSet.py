# Write a Python program to use of frozensets.
class useFrozenSets:
    def forzenset(self,set1,set2):
        frozen = 0
        for i in set1:
            int(frozen)
            co=0
            int(co)
            for j in set2:
                if(i==j):
                    co+=1
            if(co==0):
                frozen+=1
        if(frozen==len(set1)):
            print(set1,set2,": are frozen sets")
        else:
            print(set1,set2, " Are not frozen sets")
set1={1,2,3,4,5}
set2={6,7,8,9,10}
frozen=useFrozenSets()
frozen.forzenset(set1,set2)