num_racers = int(input())
asv = input()
x = [int(i) for i in input().split()]

a=[]
na=0
# 자신의 랩타임 이내에 2번 들어온 사용자가 있으면 그 랩은 우승 후보가 아니게 됨
for i in range(num_racers):
    racer = i + 1
    arrivals = []
    unique_arrivals = set()
    is_winner = False
    for arrival in x:
        if arrival != racer:  # 이번 랩이 우승 후보일 수 있는가?
            arrivals.append(arrival)
            unique_arrivals.add(arrival)
        else:  # 해당 레이서가 도착
            if len(arrivals) == len(unique_arrivals):
                is_winner = True
            arrivals = []
    if is_winner:
        na+=1
        a.append(i+1)

print(na)
aaa=len(a)
for i in range(0,aaa):
    print(a[i],end=' ')
