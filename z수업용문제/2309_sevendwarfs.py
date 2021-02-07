dw= []
for _ in range(9):
    dw.append(int(input()))
dw.sort()
s= sum(dw)
for i in range(9):
    for j in range(i+1, 9):
        if s-dw[i]-dw[j]==100:
            for k in range(9):
                if dw[k]!=dw[i] and dw[k]!=dw[j]:
                    print(dw[k])
            exit()
