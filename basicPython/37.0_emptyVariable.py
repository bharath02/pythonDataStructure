#  Write a Python program to empty a variable without destroying it.
#  ---------------Sample data: n=20, d = {"x":200}
#  ---------------Expected Output : 0 , {}
class emptyVariableDestroying:
    def variableEmptyVariable(self,number):
        print(type(number)())
numb1=20
numb2={"x":200}
obj=emptyVariableDestroying()
obj.variableEmptyVariable(numb1)
obj.variableEmptyVariable(numb2)