import sys; input= lambda: sys.stdin.readline().rstrip()


def solution(array, commands):
    ans=[]
    for i, j, k in commands:
        i=int(i)
        j=int(j)
        k=int(k)
        ans.append(sorted(array[i-1:j][:])[k-1])
    return ans


print(solution([6, 5, 4, 3, 2, 1], [[1,3,1],[2,4,3],[1,6,6]]))