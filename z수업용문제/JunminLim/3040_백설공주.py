P=[]
for i in range (9):
    a= int(input())
    P.append(a)


nots = [0, 0]
for i in range (9):
    for j in range (i+1,9):
        if ( sum(P)-(P[i]+P[j]) )==100:
            nots = [i, j]

for i in range(9):
    if i not in nots:
        print(P[i])


    '''
for i in range (9):
    for j in range (i+1,9):
        for k in range (j+1,9):
            for l in range (k+1,9):
                for m in range (l+1,9):
                    for n in range (m+1,9):
                        for o in range (n+1,9):
                            #print(P[i],P[j],P[k],P[l],P[m],P[n],P[o])
                            if P[i]+P[j]+P[k]+P[l]+P[m]+P[n]+P[o]==100:
                                    print(P[i])
                                    print(P[j])
                                    print(P[k])
                                    print(P[l])
                                    print(P[m])
                                    print(P[n])
                                    print(P[o])
'''