n = int(input())

dic = {}
for i in range(n):
    dic[input()] = i

L= []
for _ in range(n):
    L.append(dic[input()])

# L = [1,3,4,0,2]
# L= [0,2,1,3,4]
# L = [0,1,2,3,4,7,5,6]
start = False
seen = [False] * n
turn = 0
cnt = 0
for i in range(n):
    if not L[i]:
        start = True
    if start:
        if L[i] == turn:
            turn +=1
            cnt +=1
        else:
            if L[i]<turn:
                continue
            for i in range(turn , L[i]):
                
                if seen[i]:
                    turn+=1
                else:
                    continue
            turn +=1
            cnt +=1

print(n-cnt)
            


