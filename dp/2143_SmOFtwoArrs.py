t= int(input())
n= int(input())
L= [*map(int, input().split())]
dp=[0]*(n)

for i in range(n):
    dp[i]=(dp[i-1] if i-1>=0 else 0)+L[i]
dic={}
for i in range(n):
    for j in range(-1,i):
        tmp= dp[i]-(dp[j] if j>=0 else 0) 
        if tmp in dic:
            dic[tmp]+=1
        else:
            dic[tmp]=1
m= int(input())
L= [*map(int, input().split())]
dp2=[0]*(m)

for i in range(m):
    dp2[i]=(dp2[i-1] if i-1>=0 else 0)+L[i]

dic2={}
for i in range(m):
    for j in range(-1,i):
        tmp= dp2[i]-(dp2[j] if j>=0 else 0) 
        if tmp in dic2:
            dic2[tmp]+=1
        else:
            dic2[tmp]=1

cnt=0
A= []
for k1 in dic.keys():
    A.append(k1)
A.sort()

B= []
for k2 in dic2.keys():
    B.append(k2)
B.sort()

lo= 0
hi= 0
#print(A)
#print(B)
a, b= 0, len(A)-1
c, d= 0, len(B)-1
while a<=b and c<=d:
    print(a, b, c ,d)
    m1= (a+b)//2
    m2= (c+d)//2
    if A[m1]+B[m2]<t:
        if a!=b:
            a=m1+1 # 둘중하나만
        else:
            c=m2+1
    elif A[m1]+B[m2]>t:
        if a!=b:
            b=m1-1 # 둘중하나만
        else:
            d=m2-1
    else:
        cnt+=dic[A[m1]]*dic2[B[m2]]
        if a!=b:
            a=m1+1 # 둘중하나만
        else:
            c=m2+1
        if a!=b:
            b=m1-1 # 둘중하나만
        else:
            d=m2-1
        
        
'''
1 2 3 4 5
1 2 3 4
'''

print(cnt)

    

