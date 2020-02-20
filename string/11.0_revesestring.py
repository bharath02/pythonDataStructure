# Write a Python program to reverse a string.
class reverseString:
    def strRev(self,String):
        for i in range(len(String)-1):
            val = String.split(" ")

        print(" ".join(val[::-1]))
sting="Mumbai is costly city then Bengaluru and Bengaluru is costly then Hyderabad"
print(sting)
rev=reverseString()
rev.strRev(sting)