gear = ''
for _ in range(4):
    gear += input()
gear = list(gear)

round = 8
half = 4
right = 2
left = 2 + half

def rightwards(id , chk):
    if id == 3:
        return chk
    while gear[id * 8 + right] != gear[id * 8 + right + round + half]:
        chk[id + 1]= True
        id += 1
        if id + 1 >= 4:
            break
    return chk

def leftwards(id , chk):
    if id == 0:
        return chk
    while gear[id * 8 + left] != gear[id * 8 + left - round - half]:
        chk[id - 1]= True
        id -= 1
        if id - 1< 0:
            break
    return chk

k = int(input())

for _ in range(k):
    id , dir = map(int , input().split())
    id -= 1
    chk = [False] * 4
    chk[id] = True
    chk = rightwards(id , chk)
    chk = leftwards(id , chk)
    #print(chk)

    for i in range(4):
        if chk[i]:
            loc = i * 8
            if dir > 0:
                if i % 2 == id % 2:
                    gear[loc : loc + round] = [gear[loc + round-1]] + gear[loc : loc + round-1]
                else:
                    gear[loc : loc + round] = gear[loc + 1 : loc + round] + [gear[loc]]
            else:
                if i % 2 == id % 2:
                    gear[loc : loc + round] = gear[loc + 1 : loc + round] + [gear[loc]]
                else:
                    gear[loc : loc + round] = [gear[loc + round-1]] + gear[loc : loc + round-1]

#print(gear)
ans = 0
score = 1

for i in range(4):
    if gear[i * 8] == '1':
        ans += score
    score *= 2

print(ans)



    