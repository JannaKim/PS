n, l= map(int, input().split())
L= [*map(int, input().split())]
L.sort()
tape=0
cnt=0
for el in L:
    if tape<el:
        cnt+=1
        tape=el-0.5+l
print(cnt)
