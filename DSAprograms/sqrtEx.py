def sqrtEx(n):
    ans=0
    l=0
    r=n
    while(l<=r):
        mid=(l+r)//2
        if(mid**2<=n):
            ans=mid
            l=mid+1
        else:
            r=mid-1

        
    return ans

print(sqrtEx(24))