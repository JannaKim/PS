import sys; input= lambda: sys.stdin.readline().rstrip()
import time
n, k= map(int, input().split())
belt=[[False, int(i)] for i in input().split()]

'''
1. rotate

2. for i in range(2*n-1, -1, -1):
if True and (i+1)%n!=0 and n-1 and i+1==False:
    i= False i+1=True 
3. if 0==Flase: 0==True * dur-=1 if not dur: cnt+=1
4. if cnt>=k: break
'''

step=1
cnt=0
start= 0
back= 2*n-1
while True:
    #print("STEP!P!P!!!", step)
    start= (start+2*n-1)%(2*n)
    # belt[start][0]=False 로봇 그대로 둬야함

    back= (back+2*n-1)%(2*n)
    #print('start', start, belt)
    half= (start+n)%(2*n)
    for i in range(start+n-1, start-1, -1):
        cur= (i+2*n)%(2*n)
        nxt= (i+1+2*n)%(2*n)
        #print(f'cur {cur} nxt {nxt}')
        #time.sleep(0.1)
        
        if belt[cur][0]:
            if (belt[nxt][0]==False and (belt[nxt][1]>0) or nxt==half): # 떨어질 위치의 애는 무조건 떨굼. 환장.
                belt[cur][0]=False
                belt[nxt][0]=True
                if nxt!=half:
                    belt[nxt][1]-=1
                if nxt!=half and not belt[nxt][1]: # 떨어진 로봇이면 내구도 감소 안시킴
                    cnt+=1
                #print(f'robot moved from {cur} to {nxt}', belt)
   
    belt[half][0]=False

    if belt[start][1]>0:
        belt[start][0]=True
        belt[start][1]-=1
        if not belt[start][1]:
            cnt+=1
        #print('robot toped on',start, belt)
    
    if cnt>=k:
        break
    step+=1

print(step)