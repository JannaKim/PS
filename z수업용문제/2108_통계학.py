import sys; sys.setrecursionlimit(1000000)
from random import*
n= int(input())
L=[]
for _ in range(n):
    L.append(int(input()))

#random()# 0.0~1.0', 'randint(a,b)', 'shuffle(data)'
'''
for _ in range(5000):
    L.append(randint(-4000, 4000))
'''
def mid(start, end, k):
    #print(start, end, k)
    if start>=end:
        return L[start]
    i=start+1
    j=end
    p=start
    while i<=j:
        while i<=end and L[i]<=L[p]:
            i+=1
        while L[j]>L[p]:
            j-=1
        if i<j:
            L[i], L[j]= L[j], L[i]
        #print(L)
    L[p], L[j]= L[j], L[p]
    #print(L)
    #print(j-start)
    if j-start==k:
        return L[j]
    elif j-start>k:
        return mid(start, j, k)
    else:
        return mid(j+1, end, k-j+start-1)
raw= sum(L)/float(n)
#print('raw',raw,abs(raw))
a= 1
if raw<0:
    a=-1
#print('av',int(abs(raw)+0.5)*a)
#print(int(sum(L)/float(n)+0.5))
print(mid(0,n-1,(n-1)//2))


#L.sort()
#print()
#print('**',L[2499])
mx=0
dic={}
ans=[]
for el in L:
    if el in dic:
        dic[el]+=1
    else:
        dic[el]=1
    if mx<dic[el]:
        ans=[el]
        mx=dic[el]
    elif mx==dic[el]:
        ans.append(el)
ans.sort()
if len(ans)>1:
    print(ans[1])
else:
    print(ans[0])
print(max(L)-min(L))
