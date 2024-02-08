def floorK(list,k):
    l=0
    r=len(list)-1
    f=False
    mid=0
    while(l<=r):
        mid=(l+r)//2
        if(list[mid]==k):
            l=r=mid
            break
        elif(list[mid]<k):
            l=mid+1
        else:
            r=mid-1
    if r<0:
        r=0
    print(list[r],l,r)

floorK([-5,2,3,6,9,10,11,15,18],12)

        
