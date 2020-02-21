# Write a Python program to convert an integer to binary keep leading zeros.
class binaryKeepZero:
    def leadingBinaryZero(self,Val):
        print(format(Val,'08b'))
        print(format(Val,'010b'))
val=50
obj=binaryKeepZero()
obj.leadingBinaryZero(val)
