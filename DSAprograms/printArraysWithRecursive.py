def printHelper(arr,n):
    if(n==0):
        return 
    printHelper(arr,n-1)
    print(arr[n-1])


#call func
printHelper([1,2,3,4],4)    