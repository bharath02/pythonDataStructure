# Write a Python program to create an array of 5 integers and display the array items. Access individual element through indexes.

class arrayIndex:
    def index(self,indexNumber):
        self.indexNumber=indexNumber
        for i in range(len(indexNumber)):
            print(indexNumber[i])

indexNumber = [2,10,22,33,55]
obj=arrayIndex()
obj.index(indexNumber)
