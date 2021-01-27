while True:
    s= input()
    if s=='*': break
    Len= len(s)-1

    isSur=True
    for idx, i in enumerate(range(Len, 0, -1)):
        pair= {}
        for j in range(idx+1):
            a= s[j]+s[j+i]
            if a not in pair:
                pair[a]=True
            else:
                isSur= False
        if not isSur:
            break
    if isSur:
        print(f'{s} is surprising.')
    else:
        print(f'{s} is NOT surprising.')
