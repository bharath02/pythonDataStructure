# Write a Python program to create set difference.
class createDifferntSet:
    def setDiff(self,set1,set2):
        setDiff=set1-set2
        print(setDiff)
    def functionSet(self,set1,set2):
        setDiff1=set1.difference(set2)
        print(setDiff1)
set1={'a','e','i','o','u',1,2,3,4,5,6,7,8,9,0,'l','u'}
set2={'i','l','u',4,3,1,'v','h','b','z'}
diffSet=createDifferntSet()
diffSet.setDiff(set1,set2)
diffSet.functionSet(set1,set2)