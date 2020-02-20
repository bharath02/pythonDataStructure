# Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.
# -------------Test Data : color_list_1 = set(["White", "Black", "Red"]) color_list_2 = set(["Red", "Green"])
# -------------Expected Output : {'Black', 'White'}
class notPresentcolors:
    def colorDiff(self,set1,set2):
        print(sorted(set1.difference(set2)))
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
diffCol=notPresentcolors()
diffCol.colorDiff(color_list_1,color_list_2)