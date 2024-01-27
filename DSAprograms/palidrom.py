def isPalidrom(str,start,end):
    if start>=end:
        return True
    return str[start]==str[end] and isPalidrom(str,start+1,end-1)

def palidrom(str):
    n=len(str)
    result=isPalidrom(str,0,n-1)
    if result==True:
        print(str," is Palidrom")
    else:
        print(str," is not Palidrom")
#Calling above palidrom method to Test
palidrom("NitiN")
## op : NitiN  is Palidrom
palidrom("Priyanka")
## op: Priyanka  is not Palidrom
