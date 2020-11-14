from functools import cmp_to_key
import sys
N = int(input())
loc=[]
for i in range(N):
    a, b = list(map(int,input().split()))
    loc.append({'x':a, 'y':b})



# 좌표별로 down, up, left, right 계산하기

loc.sort(key=cmp_to_key(lambda a, b: a['y']-b['y'] if a['x']==b['x'] else a['x']-b['x']))

# down ↑→

loc[0]['d']=0
for i in range(1,N):
    if loc[i-1]['x'] == loc[i]['x'] and loc[i]['y'] -loc[i-1]['y'] ==1: # 붙어있을 때
        loc[i]['d']=loc[i-1]['d']+1
    else:
        loc[i]['d']=0

# up ↓←
loc[N-1]['u']=0
for i in range(N-2,-1,-1): # 이전 좌표가 더 크다
    if loc[i-1]['x'] == loc[i]['x'] and loc[i+1]['y'] -loc[i]['y'] ==1:
        loc[i]['u']=loc[i+1]['u']+1
    else:
        loc[i]['u']=0

loc.sort(key=cmp_to_key(lambda a, b: a['x']-b['x'] if a['y']==b['y'] else a['y']-b['y']))


#left →↑
loc[0]['l']=0
for i in range(1,N):
    if loc[i-1]['y'] == loc[i]['y'] and loc[i]['x'] -loc[i-1]['x'] ==1:
        loc[i]['l']=loc[i-1]['l']+1
    else:
        loc[i]['l']=0

# right ←↓
loc[N-1]['r']=0
for i in range(N-2,-1,-1): # 이전 좌표가 더 크다
    if loc[i-1]['y'] == loc[i]['y'] and loc[i+1]['x'] -loc[i]['x'] ==1:
        loc[i]['r']=loc[i+1]['r']+1
    else:
        loc[i]['r']=0



for i in range(N):
    loc[i]['p']=min(loc[i]['u'], loc[i]['d'], loc[i]['l'], loc[i]['r'])






for i in range(N):
    loc[i]['V']=False

x_max=0 # power로 인해 칠해지는 x최대 좌표
# →↑
for i in range(N):
    if i==0 or loc[i]['y']!=loc[i-1]['y']:
        x_max=0
    else:
        if loc[i]['x']+loc[i]['p'] > x_max:
            x_max=loc[i]['x']+loc[i]['p']
        if loc[i]['x']<=x_max:
            loc[i]['V']=True

x_min=2e9 # power로 인해 칠해지는 x최대 좌표
for i in range(N-1,-1,-1):
    if i==N-1 or loc[i]['y']!=loc[i+1]['y']:
        x_min=2e9
    else:
        if loc[i]['x']-loc[i]['p'] < x_min:
            x_min=loc[i]['x']-loc[i]['p']
        if loc[i]['x']>=x_min:
            loc[i]['V']=True


loc.sort(key=cmp_to_key(lambda a, b: a['x']-b['x'] if a['y']==b['y'] else a['y']-b['y']))
# →↑
y_max=0 # power로 인해 칠해지는 x최대 좌표
for i in range(N):
    if i==0 or loc[i]['x']!=loc[i-1]['x']:
        y_max=0
    else:
        if loc[i]['y']+loc[i]['p'] > x_max:
            x_max=loc[i]['y']+loc[i]['y']
        if loc[i]['y']<=x_max:
            loc[i]['V']=True

y_min=2e9 # power로 인해 칠해지는 x최대 좌표
for i in range(N-1,-1,-1):
    if i==N-1 or loc[i]['x']!=loc[i+1]['x']:
        y_min=2e9
    else:
        if loc[i]['y']-loc[i]['p'] < x_min:
            x_min=loc[i]['y']-loc[i]['p']
        if loc[i]['y']>=x_min:
            loc[i]['V']=True

[print(loc[i], end=('\n' if (i+1) % 3 == 0 else ' ')) for i in range(N)]



if not all([loc[i]['V'] for i in range(N)]):
    print(-1)
    sys.exit()

print(len([i for i in range(N) if loc[i]['p'] > 0]))

[print( loc[i]['x'], loc[i]['y'], loc[i]['p'] ) for i in range(N) if loc[i]['p'] > 0]

'''
12
1 3
2 3
3 1
3 2
3 3
3 4
3 5
4 1
4 2
4 3
5 2
5 3
'''
