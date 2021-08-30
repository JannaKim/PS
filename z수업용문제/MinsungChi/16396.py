a= int( input())
L=['.']*10000
for i in range(0,a):
    
    s= input()
    s = s.split(' ')
    for r  in range(int(s[0])-1, int(s[1])-1):
        L[r]=0
d=0
for j in range(0, 10000):
    if L[j]==0:
        d=d+1

print(d)
