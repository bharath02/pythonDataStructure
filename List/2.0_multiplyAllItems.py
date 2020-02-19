# Write a Python program to multiplies all the items in a list.
class multipleAllElem:
    def valueMultiply(self,list):
        mult=1
        for i in range(len(list)):
            mult=mult*list[i]
        print(mult)
list=[2,22,33,55,5,10]
mulList=multipleAllElem()
mulList.valueMultiply(list)
