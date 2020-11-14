from collections import deque
D = deque()
[D.append(i) for i in range(1,int(input())+1)]

while len(D)>1:
    D.popleft()
    card = D.popleft()
    D.append(card)

print(*D)
'''

Q = list(range(1,int(input())+1))

if len(Q)<=2:
    print(Q.pop())
else:
    while len(Q)>2:
        Q = Q[2:]+[Q[1]]

    print(Q[1])
'''