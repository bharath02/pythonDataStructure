#  Write a python program to check whether two lists are circularly identical.
class circularlyIdentical:
    def checkTwoList(self,List1,List2):
        print(' '.join(map(str, List2)) in ' '.join(map(str, List1 * 2)))
List1=[10,10,0,0,10,]
List2=[10,0,0,10,10]
circl=circularlyIdentical()
circl.checkTwoList(List1,List2)