# Write a Python program to get the number of occurrences of a specified element in an array.
class countOfElement:
    def numberOccurrence(self,Elements):
        for i in range(len(Elements)-1):
                print(Elements[i], "Count : ", Elements.count(Elements[i]))

Element=[1,2,3,4,5,6,7,8,1,1,1,1,2,2,2,2,5,5,5,6,8,9,4,9,2,2,2]
obj=countOfElement()
obj.numberOccurrence(Element)