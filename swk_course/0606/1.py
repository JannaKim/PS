n = int(input())
mp = [ list(input()) for _ in range(n)]


def Chk(y , x , s , el):
    for i in range(y , y + s):
        for j in range(x , x + s):
            if mp[i][j] != el:
                return False
    return True
 

def rec(y , x , side):
    half = side // 2

    for el in ('0' , '1'):
        if Chk(y , x , side,  el):
            return str(el)

    tmp = "(" 
    for lo , hi in ( (y , x) , (y , x + half),  (y + half , x) , (y + half , x + half)):

        tmp += rec(lo , hi , half) 
    tmp += ")"




    return tmp

print(rec(0 , 0 , n))
