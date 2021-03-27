mx=0
nm=0
for i in range(1,6):
    s=sum(list(map(int, input().split())))
    if mx<s:
        mx=s
        nm=i
print(nm,mx)
