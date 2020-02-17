#Write a Python program to reverse the order of the items in the array.
class reverseOrder:
    def itemReverse(self,list):
        print("[",end=" ")
        for i in range(len(list)-1,0,-1):
            print(list[i],end=",")
        print("]")
list=[10,22,55,33,2,5]
obj=reverseOrder()
obj.itemReverse(list)
