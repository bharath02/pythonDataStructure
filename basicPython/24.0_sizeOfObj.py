# Write a Python program to get the size of an object in bytes.
import sys
class sizeObj:
    def objByte(self,str1,str2,str3):
        print("Memory size of '"+str1+"' = "+str(sys.getsizeof(str1))+ " bytes")
        print("Memory size of '"+str2+"' = "+str(sys.getsizeof(str2))+ " bytes")
        print("Memory size of '"+str3+"' = "+str(sys.getsizeof(str3))+ " bytes")
str1 = "one"
str2 ="four"
str3 = "three"
siz=sizeObj()
siz.objByte(str1,str2,str3)