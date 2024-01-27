def countDigits(num):
    if num==0:
        return 0
    return 1+countDigits(num//10)
print(countDigits(123))

# def countDigits(num):
#     count=0
#     while(num>0):
#         count=count+1
#         num//=10
#     return count
# print(countDigits(123))