from functools import cmp_to_key as cmp
N, K = map(int, input().split())
w ,v = [],[]
cp= []
for i in range(N):
    a, b = map(int, input().split())
    w.append(a)
    v.append(b)
    cp.append((v[i]/w[i], i))

cp.sort(key=cmp(lambda a,b: w[b[1]]-w[a[1]] if a[0]==b[0] else a[0]-b[0]),reverse=True)

def greedy(i, size):
    s=size
    idx=0
    ans=0
    while s and idx<N:
        if cp[idx][1]<i:
            idx+=1
        else:
            if w[cp[idx][1]]>=s:
                ans+=cp[idx][0]*s
                return ans
            else:
                s-=w[cp[idx][1]]
                ans+=v[cp[idx][1]]
                idx+=1
    return ans

mx=-1
def knapsack(i,size,accum):
    global mx
    if i>=N or not size:
        return
    if w[i]<=size:
        B = greedy(i+1,size-w[i])
        if accum+ v[i]+ B>mx:
            mx=max(mx, accum+v[i])
            knapsack(i+1,size-w[i],accum+v[i])
    B=greedy(i+1,size)
    if accum+B>mx:
        knapsack(i+1,size,accum)
knapsack(0,K,0)
print(mx)
print(2**59)
'''
4 7
6 13
4 8
3 6
5 12
'''





