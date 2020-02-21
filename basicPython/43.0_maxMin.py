#  Write a Python function to find the maximum and minimum numbers from a sequence of numbers.
# ----------------------- Note: Do not use built-in functions.
class sequenceMaxMin:
    def maxValue(self,Number):
        print("Maximum Value : ", Number[-1])

    def miniValue(self, Number):
        print("Maximum Value : ", Number[0])
List=[2,4,6,8,10,12,14,16,18,20,22]
obj= sequenceMaxMin()
obj.maxValue(List)
obj.miniValue(List)