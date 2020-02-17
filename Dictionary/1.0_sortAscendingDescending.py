# Write a Python script to sort (ascending and descending) a dictionary by value.
class sortAscendingDescending:
    def ascendingOrder(self,set):
        ascend=sorted(set)
        print(ascend)
    def descendingOrder(self,set):
        desend = sorted(set, reverse=True)
        print(desend)
set={5,4,9,3,2,1,8,7,6}
obj=sortAscendingDescending()
obj.ascendingOrder(set)
obj.descendingOrder(set)
