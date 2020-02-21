# Write a Python program to extract single key-value pair of a dictionary in variables
class singleKeyValue:
    def ValueSinglePair(self,val):
        (val1,val2),=val.items()
        print( val1,'\n',val2)
val={'red':'green'}
obj=singleKeyValue()
obj.ValueSinglePair(val)