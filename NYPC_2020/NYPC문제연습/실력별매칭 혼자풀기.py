N = int(input())
S, K = list(map(int,input().split()))
score = [int(i) for i in input().split()]

queue=[]

for i in range(N):
    queue.append((i+1,score[i])) # 튜플로 저장

queue.sort(key = lambda c : abs(S-c[1]) + (0.5 if S<c[1] else 0))



new = []

for i in range(K):
    new.append(str(queue[i][0]))

print(new)
print(" ".join(new[:K]))

'''
for i in range(K):
    print(queue[i][0], end=' ')




즉석으로 함수 만들어서 바꾸고 리턴하고 싶을 때 람다 쓴다.

if, else 람다에서 한방에 쓰는 법

튜플로 묶어서 리스트에 넣기 : x,y 좌표 핸들 가능

튜플로 묶은 애들 중 몇번쨰 원소만 빼오는 코드는 이중리스트처럼 보인다.
'''
'''
5
60 3
20 80 100 40 10
'''
