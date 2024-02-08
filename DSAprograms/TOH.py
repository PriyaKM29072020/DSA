def TOH(N,src,dest,temp,resList):
    if N==1:
        resList.append([src,dest])
        return resList
    TOH(N-1,src,temp,dest,resList)
    TOH(1,src,dest,temp,resList)
    return TOH(N-1,temp,dest,src,resList)


resList=TOH(4,'A','B','C',resList=list())
print(resList,"===")