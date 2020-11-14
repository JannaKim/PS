from functools import cmp_to_key
import sys
N = int(input())

loc= []
for i in range(N):
 a,b = list(map(int,input().split()))
 loc.append({'x':a, 'y':b})

#print(loc)

# x 좌표 기준으로 오름차순 정렬, x좌표 같은 애들끼리는 y 기준 정렬
loc.sort(key=cmp_to_key(lambda p1, p2:  p1['y'] - p2['y'] if p1['x']==p2['x'] else p1['x']-p2['x'] )) # cmp_to_key a, b 받았을때 정렬


'''
print(loc)
[{'x': 1, 'y': 3}, {'x': 2, 'y': 3}, {'x': 3, 'y': 1}, {'x': 3, 'y': 2}, 
{'x': 3, 'y': 3}, {'x': 3, 'y': 4}, {'x': 3, 'y': 5}, {'x': 4, 'y': 1}, 
{'x': 4, 'y': 2}, {'x': 4, 'y': 3}, {'x': 5, 'y': 2}, {'x': 5, 'y': 3}]

'''
# UP
loc[N-1]['up'] = 0
for i in range(N-2, -1,-1): # 뒤부터 계산
    # 자기보다 위에 필해진 칸 만큼 자신의 up 수 늘리기
    # 자신과 x좌표는 같고 y좌표는 큰애
    if loc[i]['x'] ==loc[i+1]['x'] and  loc[i+1]['y'] -loc[i]['y'] ==1:
            loc[i]['up'] = loc[i+1]['up']+1 # 자기보다 위에있는 애의 up값보다 1크게
    else:
        loc[i]['up']=0
    


# DOWN
loc[0]['down'] = 0
for i in range(1,N): # 뒤부터 계산  여기 이해 안감
    # 자기보다 위에 필해진 칸 만큼 자신의 up 수 늘리기
    # 자신과 x좌표는 같고 y좌표는 큰애
    if loc[i]['x'] ==loc[i-1]['x'] and  loc[i]['y'] -loc[i-1]['y'] ==1:
            loc[i]['down'] = loc[i-1]['down']+1 
    else:
        loc[i]['down']=0



loc.sort(key=cmp_to_key(lambda p1, p2:  p1['x'] - p2['x'] if p1['y']==p2['y'] else p1['y']-p2['y'] )) # cmp_to_key a, b 받았을때 정렬

# RIGHT
loc[N-1]['r'] = 0
for i in range(N-2, -1,-1): # 뒤부터 계산
    # 자기보다 위에 필해진 칸 만큼 자신의 up 수 늘리기
    # 자신과 x좌표는 같고 y좌표는 큰애
    if loc[i]['y'] ==loc[i+1]['y'] and  loc[i+1]['x'] -loc[i]['x'] ==1:
            loc[i]['r'] = loc[i+1]['r']+1 # 자기보다 오른쪽에 있는 애의 right 값보다 1크게
    else:
        loc[i]['r']=0
    
# LEFT
loc[0]['l'] = 0
for i in range(1,N): # 뒤부터 계산  여기 이해 안감
    # 자기보다 위에 필해진 칸 만큼 자신의 up 수 늘리기
    # 자신과 x좌표는 같고 y좌표는 큰애
    if loc[i]['y'] ==loc[i-1]['y'] and  loc[i]['x'] -loc[i-1]['x'] ==1:
            loc[i]['l'] = loc[i-1]['l']+1  # 자기보다  왼쪽에 있는 애의 left 값보다 1크게
    else:
        loc[i]['l']=0


for i in range(N):
    loc[i]['power'] = min([loc[i]['up'],loc[i]['down'],loc[i]['r'],loc[i]['l']])

for i in range(N):
    print(loc[i]['x'], loc[i]['y'], loc[i]['power'])





for i in range(N):
    loc[i]['V']=False

# 오른쪽 채우기
# y좌표 로 정렬, y 같을 땐 x순서로


x_max=0
for i in range(N):
    if i==0 or loc[i-1]['y'] != loc[i]['y']:
        x_max=0
    if loc[i]['power']>0:
        if x_max < loc[i]['x'] + loc[i]['power']:
            x_max = loc[i]['x'] + loc[i]['power']
    if loc[i]['x']<=x_max:
        loc[i]['V']=True

#왼쪽 채우기
x_min=2e9
for i in range(N-1,-1,-1):
    if i==N-1 or loc[i+1]['y'] != loc[i]['y']:
        x_min=2e9
    if loc[i]['power']>0:
        if x_min > loc[i]['x'] - loc[i]['power']:
            x_min = loc[i]['x'] - loc[i]['power']
    if loc[i]['x']>=x_min:
        loc[i]['V']=True


    

loc.sort(key=cmp_to_key(lambda p1, p2:  p1['y'] - p2['y'] if p1['x']==p2['x'] else p1['x']-p2['x'] )) 

# 위쪽 채우기
# x좌표 로 정렬, x같을 땐 y순서로 

y_max=0
for i in range(N):
    if i==0 or loc[i-1]['x'] != loc[i]['x']:
        y_max=0
    if loc[i]['power']>0:
        if y_max < loc[i]['y'] + loc[i]['power']:
            y_max = loc[i]['y'] + loc[i]['power']
    if loc[i]['y']<=y_max:
        loc[i]['V']=True

#아래쪽 채우기
y_min=2e9
for i in range(N-1,-1,-1):
    if i==N-1 or loc[i+1]['x'] != loc[i]['x']:
        y_min=2e9
    if loc[i]['power']>0:
        if y_min > loc[i]['y'] - loc[i]['power']:
            y_min = loc[i]['y'] - loc[i]['power']
    if loc[i]['x']>=y_min:
        loc[i]['V']=True



if not all([loc[i]['V'] for i in range(N)]):
        print(-1)
        sys.exit()


print(len([point for point in loc if point['power']>0]))


for i in range(N):
    if loc[i]['power']>0:
        print(loc[i]['x'],loc[i]['y'],loc[i]['power'])
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