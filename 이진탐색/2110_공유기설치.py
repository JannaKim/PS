N, C =map(int,input().split())

L = [int(input()) for _ in range(N)]
R1=False
min_list=[]
def mx(A):
    global R1
    if len(A)==1:
        return A[0]
    elif len(A)==len(L): # round 1
        R1=True

    B = []
    for x, y in zip(A[::2], A[1::2]+[0]):
        if x>= y:
            B.append(x)
            if R1:
                min_list.append(y)
        else:
            B.append(y)
            if R1:
                min_list.append(x)
    R1=False
    return mx(B)

def mn(A):
    if len(A)==1:
        return A[0]

    B = []
    for x, y in zip(A[::2], A[1::2]+[(int(1e9))]):
        if x<= y:
            B.append(x)
        else:
            B.append(y)

    return mn(B)   

last_house = mx(L)
del min_list[-1]
first_house = mn(min_list)

house=[False]*(last_house+1)
for el in L:
    house[el]=True

# 집 놓기 끝



def install(R, n, first, last):
    #print(f'R: {R}')
    cnt=n-1
    #print(f'{cnt} 개 설치하기.')
    last_installed=first

    while cnt:
        if last_installed+R >last:
                #print('설치 불가능')
                return False
        for i in range(last_installed+R,last+1):
            #print(f'house {i}')
            if house[i]:               
                cnt-=1
                last_installed=i
                #print(f'설치, {cnt}개 남음')
                break
            if i==last and cnt!=0: # 공유기 설치 다 못함
                #print('다 설치못함: 실패')
                return False
            
    return True

def BS(a, b):
    global C
    if b<=a:
        return a
    elif b-a==1:
        if install(b,C,first_house,last_house):
            return b
        else:
            return a
    else:
        m = (a+b)//2
        if install(m,C,first_house,last_house):
            return BS(m,b)
        else:
            return BS(a,m-1)

print(BS(1,int(1e9)))




   

