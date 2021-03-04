n= int(input())


candi= {}
for _ in range(n**2):
    score, num, *t,=[*map(int, input().split())]
    for time in t:
        if time not in candi:
            candi[time]=score
        else:
            candi[time]= max(candi[time], score)

ans= sum(candi.values())
print(ans)