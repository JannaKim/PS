n= int(input())

cnt=0
while n>2:
    cnt+=1
    if n%3>=1:
        n-=1
        continue
    if not n%3:
        n//=3
if n!=1:
    cnt+=n-1
print(cnt)
