def printDECR(N):
    if N==1:
        print(1)
        return
    print(N,end=",")
    printDECR(N-1)

#call function
printDECR(5)
