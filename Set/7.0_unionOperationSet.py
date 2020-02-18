# Write a Python program to create a union of sets.
class unionOfSet:
    def unionValues(self,set1,set2):
        setUnion=set1|set2
        print(setUnion)
    def functionUnion(self,set1,set2):
        setUnion1=set1.union(set2)
        print(setUnion1)
set1={'Bharath','Naresh','Suvam','Shiva','Jayenth','Punnith','Sai'}
set2={'Harika','Neelima','Kavya','Varshini','Priyanka','Pushpa','Srilekha','Akhila'}
unionOpera=unionOfSet()
unionOpera.unionValues(set1,set2)
unionOpera.functionUnion(set1,set2)