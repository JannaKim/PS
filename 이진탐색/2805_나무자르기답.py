'''
4 7
20 15 10 17

15
'''
N, M = list(map(int, input().split()))
tree = [int(i) for i in input().split()]

def chop(cutter):# 받은 매개변수로 잘라보기
        return sum([int(i)-cutter for i in tree if i>=cutter])


def binary_search(a,b):
    m  = (a+b)//2
    if (b-a)<=1: # 여기 설정하는 게 제일 어려움
        #print(f"{a}, {b}두 개 남음")
        if chop(b)>=M and chop(a)>=M: return b #두 개 남았는데 둘다 답이 되면 더 큰 b가 답이다
        else: return a
    elif chop(m) > M: 
        #print(f"m={m}이면 {chop(m)}가져갔다: 답보다 아래로 잘 잘랐다 답은{m} 과{b}사이다 아래로 잘랐는데 바운더리 1이면?")
        return binary_search(m,b) 
    elif chop(m) < M:
        #print(f"{m}이면 {chop(m)}가져갔다: 답보다 위로 잘랐다 절대 답 안됨! 답은{a} 과{m-1}사이다")
        return binary_search(a,m-1)
    else:
        return m
        
print(binary_search(0,max(tree)))  # print(binary_search(0,int(1e9))) ??이해 또 안됨