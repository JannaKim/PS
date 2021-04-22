n= int(input())
ans=1
for i in range(1,n+1):
    while not i%10 and i>=1e7:
        i//=10
    ans*=i%int(1e7)
    while not ans%10 and ans>=1e7:
        ans//=10
    ans%=int(1e7)
while not ans%10:
    ans//=10
print(ans % 10)

 