a = input() #개수와 안되는 조합
a = a.split(' ')
w = int(a[0])# 아이스크림 개수
d = int(a[1])# 안되는 조합 개수
q = 0 #최종 답
H = {}# 안되는 조합 넣는 곳
for j in range(0,d): # 안 되는 조합 받기
    v = input()
    n1, n2 = map( int, v.split(' ')) # 조합들 n1, n2 에 넣기(map는 전체를 바꾸는 것)
    if n2 < n1:# 순서 바꾸기
        n1, n2 = n2, n1
    H[ (n1, n2) ] = True

L = list(range(1, 1 + w)) 
for i in range(w):  #경우의 수 고르기
    for j in range(i + 1, w):
        for k in range(j+1, w):
            set1 = (L[i], L[j])
            set2 = (L[j], L[k])
            set3 = (L[i], L[k]) 
            if set1 not in H and set2 not in H and set3 not in H:# 세트 있는 거를 비교
                q += 1#점수/값 1 올리기
            
print(q)# 최종 값
