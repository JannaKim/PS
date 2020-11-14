#dp[max(seq[i])]: 카드 i장 구매를 위해 지불해야하는 금액 최대값
#seq[i]: (0,i+1)을 이용해 숫자 i를 만들 수 있는 모든 경우
N = int(input())
P=[0]
P+=[int(i) for i in input().split()]
seq=[0,[[P[1]]*N]]
remain=0
for i in range(2,N+1):
    seq.append([])
    a=0
    remain=i
    print(f"remain={remain}")
    for j in range(i,0,-1):# j 는 큰돌
        seq[i].append([j])
        remain=i-j
        print(f"큰 돌 {j} 넣음: remain={remain}")
        print(seq)
        if remain!=0:
            k=j
            while(remain):
                #seq[i].append([j])
                print(f"큰 돌:{j}, 다음 돌:{k}")
                while k>remain:
                    print("다음돌이 들어가긴 크므로 1 줄임")
                    k-=1
                print(f"a={a}")
                if k>0:
                    seq[i][a].append(k)
                    remain-=k
                else:
                    break
                    
                #seq[i].append()
            a+=1
        else:
            a+=1
                
            