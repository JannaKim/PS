n, k= map(int, input().split())
L= [*map(int ,input().split())]
L.sort(reverse=True)

leng= len(str(n))
isThree=True
def backtrack(i, num, digit):
    if i==digit:
        if num<=n:
            print(num)
            exit()
        else:
            return
    for el in L:
        backtrack(i+1, num*10+el, digit)

backtrack(0, 0, leng)
backtrack(0, 0, leng-1)
#print(str(L[0])*(leng-1))