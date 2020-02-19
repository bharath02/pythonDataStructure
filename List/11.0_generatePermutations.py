#  Write a Python program to generate all permutations of a list in Python.
class generatePermutation:
    def permutationList(self,List):

        for i in range(len(List)):
            for j in range(len(List)):
                for k in range(len(List)):
                    if (List[i] != List[j] != List[k]):
                        if (List[i] != List[k]):
                            print("[",List[i], List[j], List[k],"]")
List=[1,2,3]
permu=generatePermutation()
permu.permutationList(List)