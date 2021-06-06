n = int(input())
edge = [ [] for _ in range(n + 1)]
cross_edge = [ [] for _ in range(n + 1)]
ans = []
for i in range(1 , n + 1):
    tmp = int(input())
    if tmp == i:
        ans.append(i)
    edge[i].append(tmp)
    cross_edge[tmp].append(i)


stc = []
cross_chk = [False] * (n + 1)
def cross_po(v):
    for v2 in cross_edge[v]:
        if not cross_chk[v2]:
            cross_chk[v2] = True
            cross_po(v2)
    stc.append(v)


for i in range(1 , n + 1):
    cross_edge[i].sort()
    edge[i].sort()

for i in range(1 , n + 1):
    if not cross_chk[i]:
        cross_chk[i] = True
        cross_po(i)

chk = [False] * (n + 1)

def po(v):
    stack = []
    stack.append(v)
    for v2 in edge[v]:
        #print('->' , v2)
        if not chk[v2]:
            chk[v2] = True
            stack += po(v2)
    return stack

#print(stc)
while stc:
    ths = stc.pop()
    if not chk[ths]:
        #print(ths)
        chk[ths] = True
        tmp = po(ths)
        if len(tmp) > 1 :
            #print(ths , tmp)
            ans += tmp
print(len(ans))
ans.sort()
print(*ans , sep = '\n')