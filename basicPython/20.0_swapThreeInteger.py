# Write a Python program to sort three integers without using conditional statements and loops
class sortThreeIntegeger:
    def sortValues(self,numb1,numb2,num3):
        min1=min(numb1,numb2,num3)
        max1=max(numb1,numb2,num3)
        mid1=numb1+numb2+num3-min1-max1
        print("Sorted Values are : ", min1,mid1,max1)
num1,num2,num3=5,10,2
sortedVal=sortThreeIntegeger()
sortedVal.sortValues(num1,num2,num3)
