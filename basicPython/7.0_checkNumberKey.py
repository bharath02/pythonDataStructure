#  Write a Python program to check whether a specified value is contained in a group of values.
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False
class checkNumber:
    def specifiedValue(self,List,Key):

        if Key in List:
            print(True)
        else:
            print(False)
List=[1,5,8,3]
check=checkNumber()
check.specifiedValue(List,Key=3)
check.specifiedValue(List,Key=-1)



