# Write a Python program which accepts the user's first and last name and
# print them in reverse order with a space between them.
class nameRev:
    def reverseFirstLast(self,firstName,lastName):
        name= firstName+" "+lastName
        print(name)
        name1=lastName+" "+firstName
        print(name1)
        for i in range(len(name)-1,-1,-1):
            print(name[i],end=" ")
firstName="Bharath"
lastName="Kumar"
revName=nameRev()
revName.reverseFirstLast(firstName,lastName)

