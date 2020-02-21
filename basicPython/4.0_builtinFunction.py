# Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
# -----------Sample function : abs()
# -----------Expected Result : mat
# -----------abs(number) -> number
# Return the absolute value of the argument.
class builtinFunction:
    def builtFun(self,numb):
        numb=abs(numb)
        print(numb)
        print(numb.__doc__)
        print(abs.__doc__)
num=-90
absNumb=builtinFunction()
absNumb.builtFun(num)