# Write a Python program to get numbers divisible by fifteen from a list using an anonymous function
class useAnonymousFunction:
    def numberDivisble_15(self,List):
        for num in range(len(List)-1):
            if(List[num]%15==0):
                print(List[num],end=" ")
        valu=tuple(filter(lambda x : x%15==0, List)) # useAnonymousFunction Lambda
        print("\n",valu)
List=[15,88,30,45,150,135,165,20,10,22,33]
div=useAnonymousFunction()
div.numberDivisble_15(List)

