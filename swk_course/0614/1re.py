from itertools import combinations as combi
for _ in range(4):
    L = [*map(int, input().split())]
    player = list(range(6))
    game = list(combi(player, 2))

    #print(*game, sep = '\n')

    inst = (( (1, 0, 0), (0, 0, 1)),
        ((0, 0, 1), (1, 0, 0)),
        ((0, 1, 0), (0, 1, 0)) )

    def backtrack(pos):
        #print(pos , B)
        if pos == 15:
            if A == L:
                return True
            return False
        p1, p2 = game[pos]

        res = False
        for a , b in inst:
            for idx, i in enumerate(range(p1 * 3, p1 * 3 + 3)):
                A[i] += a[idx]

            for idx, i in enumerate(range(p2 * 3, p2 * 3 + 3)):
                A[i] += b[idx]

            flag = True
            for i in range(18):
                if A[i] > L[i]:
                    flag = False
                    break  
            if flag:
                res |= backtrack(pos + 1)

            for idx, i in enumerate(range(p1 * 3, p1 * 3 + 3)):
                A[i] -= a[idx]

            for idx, i in enumerate(range(p2 * 3, p2 * 3 + 3)):
                A[i] -= b[idx]

        return res
    A = [0]* 18
    if backtrack(0):
        print(1, end = ' ')
    else:
        print(0)

        


    '''
    5 0 0 3 0 2 2 0 3 0 0 5 4 0 1 1 0 4
    4 1 0 3 0 2 4 1 0 1 1 3 0 0 5 1 1 3
    5 0 0 4 0 1 2 2 1 2 0 3 1 0 4 0 0 5
    5 0 0 3 1 1 2 1 2 2 0 3 0 0 5 1 0 4

5 0 0 3 0 2 2 0 3 0 0 5 4 0 1 1 0 4
4 1 0 3 0 2 4 1 0 1 1 3 0 0 5 1 1 3
5 0 0 4 0 1 2 2 1 2 0 3 1 0 4 0 0 5
5 0 0 3 1 1 2 1 2 2 0 3 0 0 5 1 0 4
    '''