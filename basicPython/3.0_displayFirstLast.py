#. Write a Python program to display the first and last colors from the following list.
#color_list = ["Red","Green","White" ,"Black"]
class displayFirstLast:
    def firstColorLast(self,colorList):
        print("firstColor : ",colorList[0],",  lastColor : ",colorList[-1])
colorList=["Red","Green","White" ,"Black"]
liCol=displayFirstLast()
liCol.firstColorLast(colorList)