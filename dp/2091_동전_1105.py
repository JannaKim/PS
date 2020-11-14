# 1<= X <=10000
# 0<= A B C D <=10000
from copy import *
#from time import*
#start = time()
X, A, B, C, D = map(int, input().split())

# 이따 로그로 바꾸기
bag = [] # (개수, 금액, 쓴 동전)
def binary_pack(num, unit, idx):
    n = len(bin(num)[2:])
    if num==2**n-1:
        for i in range(n):
            bag.append((2**i*unit, 2**i, idx))
    else:
        for i in range(n-1):
            bag.append((2**i*unit, 2**i, idx))
        num -= 2**(n-1)-1
        remain = bin(num)[2:]
        for deg, i in enumerate(remain[::-1]):
            if int(i):
                bag.append((2**deg*unit, 2**deg, idx))
binary_pack(A, 1, 0)
binary_pack(B, 5, 1)
binary_pack(C, 10, 2)
binary_pack(D, 25, 3)
#[print(bag[i],end= (' ' if (i+1)%10 else '\n' )) for i in range(len(bag))]

#L[j][0]: 0~i번째 동전까지 내서 j원을 맞출 때 낼 수 있는 최대 동전 개수
#L[j][1]: 사용한 동전별 개수 [penny, dime, nickle, quarter]


L=[]
[L.append([0,[0,0,0,0]]) for _ in range(X+1)]

# 1차면 [:], 2차 이상이면 deepcopy
M=[]
[M.append([0,[0,0,0,0]]) for _ in range(X+1)]


Len_Of_bag = len(bag)
for i in range(Len_Of_bag):
    for j in range(X+1):
        if not i%2: #짝
            if bag[i][0]<j:
                if L[j-bag[i][0]][0] !=0 and L[j-bag[i][0]][0] + bag[i][1] > L[j][0]: # 더 많은 동전 낼 수 있다면
                        M[j][0] = L[j-bag[i][0]][0] + bag[i][1]
                        a = [0,0,0,0]
                        a[bag[i][2]]+=bag[i][1] # 현재 받은 동전에 해당되는 개수

                        for idx,k in enumerate(L[j-bag[i][0]][1]):
                            a[idx]+=k
                        M[j][1] = a                
                else:
                    M[j] = deepcopy(L[j]) 

            elif bag[i][0]==j: # 동전 하나로 값 j가 채워진 게
                if bag[i][1]>L[j][0]: # 현재 dp보다 더 많은 동전을 내는 거라면
                    M[j][0] = bag[i][0]

                    a = [0,0,0,0]
                    a[bag[i][2]]+=bag[i][1] #쓴 동전의 인덱스에 해당하는 곳에 개수 더하기
                    M[j][1] = a
                else:
                    M[j] = deepcopy(L[j]) 

            else:
                #print(f'L[{j}]={L[j]}')
                M[j] = deepcopy(L[j])
        else: #홀
            if bag[i][0]<j:
                if M[j-bag[i][0]][0] !=0 and M[j-bag[i][0]][0] + bag[i][1] > M[j][0]: # 더 많은 동전 낼 수 있다면
                        L[j][0] = M[j-bag[i][0]][0] + bag[i][1]
                        a = [0,0,0,0]
                        a[bag[i][2]]+=bag[i][1] # 현재 받은 동전에 해당되는 개수

                        for idx,k in enumerate(M[j-bag[i][0]][1]):
                            a[idx]+=k
                        L[j][1] = a                
                else:
                    L[j] = deepcopy(M[j]) 

            elif bag[i][0]==j: # 동전 하나로 값 j가 채워진 게
                if bag[i][1]>M[j][0]: # 현재 dp보다 더 많은 동전을 내는 거라면
                    L[j][0] = bag[i][0]

                    a = [0,0,0,0]
                    a[bag[i][2]]+=bag[i][1] #쓴 동전의 인덱스에 해당하는 곳에 개수 더하기
                    L[j][1] = a
                else:
                    L[j] = deepcopy(M[j]) 

            else:
                #print(f'L[{j}]={L[j]}')
                L[j] = deepcopy(M[j])           

        #print(dp[i][j])

if Len_Of_bag:
    if not (Len_Of_bag-1)%2: # N-1이 짝수면
        print(*M[X][1])
    else:
        print(*L[X][1])
    
else:
    print('0 0 0 0')

#print(time()-start)
            
'''
1235 0 123 0 24

'''

# [[1, 1, 'A'], [2, 2, 'A'], [1, 1, 'A'], [1, 1, 'A'], [5, 1, 'B'], [10, 2, 'B'], [10, 1, 'C'], [25, 1, 'D'], [25, 1, 'D']]

