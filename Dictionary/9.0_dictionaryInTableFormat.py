# Write a Python program to print a dictionary in table format.
class dictTable:
    def convertTable(self,Set):
        for row in zip(*([key] + (value) for key, value in sorted(Set.items()))):
            print(*row, sep="   ")
Sets={"Col1":[1,2,3,4],"Col2":[5,6,7,8],"Col3":[9,0,1,2]}
table=dictTable()
table.convertTable(Sets)
