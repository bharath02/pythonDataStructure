# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
#--------Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#--------Expected Output : ['Green', 'White', 'Black']
class removeElements:
    def specifiedList(self,List):
        print("Removeing List : ",List[1],List[2],List[3])
    def delToPrint(self,List):
        del (List[0],List[4],List[3])
        print("Del Function : ",List)
List=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
specifiedVal=removeElements()
specifiedVal.specifiedList(List)
specifiedVal.delToPrint(List)