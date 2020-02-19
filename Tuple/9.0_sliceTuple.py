# write a program to Slice a tuple
class tupleSlice:
    def Slice(self,Tup):
        print(Tup[2:])
        print(Tup[:10])
        print(Tup[1:9])
        for tupl in range(1,len(Tup)-1,4):
            print(tupl,end=" ")

Tup=(1,2,3,4,5,6,7,8,9,10,11,12,13,14)
sli=tupleSlice()
sli.Slice(Tup)
