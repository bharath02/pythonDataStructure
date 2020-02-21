# Write a Python program to determine if variable is defined or not.
class determineVariableDefined:
    def determineVariableDefined(self):
        try:
            x=1
        except NameError:
            print("Variable is Not defined ")
        else :
            print("Variable is defined :",x)

        try:
            y
        except NameError:
            print("Variable is Not defined ")
        else:
            print("Variable is defined :", y)
obj= determineVariableDefined()
obj.determineVariableDefined()
