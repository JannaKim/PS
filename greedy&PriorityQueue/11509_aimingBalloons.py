n= int(input())
L= [*map(int, input().split())]

dic={}
arr=0
for i in range(n):
    if L[i] not in dic:# 쏠 화살 없으면 새로 만들어서 쏨
        arr+=1
        if L[i]-1 in dic:
            dic[L[i]-1]+=1 # dd
        else:
            dic[L[i]-1]=1
        
    else: # use existing arrow
        if dic[L[i]]==1:
            del dic[L[i]]
        else:
            dic[L[i]]-=1 # grade down
        if L[i]-1 in dic:
            dic[L[i]-1]+=1
        else:
            dic[L[i]-1]=1
print(arr)