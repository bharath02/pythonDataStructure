#  Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). Sample Dictionary ( n = 5) :
#     Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
class scriptGenerator:
    def valueSquare(self,Number):
        generator={x : x*x for x in range(1,Number+1)}
        print(generator)
number=5
obj = scriptGenerator()
obj.valueSquare(number)
