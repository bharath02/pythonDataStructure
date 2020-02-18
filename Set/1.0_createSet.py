class setCreating:
    def set(self,set1,set2):
        setx=set1&set2
        sety=set1|set2
        setz=set1-set2
        print(setx,sety,setz)
set1=set(['Bharath','Harika'])
set2=set(['Bharath','Aishwerya'])
setCreate=setCreating()
setCreate.set(set1,set2)
