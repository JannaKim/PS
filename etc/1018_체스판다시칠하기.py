N, M = map(int, input().split())
mp=[]
mp=[' '*M]
for _ in range(N):
    mp.append(' '+input())

def brute_force(i,j):
    cnt=0
    cnt2=0
    for y in range(i,i+8):
        for x in range(j,j+8):
            if (y-i)%2:
                L=['B','W']
                if mp[y][x]!=L[(x-j)%2]:
                    cnt+=1
            else:
                L=['W','B']
                if mp[y][x]!=L[(x-j)%2]:
                    cnt+=1
            if (y-i)%2:
                L=['W','B']
                if mp[y][x]!=L[(x-j)%2]:
                    cnt2+=1
            else:
                L=['B','W']
                if mp[y][x]!=L[(x-j)%2]:
                    cnt2+=1
    return min(cnt,cnt2)
mn=M*N
for i in range(1,N-8+2):
    for j in range(1,M-8+2):
        mn = min(mn,brute_force(i,j))
print(mn)

'''
8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW

10 13
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
WWWWWWWWWWBWB
WWWWWWWWWWBWB
'''
