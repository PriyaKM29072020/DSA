moves=0
def TOH(N,src,dest,temp):
    global moves
    if N==0:
        return 
    TOH(N-1,src,temp,dest)
    moves=moves+1
    print(moves,"moves===")
    TOH(N-1,temp,dest,src)


TOH(4,'A','B','C')

