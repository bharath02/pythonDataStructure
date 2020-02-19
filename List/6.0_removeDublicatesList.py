# write a Program for removing Dublicates From List
class removeDublicatesList:
    def dublicatesList(self,list1):
        new_list=set()
        for num in list1:
            new_list.add(num)
        print(list(new_list))

list1=[1,2,3,4,5,6,7,8,9,7,3,10]
removeList=removeDublicatesList()
print("original List : ", list1)
removeList.dublicatesList(list1)
