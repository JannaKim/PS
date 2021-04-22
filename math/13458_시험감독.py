n= int(input())
A= [*map(int, input().split())]
b, c= map(int, input().split())

ans=0
for el in A:
    tmp=el-b
    if tmp<=0:
        ans+=1
    else:
        ans+=(el-b)//c+(1 if (el-b)%c else 0)+1
print(ans)