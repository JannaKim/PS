while True:
    lot= input()
    if lot=='0': break

    L= [*map(int,lot.split())]

    ans=[]
    def backtrack(i, cnt, n):

        if cnt==6:
            print(*ans)
            return
        if i>n: return
        if n-i+1+cnt<6: return

        ans.append(L[i])
        backtrack(i+1, cnt+1, n)
        ans.pop()
        backtrack(i+1, cnt, n)


    backtrack(1, 0, L[0])
    print()