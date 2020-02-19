#  Write a Python function that takes two lists and returns True if they have at least one common member.
class commonMember:
    def checkCommon(self,List1,List2):
        for Ls1 in List1:
            for Ls2 in List2:
                if(Ls1==Ls2):
                    return True
        else:
            return False

List1=["bharath",2,22,55]
List2=["harika",26,33,55]
List3=["Lella",32,36,38,37]
commonValue=commonMember()
Result=commonValue.checkCommon(List1,List2)
Result1=commonValue.checkCommon(List1,List3)

print(Result)
print(Result1)

