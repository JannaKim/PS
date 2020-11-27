from functools import cmp_to_key as cmp
K = int(input())
n = int(input())
w = [int(i) for i in input().split()]
v = [int(i) for i in input().split()]

cp=[]
for i in range(n):
    cp.append((v[i]/w[i],i))

cp.sort(key = cmp(lambda a, b: w[b[1]]-w[a[1]] if a[0]==b[0] else a[0]-b[0]), reverse=True)

def cost_performance(i,size):
    s = size
    ans=0
    for _cp, idx in cp:
        if idx>=i:
            if w[idx]>=s:
                ans+= _cp*s
                return ans
            else:
                s-=w[idx] # 여기서 음수로 빠질 일이 없을 것이다
                ans+=v[idx]
    return ans # 가방 다 못채웠는데 더 넣을게 없으면
mx=-1
x=[-1]*n
def knapsack(i,size):
    global mx
    if i>=n or size<=0:
        return
    p = 0 # 새로운 방법!
    p += sum([v[j] for j in range(i) if x[j]==1])
    if w[i]<=size:
        B = cost_performance(i+1,size-w[i])
        if p+ v[i]+ B> mx:
            x[i]=1
            mx=max(p+v[i], mx)
            knapsack(i+1,size-w[i])

    B = cost_performance(i+1,size)
    if p+ B>mx:
        mx=max(mx,p) # 이번꺼 안가져가는건 예전에 이미 mx 처리 하지 않았을까?
        x[i]=0
        knapsack(i+1,size)

knapsack(0,K)
print(mx)

'''
10
5
7 2 10 2 4
46 19 30 49 11
'''

        


    