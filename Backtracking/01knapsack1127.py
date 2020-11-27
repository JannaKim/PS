from functools import cmp_to_key as cmp
N, K = map(int, input().split())
wv=[]
cp=[]
for i in range(N):
    wv.append(tuple(map(int, input().split())))
    cp.append((wv[i][1]/wv[i][0], i))

cp.sort(key= cmp(lambda a,b: wv[b[1]][0]-wv[a[1]][0] if a[0]==b[0] else a[0]-b[0]), reverse=True)
print(cp)

#가성비가 같다면 가벼우운순으로
X=[-1]*N
mx=-1

def cost_performance(i,size):
    #print('cp')
    #print(i,size)
    s=size
    cnt=i
    ans=0
    for _cp, idx in cp:
        if idx>=cnt:
            if wv[idx][0]>=s:
                ans+=_cp*s
                #print('다채움', ans)
                return ans
            elif s>=0:
                s-=wv[idx][0]
                ans+=wv[idx][1]
                #print('ans줄임',ans)
    #print('다채움', ans)
    return ans





def knapsack(i,size):
    global mx
    global X
    if i>=N or size<=0:
        return
    accum = sum([(wv[j][1] if X[j]==1 else 0) for j in range(i)]+[0])
    #print(i,'전까지 accum',accum)

    if wv[i][0]<=size:
        #print(f'{wv[i][0]}<={size}')
        B = cost_performance(i+1,size-wv[i][0])
        if accum + wv[i][1] + B >mx: 
            X[i]=1
            mx = max(accum+wv[i][1],mx)
            #print(X[:i+1], i+1, size-wv[i][0])
            knapsack(i+1,size-wv[i][0])

    B = cost_performance(i+1,size)
    if accum+B>mx:
        X[i]=0
        mx = max(accum,mx)
        #print(X[:i+1], i, size)
        knapsack(i+1,size)

knapsack(0,K)
print(mx)

'''
4 7
6 13
4 8
3 6
5 12
'''