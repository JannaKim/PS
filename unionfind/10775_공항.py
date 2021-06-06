g= int(input())
p= int(input())
par= list(range(g + 1))

def find(v):
    if par[v] == v:
        return v
    par[v] = find(par[v])
    return par[v]

'''
https://www.acmicpc.net/source/24905106
파이썬 시간 1등 코드인데, 이렇게 짜면 부모를 가져오긴 해도 경로 압축이 안되지 않나요? 어째서 저보다 5배 빠른건지
def find(root):
    while root != tree[root]:
        root = tree[root]
        
    return root
'''
ans = 0

for i in range(1, p + 1):
    plane = int(input())

    
    if find(plane):
        find(par[plane] - 1)
        par[par[plane]] = par[par[plane] - 1]

    else: # 인풋 다 안받고 답 출력해도 에러가 안난다는 게 이해가 안가네요
        break
    ans += 1

print(ans)

'''
<<사유서>>
(1) 제출 문항 번호 : https://www.acmicpc.net/problem/10775
(2) 제출 링크 : http://boj.kr/b6cc856864354e03a318dbd1b7dad649
(3) 전체 코드 :

g= int(input())
p= int(input())
par= list(range(g+1))

def find(v):
    if par[v]==v:
        return v
    par[v]=find(par[v])
    return par[v]

def union(u, v):
    r1= par[u]
    r2= par[v]
    if r2<r1:
        r1, r2= r2, r1
    par[r2]=r1

for i in range(1,p+1):
    plane= int(input())
    find(plane)
    if par[plane]:
        par[plane]-=1
    else:
        print(i)
        break

(4) 문제 코드 :

    if par[plane]:
        par[plane]-=1

(5) 문제 사유 :
받은 plane의 부모를 plane-1의 부모로 바꿔줘야하는데 그냥 -1 썼다
두 노드의 유니온은 두 노드의 부모를 이어주는 것. 아래 노드에서 이어주면 그 노드가 부모갱신 일어나지 않은 상태일 수 있으므로
Find 한번씩 돌려줘야한다. 이 작업이 union 함수의 역할인데 union 함수 안쓰고 for문 내에서 작업하려다가 실수했다

위에꺼 아는데 유니온 파인드 풀때마다 항상 실수 한다. 거짓말 문제도 저래서 많이 틀렸었다
(6) 방지책 : 
함수로 빼기. 유니온 파인드 쓸 때마다 저부분 항상 조심하기 








'''