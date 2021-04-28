s=input()
n= len(s)
m= int(input())
broke= [False]*10
L=[]
if m:
    L=[*map(int, input().split())]
for k in L:
    broke[k]=True

goal= int(s)
ans=abs(100-int(s))

for i in range(1000000+1):
    flag=True
    for num in str(i):
        if broke[int(num)]:
            flag=False
            break
    if flag:
        ans= min(len(str(i))+abs(goal-i), ans)
print(ans)

# 19 18 17 16 15 14 13 12 11
#119
#120 121 122 123

'''
5455 + +

20
0 
'''
'''
'''
타켓 ABC..Z에 대해
A___, A에 가장 가까운 작은 숫자 a___, A에 가장 가까운 가장 큰 숫자 b___중 기존 타켓에 가장 가까운 숫자 고름
not_broken이 비어 있지는 않을 것이므로 위의 세 가지 중 적어도 한 가지 경우는 무조건 존재
cab == False인 경우는 다루는 타겟이 일부분이 아닐 경우로 a와 b가 존재하지 않을 시 올림수나 내림수를 고려하여 숫자를 찾음
cab == True인 경우 다루는 타겟이 일부분인 경우로, a 또는 b가 없을 시 해당 경우를 그냥 스킵함
(일부분 바로 앞의 가장 높은 자릿수의 숫자가 정해져 있으므로 올림수 또는 내림수를 고려하지 않음)
'''


def finding_closest_num(target: str, not_broken: list, cab=False) -> str:
    cases = []
    # highest digit is closest of smaller ones than that of the target
    # 'smallest number' + MAX
    digit_num = -1
    for i in not_broken:
        if i >= int(target[0]):
            break
        digit_num = i
    if digit_num == -1:
        if cab:
            pass
        else:
            cases.append(str(not_broken[-1])*len(target[1:]))
    else:
        cases.append(str(digit_num)+str(not_broken[-1])*len(target[1:]))
    # highest digit is closest of bigger ones than that of the target
    # 'biggest number' + MIN
    digit_num = -1
    for i in not_broken[::-1]:
        if i <= int(target[0]):
            break
        digit_num = i
    if digit_num == -1:
        if cab:
            pass
        else:
            # 가장 큰 자리수가 0일 수는 없다
            if not_broken[0] == 0:
                if len(not_broken) == 1:
                    pass
                else:
                    cases.append(str(not_broken[1]) +
                                 str(not_broken[0])*(len(target[0:])))
            else:
                cases.append(str(not_broken[0])*(len(target[0:])+1))
    else:
        cases.append(str(digit_num)+str(not_broken[0])*len(target[1:]))

    # highest digit is the same as that of the target
    if int(target[0]) in not_broken:
        if len(target) > 1:
            cases.append(target[0] +
                         finding_closest_num(target[1:], not_broken, True))
        else:
            cases.append(target[0])

    closest_num = ''
    for i in cases:
        if not closest_num or \
           abs(int(target)-int(closest_num)) > abs(int(target)-int(i)):
            closest_num = i
    return closest_num


# print(finding_closest_num('54255', [2,5,6,7]))

target = input()
broken_num = int(input())
broken = []
if broken_num != 0:
    broken = input().split(" ")
not_broken = [int(i) for i in range(0, 10) if str(i) not in broken]

# 10개 다 망가짐
if not not_broken:
    print(abs(int(target) - 100))
else:
    closest_num = int(finding_closest_num(target, not_broken))
    print(min(abs(int(target) - 100),
          len(str(closest_num))+abs(int(target) - closest_num)))

'''