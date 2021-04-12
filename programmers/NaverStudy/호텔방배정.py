import sys; sys.setrecursionlimit(220000)
def solution(k, room_number):
    dic= {}
    answer = []
    def find(k):
        if k in dic:
            if dic[k]!=k:
                dic[k]= find(dic[k])
                return dic[k]
            else:
                return k
        else:
            dic[k]=k
        return k

    def union(u, v):
        root1= find(u)
        root2= find(v)
        dic[root1]=root2

    for num in room_number:
        if num not in dic:
            dic[num]=num
        ths=find(dic[num])
        answer.append(ths)
        dic[ths]+=1
        union(ths, num)

    return answer


print(solution(10, [1,3,4,1,3,1]))
#print(solution(10, [1,1,1,1,1,1]))
#print(solution(55, [1,1,1,1,1,1,1,1,1,1,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]))