n=int(input())
if n==1:
    ans=int(input())
    realans=[]
    for i in range (2, int(ans**(0.5))+1):
        if ans%i==0:
            realans.append(i)
            if i!=ans//i:
                realans.append(ans//i)
    realans.append(ans)
    realans.sort()
    print(*realans)
    exit()


A=[]
for i in range (n):
    p=int(input())
    A.append(p)
def gcd(a, b):
    if a*b==0:
        return a+b
    if a>b:
        return gcd(a%b, b)
    else:
        return gcd(a,b%a)
A.sort()
#print(a)
#print(A)
L=[]
for i in range(1,n):
    L.append(A[i]-A[i-1])
#print(L)
m= len(L)
ans=L[0]
for i in range(1,m):
    ans= gcd(ans,L[i])
#print(ans)
realans=[]
for i in range (2, int(ans**(0.5))+1):
    if ans%i==0:
        realans.append(i)
        if i!=ans//i:
            realans.append(ans//i)
realans.append(ans)
realans.sort()
print(*realans)



