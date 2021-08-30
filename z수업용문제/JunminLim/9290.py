def check(a, b, c, p):
    cnt = 0
    if L[a // 3][a % 3] == p:
        cnt +=1
    if L[b // 3][b % 3] == p:
        cnt +=1
    if L[c // 3][c % 3] == p:
        cnt +=1

    if cnt >= 2:
        return True
    return False 
n=int(input())

for i in range (n):
    L=[]

    for j in range (3):
        a=input()
        L.append(list(a))
    p=input()
    G = [[0,3,6], [0,1,2], [0,4,8], [3,4,5],[1,4,7],[6,4,2],[6,7,8],[2,5,8]]
    for el in G:
     
        if check(el[0], el[1], el[2], p) == True:
          
            L[el[0] // 3][el[0] % 3] =p
            L[el[1] // 3][el[1] % 3] =p
            L[el[2] // 3][el[2] % 3] =p
    
    print(f'Case {i + 1}:')
    for j in L:
        print(*j,sep='')


'''
1
o--
-o-
xx-
x
'''