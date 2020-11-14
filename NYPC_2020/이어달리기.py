'''
1등 팀의 기록과 10초 미만으로 균형있게 팀 만들기 

입력 
5
00:30:00
00:31:00
00:32:00
00:33:00
00:50:00

출력
2
'''
N = int(input())
recs=[]
remainder=[]
all_cnts=[]
def find_max(low,remainder):
    cnt=0
    l,r=0,len(remainder)-1
    while(l<r):
        while(l<r):
            if remainder[l]+remainder[r]<low:#작으면 키우기
                l+=1
            elif remainder[l]+remainder[r]>=low+1000:#크면 줄이기
                r-=1
            else: #low< <low+1000이면 짝 발견, 걔네 빼고 다시 찾기
                #print(f"짝 발견{remainder[l]},{remainder[r]}")
                cnt+=1
                l+=1
                r-=1
                break
    return cnt




for i in range(N):
    best_rec=list(map(int,input().split(':')))
    recs.append(best_rec[0]*6000+ best_rec[1]*100 +best_rec[2])
recs.sort()
for i in range(0,N-1):
    for j in range(i+1,N):
        low=recs[i]+recs[j]
        remainder=recs[:]
        remainder.remove(recs[i])
        remainder.remove(recs[j])
        all_cnts.append(find_max(low, remainder)) # low로 가정한 애들 뺀 리스트
        #print(f"low짝은 {recs[i]}+{recs[j]}={low}")
#print(all_cnts)
print(max(all_cnts)+1)
