#  Write a Python program to unpack a tuple in several variables
class unpackVariable:
    def severalVariable(self,Tup):
        tup1,tup2,tup3=Tup
        print(tup1+tup2+tup3)
tup=(1,2,3)
tuplel=unpackVariable()
tuplel.severalVariable((tup))