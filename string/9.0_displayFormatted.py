# Write a Python program to display formatted text (width=50) as output.
import textwrap
class display50Width:
    def widthDisplay(self,String):
        print(textwrap.fill(String, width=1500))
String="Hi! Checking text Width...."
print("Normal String : ",String)
textWrap=display50Width()
textWrap.widthDisplay(String)