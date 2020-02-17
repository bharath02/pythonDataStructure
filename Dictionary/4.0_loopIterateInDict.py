# Write a Python program to iterate over dictionaries using for loops.
class loopIterateInDict:
    def valueIterate(self,set):
        for name,value in set.items():
            print(name,":", set[name])
names={1:"Naresh",2:"Bharath",3:"Suvam",4:"Sandeep",5:"Huthash"}
obj=loopIterateInDict()
obj.valueIterate(names)
