# Write a Python program to create a symmetric difference.
class symmetricDiff:
    def differenceSymm(self,set1,set2):
        symmDif=set1^set2
        print(symmDif)
    def functionSymmDiff(self,set1,set2):
        symmDif1=set1.symmetric_difference(set2)
        print(symmDif1)
set1 = {'a', 'e', 'i', 'o', 'u', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'l'}
set2 = {'i', 'l', 'u', 4, 3, 1, 'v', 'h', 'b', 'z'}
syDf=symmetricDiff()
syDf.differenceSymm(set1,set2)
syDf.functionSymmDiff(set1,set2)