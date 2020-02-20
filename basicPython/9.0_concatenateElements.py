#  Write a Python program to concatenate all elements in a list into a string and return it.
class concatenateListString:
    def conListString(self,List):
        result = ''
        for element in List:
            result += str(element)
        print(result)
List=[1,2,3,4,5,6]
concat=concatenateListString()
concat.conListString(List)
