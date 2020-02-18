#  Write a Python program to count the values associated with key in a dictionary.
#---------Sample data: = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
#---------Expected result: Count of how many dictionaries have success as True
class countAssociatedKey:
    def valuesCount(self,Data):
        print("Key Value Success count in dict : ",sum(key['success']for key in Data))
data = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
success=countAssociatedKey()
success.valuesCount(data)