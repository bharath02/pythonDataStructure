#  Write a Python program to get the smallest number from a list.
class smallestNumber:
    def minimumNumber(self,list):
        for num in range(len(list)-1):
            for sort in range(len(list)-num-1):
                if(list[sort]>list[sort+1]):
                    list[sort],list[sort+1]=list[sort+1],list[sort]

        print("smallest Number is : ", list[0])
    def functionMin(self,list):
        minVal=min(list)
        print("Smallest value with function : ", minVal)
    def sortMin(sel,list):
        sortVal=sorted(list)
        print("sorted to find a list small value : ",list[0])
list=[2,22,33,55,5,10]
smallvalue=smallestNumber()
smallvalue.minimumNumber(list)
smallvalue.functionMin(list)
smallvalue.sortMin(list)