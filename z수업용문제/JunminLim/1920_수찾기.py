n=int(input())
L=[*map(int,input().split())]
L.sort()


def check(k):
    left= 0
    right=n-1

    while left<right:

        middle= (left+right)//2
        if L[middle]==k:
            return 1
        elif L[middle]>k:
            right= middle-1

        elif L[middle]<k:
            left= middle+1
    if L[left]!=k:
        return 0
    else:
        return 1


m= int(input())
Q= [*map(int, input().split())]
for q in Q:
    print(check(q))
