X, A, B, C, D = map(int, input().split())
pack = []
def binary_pack(unit, num, idx):
    n = len(bin(num)[2:])
    if num==2**n-1:
        for i in range(n):
            pack.append((2**i*unit, 2**i, idx))
    else:
        for i in range(n-1):
            pack.append((2**i*unit, 2**i, idx))
        num -= 2**(n-1)-1
        remain = bin(num)[2:]
        for deg, i in enumerate(remain[::-1]):
            if int(i):
                pack.append((2**deg*unit, 2**deg, idx))

binary_pack(1,A, 0)
binary_pack(5,B, 1)
binary_pack(10,C, 2)
binary_pack(25,D, 3)

print(pack)
print()
#pack:(amount, num, idx)
# dp[i][j]: 새로받은 i번째 동전까지 썼을때 j원을 만드는 데 쓸 수 있는 
# (최대 동전개수,[쓴동전별 개수])
dp = []

[dp.append([[0,[0,0,0,0]]]*(X+1)) for _ in range(len(pack))]
#[print(i) for i in dp]
#print()
for i in range(len(pack)):
    print(pack)
    ANI=pack[i] # (Amount, Num, Idx)
    if ANI[0]<X+1 and dp[i-1][ANI[0]][0] <ANI[1]:
        a = [0,0,0,0]
        a[ANI[2]]=ANI[1]
        dp[i][ANI[0]] = (ANI[1], a)
        print(f'1 dp[{i}][{ANI[0]}]: {dp[i][ANI[0]]}')
    elif ANI[0]<X+1: 
        dp[i][ANI[0]] = dp[i-1][ANI[0]][:]
        print(f'2 dp[{i}][{ANI[0]}]: {dp[i][ANI[0]]}')

    for j in range(1,X+1): # dp: (lowest n, info)
        if ANI[0]<j:
            print()
            print(f'  if {dp[i-1][j][0]}<dp[{i-1}][{j}-{ANI[0]}][0]+{ANI[1]}')
            if dp[i-1][j][0]<dp[i-1][j-ANI[0]][0]+ANI[1]:
                a = dp[i-1][j-ANI[0]][1][:]
                print(f'dp[{i-1}][{j-ANI[0]}][1] {dp[i-1][j-ANI[0]][1]}')
                print('   ',a)
                a[ANI[2]]+=ANI[1]
                print('   ',a)
                dp[i][j] = (dp[i-1][j-ANI[0]][0]+ANI[1], a)
                print(f'3 dp[{i}][{j}]: {dp[i][j]}')
            else:
                dp[i][j] = dp[i-1][j][:]
                print(f'4 dp[{i}][{j}]: {dp[i-1][j]}')
        elif ANI[0]!=j:
            dp[i][j] = dp[i-1][j][:]
            print(f'5 dp[{i}][{j}]: {dp[i-1][j]}')

#[print(i) for i in dp]
print()
print(dp[-1][X])



'''
12 5 3 1 2
'''