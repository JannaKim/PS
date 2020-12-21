from functools import cmp_to_key as cmp#L.sort(key=cmp(lambda a, b:)) 
dic={}
def f(a, b):
    global dic
    if dic[a[0]]> dic[b[0]]:
        return 1
    elif dic[a[0]]< dic[b[0]]:
        return -1
    else:
        if a[1]>b[1]:
            return 1
        elif a[1]<b[1]:
            return -1
        else:
            if a[2]>b[2]:
                return -1
            else:
                return 1
            
def solution(genres, plays):
    global dic
    answer = []
    L=[]
    for i in range(len(genres)):
        if genres[i] in dic:
            dic[genres[i]]+=plays[i]
        else:
            dic[genres[i]]=plays[i]
        L.append((genres[i], plays[i], i))
        
    
       
    L.sort(key=cmp(f), reverse= True)

    temp2=''
    temp=''
    for i in range(len(genres)):
        if temp!=L[i][0]:
            answer.append(L[i][2])
            temp2= temp
            temp=L[i][0]
        elif temp2==L[i][0]: continue
        else:
            temp2=temp
            answer.append(L[i][2])
        
    return answer

g = ['classic', 'pop', 'classic', 'classic', 'pop']
p = [500, 600, 150, 800, 2500]
print(solution(g, p))