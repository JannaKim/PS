from sys import*
#N, M, S: 다른시험개수, 필요한시간, 총시간
N, M, S = map(int, input().split())
sd=[]
for _ in range(N):
    a, b = map(int, input().split()) 
    sd.append((a,a+b)) # (수업 시작 시간, 수업끝시간+1)

sd.sort(key = lambda x:x[0])

ans=False
if sd[0][0]>=M: # 셰줄앞
        print(0)
        exit()
for A,B in zip(sd,sd[1:]): # A:비는 시작시간, B:뒷 수업 시작시간
    if B[0]-A[1]>=M:
        print(A[1])
        ans=True
        break
if ans==False:
    if S-sd[-1][1]>=M: # 셰줄뒤
        print(sd[-1][1])
    else:
        print(-1)

'''
2 3 5
0 1
1 4
'''

'''
sch = [0]*(S+1+int(1e9))
for start, dur in sd:
    for i in range(dur):
        sch[start+i]=1
#print(sch)
cnt=0
for i in range(0,S+1):
    if sch[i]==0:
        cnt+=1
    else:
        cnt=0
    if cnt==M:
        print(i-M+1)
        exit()
print(-1)
'''
'''
2 3 5
0 1
1 4
'''