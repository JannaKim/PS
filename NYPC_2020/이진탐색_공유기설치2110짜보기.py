N, C = [int(i) for i in input().split()]
house_loc=[]
for i in range(N):
    house_loc.append(int(input()))
low=house_loc[0]
high=house_loc[-1]

# router = rt
# install = Ins
rt_Insd_idx=[0] # 설치 완료된 집들의 index
rt_left = C-1 # num of router left to be installed
try_idx = 1 # 설치 시도해볼 집의 index
while(low<=high):
    while(rt_left):
        m = (low+high)//2 # m을 공유기 사이 최대 거리라 가정
        while (house_loc[try_idx]- house_loc[rt_Insd_idx[-1]] <C):
            try_idx+=1


    


