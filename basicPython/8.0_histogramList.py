# Write a Python program to create a histogram from a given list of integers.
class histList:
    def histogram(self,List):
        for hist in List:
            output = ''
            times = hist
            while (times > 0):
                output += '*'
                times = times - 1
            print(output)

List=[4,6,2,10]
histL=histList()
histL.histogram(List)