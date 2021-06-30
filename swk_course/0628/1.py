from heapq import heappop, heappush
'''
적은순, 오래될수록
중복: 횟수만 증가
삭제: 0으로

6 2 7

게시된 지 가장 오래된 사진
'''

n = int(input())
m = int(input())
L =[*map(int, input().split())]
candi = [] # (횟수, 등록순, 학생번호)
regidate = {}
exis = {}
mx = 0
for j in range(m):
    stu = L[j]
    if stu not in exis or not exis[stu]: #없는 애면
        if mx == n: 
            while True:
                num, when, id = heappop(candi)
                if exis[id] == num:
                    break
            # 가장 오래되고 작은애 찾기
            exis[id] = 0
        else:
            mx += 1
        regidate [stu] = j
        heappush(candi, (1, j, stu))
        exis[stu] = 1

    else: # 있는 애면
        exis[stu] += 1
        heappush(candi, (exis[stu], regidate [stu], stu))
        

ans = []
while candi:
    num, when, id = heappop(candi)
    if exis[id] == num:
        ans.append(id)
    
print(*sorted(ans))