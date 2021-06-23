a=(input())
if a=='0':
    print(1)
    exit(0)
k=0
A=''
if len(a)<2:
    A='0'+a
else:
    A=a
c=0

while int(c)!=int(a):
    if len(A)<2:
        A = '0' + A

    b=str(int(A[0])+int(A[1]))

    if len(b)<2:
        b=str(0)+b
    c=A[1]+str(b[1])
    A=c
    k=k+1
print(k)


