a = [int(i) for i in input().split()] #소공 스킬 사거리, 범위
N = int(input()) # 몬스터 마리수
X = a[0] # 스킬 쏜 곳의 좌표
R = a[1] # 스킬범위
ms=[]
mv=[]
for i in range(N):
    k = [int(j) for j in input().split()] # 몬스터의 위치랑 초마다 움직이는 만큼.
    # k[0] 몬스터 위치 좌표
    mv.append(k[1]) # 몬스터의 움직임
    ms.append(k[0])

def check(ms):
    cnt = N
    for j in range(N): #모든 몬스터 마릿수만큼 체크해보자
        #print(ms)
        if X-R<=ms[j] and ms[j] <=X+R:
            cnt-=1
    if cnt==0:
        
        return 1
    else:
        return 0

final_check=-1

final_check = check(ms)
if final_check==1: # 일단 지금 잘 있는지 보자
    print("T")
       
# not_again=[0]*N
break_while_loop=1
while(break_while_loop):
    for j in range(N): #모든 몬스터의 좌표 다음 초로 바꿔주자
        bf=ms[j]
        ms[j]+=mv[j]
        #print(bf, ms[j])

        if ms[j]<X-R and mv[j]<0:
            break_while_loop=0
            print("F")
            break
        if ms[j]>X+R and mv[j]>0:
            break_while_loop=0
            print("F")
            break


        

          #답이있긴한놈들을 점프시키자
    JUMP=[]
    for i in range(N):
            #왼쪽에 있는놈들
        if 0 not in mv:
            if (ms[i]<X-R and ms[i]+mv[i]<X-R):
                JUMP.append(int((X - ms[i])/ mv[i]))
                #print("ms",i,"를",int((X - ms[i])// mv[i]),"칸 점프")
            elif(ms[i]>X+R and ms[i]+mv[i]>X+R):#X+R<ms[j] 오른쪽놈들은
                JUMP.append(int(abs(X - ms[i])//mv[i]))
                #print("ms",i,"를",int((X - ms[i])/ mv[i]),"칸 점프")
                    
            
    #print("min(JUMP)",min(JUMP))               
    if len(JUMP)>0:
        #print("다가티 점프",min(JUMP))
        for i in range(N):
            ms[i]+=mv[i]*min(JUMP)
                
    #print("현재",ms)           
    final_check = check(ms)
    if final_check==1:
        print("T")
        break


 #                                  min(/mv)
#3 1  100                   3 -> + 1*t=  97  97 t= 49      49    52
#1 2  100                   1 -> + 2*t= 99   48             98   99
#300 -1 100 100-300 200    300->- 1*t = 200  100           49     251

