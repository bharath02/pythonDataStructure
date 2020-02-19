# write a Program to remove Item from Tuple
class removeItemTuple:
    def itemTupleRemo(self,Tup):
        val=list(Tup)
        val.remove(4)
        print(tuple(val))
Tup=(1,2,3,4,5,6,7)
tupleset=removeItemTuple()
tupleset.itemTupleRemo(Tup)