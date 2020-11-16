from operator import itemgetter
N = int(input())
s = []
for i in range(N):
    w, h = map(int, input().split())
    s.append((w,h,i))
s.sort(key = itemgetter(0,1),reverse=True)

# L 몸무게 <= R 몸무게 일 땐 rank(L) >! rank(R)


# L 몸무게 == R 몸무게 일 땐 rank(L) == rank(R) 



# 몸무게 많은 순으로 정렬을 리스트S에 했을 때
# Si Sj (i<j, |j-i|=1) 의 관계만 알 수 있음
# |j|>i+1 인 Si Sj 관계 알 수 없음


# O n^2미만으로는 풀 수 없음을 증명
# 현재 등수를 알아낼 사람을 지정 O(n)  * 지정된 사람과 다른 모든 사람들을 비교하는 시간 O(n-1)

# N명중 임의의 두명 L, R 에 대해
# L 몸무게 > R 몸무게 이라고 |rank(L)-rank(R)|=1 이 항상 1이 아님  |rank(L)-rank(R)|>=1 임
# 몸무게만으로 정렬하거나 키만으로 정렬해서는 등수 얻을수없음
# 정렬을 못한다는 건 i (0<=i<N) 인 Si 의 등수를 구하기 위해 O(n) 이상의 작업을 해야한다는 뜻




ans=[0]*N

ans[s[0][2]]=1
print(s)
for idx, (L, R) in enumerate(zip(s,s[1:])):  
    if L[0]>R[0] and L[1]>R[1] :        
        ans[R[2]]=idx+2

    elif L[0]>R[0] and L[1]<=R[1] :        
        ans[R[2]]=ans[L[2]]

    elif L[0]==R[0]:
        ans[R[2]]=ans[L[2]]

print(*ans)



'''
# 각사람마다 자기 위에 몇명있는지 센다
for i in range(N):
    cnt=0
    for j in range(N):
        if i!=j:
            if s[j][0]>s[i][0] and s[j][1]>s[i][1]:
                cnt+=1
    ans[s[i][2]]=cnt+1

print(*ans)
  '''  
'''
9
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3
'''



    
    


