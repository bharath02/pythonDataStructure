# Write a Python program to clear a set.
class clearSet:
    def clearVal(self,Set):
        Set.clear()
        print(Set)
Set={1,2,3,4,5,6,2,9,8,7}
clear=clearSet()
clear.clearVal(Set)