import sys; input= lambda: sys.stdin.readline().strip();r= range
ori, bl, ans= [], [], 0
N, M= map(int,input().split())
for _ in r(N): ori+=list(map(int,input().split())) # one dimensional axis
for i in r(N*M):
	if ori[i]==0: bl.append(i)
h=len(bl)

for i in r(h-2):
    for j in r(i+1,h-1):
        for k in r(j+1,h):
            walled, q=ori[:], []
            walled[bl[i]], walled[bl[j]], walled[bl[k]]= 1, 1, 1 # put 3 wall in a copied map

            # collect virus
            for idx in r(N*M):
                if walled[idx]==2: q.append(idx)

            # spread virus
            for v in q:
                if walled[v]==2:
                    U,R,D,L= v-M, v+1, v+M, v-1 # one dimensional axis
                    if walled[U]==0and U>=0: walled[U]=2; q.append(U)
                    if R<N*M and walled[R]==0and R%M: walled[R]=2; q.append(R)
                    if D<N*M and walled[D]==0: walled[D]=2; q.append(D)
                    if walled[L]==0and L%M!=M-1: walled[L]=2; q.append(L)
        
            s=walled.count(0) # <- ?
            ans= max(s, ans)
print(ans)