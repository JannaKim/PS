a= input()
a=a.split(' ')
A=int(a[0])
B=int(a[1])
V=int(a[2])
ans = 1
V  = V - A

X = A - B

if V % X==0:
    ans += V // X

elif V % X!=0:

    ans += V // X + 1 


print(ans)