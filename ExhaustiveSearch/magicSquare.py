sq= [[*map(int, input().split())] for _ in range(3)]
ans=81

'''
side= [sum(sq[0]), sum(sq[2])]
for i in (0,2):
    s=0
    for j in range(3):
        s+=sq[j][i]
side.append(s)
mid= [sq[0][0]+sq[1][1]+sq[2][2]]
mid.append(sq[0][1]+ sq[1][1]+ sq[2][1])
mid.append(sq[0][2]+ sq[1][1]+ sq[2][0])
mid.append(sq[1][0]+ sq[1][1]+ sq[1][2])

k=0
if abs(sum(side)-sum(mid))>=4:
    if sum(side)>sum(mid):
        k=(abs(sum(side)-sum(mid)))//4
        sq[1][1]-=(abs(sum(side)-sum(mid)))//4
    else:
        k=(abs(sum(side)-sum(mid)))//4
        sq[1][1]+=(abs(sum(side)-sum(mid)))//4
'''

k=abs(sq[1][1]-5)
for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            for d in range(1,10):
                for e in range(1,10):
                    for f in range(1,10):
                        for g in range(1,10):
                            for h in range(1,10):
                                s=0
                                s+=abs(a-sq[0][0])
                                s+=abs(b-sq[0][1])
                                s+=abs(c-sq[0][2])
                                s+=abs(d-sq[1][0])
                                s+=abs(e-sq[1][2])
                                s+=abs(f-sq[2][0])
                                s+=abs(g-sq[2][1])
                                s+=abs(h-sq[2][2])
                                ans=min(ans,s)

print(ans)