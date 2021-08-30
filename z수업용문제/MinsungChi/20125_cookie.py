


# def getLeftArm(y, x, n):
#     leng = 0
#     for g in range(x - 1, -1, -1): ## 거꾸로 돌리려면 (x-1, -1, -1)
#         if L[y][g] != '*':
#             break
#         leng += 1
#     return leng

# def getRightArm(y, x, n):
#     leng = 0
#     for g in range(x + 1, n): ## 거꾸로 돌리려면 (x-1, -1, -1)
#         if L[y][g] != '*':
#             break
#         leng += 1
#     return leng


# LA = getLeftArm(Y, X, n)
# RA = getRightArm(Y, X, n)




# def getLeftLeg(y, x):
#     ll = 0
#     for d in range(y,n):
#         if L[d][x]=='*':
#             ll+=1
#         else: break

#     return ll



# def getRightLeg(y, x): ## ???
#     rr = 0
#     for d in range(y,n):
#         if L[d][x]=='*':
#             rr+=1
#         else: break

#     return rr

# 

# LL = getLeftLeg(BY + 1, BX - 1)
# RL = getRightLeg(BY + 1, BX + 1)




def getMap(N):
    L = []
    for _ in range(N):
        L.append(list(input()))
    return L

def heart(L, n):
    for i in range(n):
        for j in range(n):
            if L[i][j] == '*':
                return (i + 1, j) ## () 두 개 이상이면 무조건 튜플로 묶어주기



def getWaist(y, x, n):
    leng = 0
    by, bx = 1, -1
    for g in range(y + 1, n): ## 거꾸로 돌리려면 (x-1, -1, -1)  ####################### 
        if L[g][x] != '*':
            break
        leng += 1
        by, bx = g, x
    # print(leng, by, bx)
    return (leng, by, bx)





def getLength(y, x, d):
    if d == 0 : # 왼쪽으로 가라는
        leng = 0
        for g in range(x , -1, -1): ## 거꾸로 돌리려면 (x-1, -1, -1)
            if L[y][g] != '*':
                break
            leng += 1
        return leng


    elif d == 1 : # 오른쪽으로 가라는

        leng = 0
        for g in range(x,  n): ## 거꾸로 돌리려면 (x-1, -1, -1)
            if L[y][g] != '*':
                break
            leng += 1
        return leng

    else:
        
        l = 0
        for d in range(y,n):
            if L[d][x]=='*':
                l += 1
            else: break

        return l




n = int(input())
L = getMap(n)
Y, X = heart(L, n)
LA = getLength(Y, X - 1, 0)
RA = getLength(Y, X + 1, 1)

W, BY, BX = getWaist(Y, X, n)

LL = getLength(BY + 1, BX - 1, 2)
RL = getLength(BY + 1, BX + 1, 2)

print(Y + 1, X + 1)
print(LA, RA, W, LL, RL)