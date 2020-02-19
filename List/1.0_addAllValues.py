# Write a Python program to sum all the items in a list.
class sumAllList:
    def addList(self,list):
        sum=0
        for i in range(len(list)):
            sum=sum+list[i]
        print("Sum of all Values in list : ", sum)
    def sumFun(self,list):
        valuSum=sum(list)
        print("Sum Value by Function : ", valuSum)
list=[2,22,33,55,5,10]
sumList=sumAllList()
sumList.addList(list)
sumList.sumFun(list)