w= int(input())
L = list(range(1, 1 + w))
for i in range(w):  
    for j in range(w):
        for k in range(w):
            se = set()
            se.update([L[i], L[j], L[k]]
            if len(se) == 3:
                print(L[i], L[j], L[k])
            # 1 3 6 6 7 // 1 3 6 7

