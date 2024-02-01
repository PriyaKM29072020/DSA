k=2
n=5
op=[]
# for i in range(1,n+1):
#     print(i)
#     a=[]
#     for j in range(i+1,n+1):
#         a.append(i)
#         a.append(j)
#     op.append(a)
# print(op)

""" for i in range(1,n+1):
    for j in range(i+1,n+1):
        
        for l in range(k):
            arr=[]
    
            arr.append(i)
            arr.append(j)
        op.append(arr)
print(op)
 """
def funCombList(n,k):
    c:list[list[int]]=[]
    s:list[int]=[]
    def fun(i:int):
        if(len(s)==k):
            c.append(s[:])
            return
        if i==n+1:
            return
        else:
            s.append(i)
            fun(i+1)
            s.pop()
            fun(i+1)
    fun(1)
    return c

print(funCombList(5,2))   