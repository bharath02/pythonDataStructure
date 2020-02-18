# Write a Python program to create an intersection of sets.
class intersectionSet:
    def sameVariableSet(self,set1,set2):
        intersec=set1&set2
        print(intersec)
    def functionintersectio(self,set1,set2):
        intersec1=set1.intersection(set2) #using intersection function
        print(intersec1)
set1={'a','e','i','o','u',1,2,3,4,5,6,7,8,9,0,'l','u'}
set2={'i','l','u',4,3,1,'v','h','b','z'}
interSet=intersectionSet()
interSet.sameVariableSet(set1,set2)
interSet.functionintersectio(set1,set2)