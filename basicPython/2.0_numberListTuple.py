# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
# --------------Sample data : 3, 5, 7, 23
# Output :
# --------List : ['3', ' 5', ' 7', ' 23']
# --------Tuple : ('3', ' 5', ' 7', ' 23')
class numberListTuple:
    def numberList(self,number):
        number=list(number)
        print(number)
    def numberTup(self,number):
        number1=tuple(number)
        print(number1)
number=3,5,7,23
convert=numberListTuple()
convert.numberList(number)
convert.numberTup(number)