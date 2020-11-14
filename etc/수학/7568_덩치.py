from functools import cmp_to_key as cmp
N = int(input())
s = []
for i in range(N):
    w, h = map(int, input().split())
    s.append((w,h,i))
s.sort(key = cmp(lambda a, b: a[1]-b[1] if a[0]==b[0] else a[0]-b[0]),reverse=True)
ans=[0]*N
rank=1
jumped=0

for WH1, WH2 in zip(s,s[1:]+[(0,0,0)]):

    if WH1[0]>=WH2[0] and WH1[1]>WH2[1] :
        
        ans[WH1[2]]=rank
        rank+=jumped
        rank+=1
        jumped=0
    else: # WH1[1]<=WH2[1]
        ans[WH1[2]]=rank
        jumped+=1

print(*ans)
'''
5
55 185
58 183
88 186
60 175
46 155
'''



    
    


