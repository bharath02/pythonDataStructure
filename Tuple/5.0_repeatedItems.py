# Write a Python program to find the repeated items of a tuple.
class repeatedElements:
    def itemsTuple(self,Tup):
        count1=Tup.count(1)
        cunt2=Tup.count(2)
        print(count1, cunt2)
Tup=(1,2,3,4,5,6,1,2,9,8,7)
Tuple=repeatedElements()
Tuple.itemsTuple(Tup)