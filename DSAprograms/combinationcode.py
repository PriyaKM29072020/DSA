count=0
def funComb(n,r):
    #print(n,r)
    if r==0 or n==r:
        return 1
    print(n,r)
    return funComb(n-1,r)+funComb(n-1,r-1)

#calling funComb
print(funComb(8,3)*2)
