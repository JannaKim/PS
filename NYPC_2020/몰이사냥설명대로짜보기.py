
'''
3 2
3
-1 1
7 -3
3 0
'''
X, R = [int(i) for i in input().split()]
N = int(input()) # 모든 몬스터 수
monster_info=[] # 몬스터의 초기 위치, 점프 정도를 튜플로 묶어 저장
go=1
for i in range(N):
    d, s = [int(j) for j in input().split()] # lower_bound, upper_bound 구할 때 s=0인거
    # 쌤해설에서는 s=a d=b  
    monster_info.append((d,s))
    if s==0:
        if d<0 or d>X+R: # 기울기 0 인 몬스터의 초기위치가 소공 범위안에 없으면
            print("F")
            print("1")
            go=0 # 코드 더 돌릴 필요x
            break


def f(t): # O(n). 쌤 설명에서는 이 함수가 f(t)
    # =max_distance_for_all_monster_at_time_t(t)
    # 시간 t의에서 몬스터 위치 d + s*t 모아 리스트에 저장
    monter_locs_at_t=[monster_info[i][0]+ monster_info[i][1]*t for i in range(N)]
    return max(monter_locs_at_t)- min(monter_locs_at_t)


''' 설명중에서,
모든 몬스터에대해 lower_bound ≤ t ≤ upper_bound 찾기

0< b+at <= X+R
0< d+st <= X+R
'''
t_low=[]
t_high=[]
if go:
    for i in range(N):
        '''
                        d +      s   t
                        b +      a   t
        monster_info[i][0]+  monster_info[i][1] * t
        '''
        print(f"i={i}")
        if monster_info[i][0]>=0 and monster_info[i][1]>0: # b>=0, a>0
            if monster_info[i][0]>X+R: #노답
                print(f"5,monster_info[{i}][0]={monster_info[i][0]} ")
                go=0
                break
            t_low.append(0)
            t_high.append( (X+R-monster_info[i][0]) //monster_info[i][1])
            print(f' {i}번째 몹으로 인해 t_low={t_low}, t_high={t_high}')
        elif monster_info[i][0]<0 and monster_info[i][1]>0: # b<0, a>0
            if monster_info[i][0]==monster_info[i][1]:
                t_low.append( (-monster_info[i][0]) //monster_info[i][1])
            else: # a/-b 가 소숫점이면 > 한 t를 t_low 로 넣음
                t_low.append( (-monster_info[i][0]) // monster_info[i][1] +1)
            t_high.append((X+R-monster_info[i][0])//monster_info[i][1])
            print(f' {i}번째 몹으로 인해 t_low={t_low}, t_high={t_high}')
        elif monster_info[i][0]>=0 and monster_info[i][1]<0: # b>=0, a<0
            if monster_info[i][0]-X-R == -monster_info[i][1]:
                t_low.append((monster_info[i][0]-X-R) //(-monster_info[i][1]))
            else:
                t_low.append( (monster_info[i][0]-X-R) //-monster_info[i][1] +1)
            t_high.append( monster_info[i][0]//(-monster_info[i][1]) +1)
            print(f' {i}번째 몹으로 인해 t_low={t_low}, t_high={t_high}')
        else:
            print("6")
            print(f'monster_info[i][0]={monster_info[i][0]}, monster_info[i][1]={monster_info[i][1]}')
            if (monster_info[i][1]!=0): #  b<0, a<0 노답
                go=0
                break
            else: # a=0 인데 소공 범위 안
                pass


def Ternery_Search(a, b):
    print(f'a,b={a},{b}')
    if b-a<=3:
        print(f"f({a}) = {f(a)}, f({b}) = {f(b)} ")
        for i in range(a,b+1):
            print(f'f({i})={f(i)}')
            if f(i)<=R:
                print(f"{i}초 일때 소공이 모든 몹 한 번에 잡을 수 있다")
                return 'T'
        print("7")        
        return 'F' 

    a_=a+ (b-a)//3
    b_=a+ ((b-a)//3)*2

    if f(a_)==f(b_):
        return Ternery_Search(a_,b_)
    elif f(a_)<f(b_):
        return Ternery_Search(a,b_)
    else: # elif f(a_)>f(b_):
        return Ternery_Search(a_,b)
    


if go==0:
    print("4")
    print("F")
else:
    print(f' 최종 t_low={t_low}, t_high={t_high}')
    t_min=min(t_low)
    t_max=max(t_high)
    print(f't_min={t_min}, t_max={t_max}')
    print(Ternery_Search(t_min, t_max))









