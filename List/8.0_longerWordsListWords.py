# Write a Python program to find the list of words that are longer than n from a given list of words.
class longerWord:
    def rangeWords(self,number,List):
        List1=List.split(" ")
        for word in List1:
            if(len(word)>number):
                print(word,end=" ")
List="welcome to Bridgelbz from differnet area or location a main problem is food cort or shops in mumbai"
number=int(input("Enter range for printing Words : "))
rangeof=longerWord()
rangeof.rangeWords(number,List)
