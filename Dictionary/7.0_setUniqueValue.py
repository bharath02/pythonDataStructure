# Write a Python program to print all unique values in a dictionary.
#----------Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
#----------Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}

class setUniqueValue:
    def finddublicate(self,Data):
        unique={values for dic in Data for values in dic.values()}
        print(unique)

sampleData=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
uniqueValues=setUniqueValue()
uniqueValues.finddublicate(sampleData)
