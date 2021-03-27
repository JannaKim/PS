n, l = map(int, input().split())
s = list(map(int, input().split()))
s.sort()
loc = s[0]-1+l # loc.5
cnt=1
for el in s[1:]:
    if el<=loc:
        pass
    else:
        cnt+=1
        loc=el-1+l

print(cnt)