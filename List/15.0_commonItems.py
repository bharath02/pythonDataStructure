# Write a Program to find a common Items in two List
class commonItems:
    def twoListCommon(self,List1,List2):
        print("common Items : ",end="")
        for com1 in List1:
            for com2 in List2:
                if(com1==com2):
                    print(com1,end=" ")
List1=[1,2,3,4,"bharath",5,6,7,8,"naresh",9,0,"friends","suvam"]
List2=['a',1,2,4,45,16,7,8,19,10,15,16,79,"bharath","friends",'naresh','suvam']
commonIt=commonItems()
commonIt.twoListCommon(List1,List2)
