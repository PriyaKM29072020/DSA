def printINC(N):
    if N==1:
        print(1,end=",")
        return
    printINC(N-1)
    print(N,end=",")
printINC(5)