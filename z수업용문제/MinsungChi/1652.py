
'''
for i in range (0,n):
    found = False
    for t in range(0,n-1):
        if found == True and L[i][t] == '.':
            continue
        elif found == True and L[i][t] == 'X':
            found = False
        if found == False and L[i][t]=='.'and L[i][t+1]=='.':
            a+=1
            found = True
        #print(i , t ,a)

#[print(*el) for el in S]
for i in range (0,n):
    found = False
    for t in range(0,n-1):
        if found == True and S[i][t] == '.':
            continue
        elif found == True and S[i][t] == 'X':
            found = False
        if found == False and S[i][t]=='.'and S[i][t+1]=='.':
            b+=1
            found = True
        #print(i , t ,b)
'''


n = int(input())

L = []

for _ in range(n):
    L.append( input() )
S = list(map(list , zip(*L)) )[::-1]

for star in range(n , 1 , -1):
    for i in range(n):
        L[i] = L[i].replace( '.'*star , '*')

a , b = 0 , 0
for line in L:
    for el in line:
        if el =='*':
            a += 1

#[print(*el) for el in L]
#print()
for i in range(n):
    S[i] = ''.join(S[i])


for star in range(n , 1 , -1):
    for i in range(n):
        S[i] = S[i].replace( '.'*star , '*')

for line in S:
    for el in line:
        if el =='*':
            b += 1

#[print(el) for el in S]

print(a,b)       


#[print(*el) for el in S]

'''
6
..X...
....X.
......
......
......
......
'''