# input
"""
packing, unpacking

c = (3,4)
d,e=c
"""
n = int(input())
s, k = [int(x) for x in input().split()]
score = [int(x) for x in input().split()]
queue = []
for i in range(n):
    queue.append((i+1, score[i])) # 튜플로 저장

#print(queue)

def keyfunction(x):
	return abs(x-s) + (0.5 if x > s else 0)



#queue.sort(key = lambda x : abs(x[1]-s) + (0.5 if x[1] > s else 0)) # key: 앞에 꺼

queue.sort(key = lambda x : keyfunction(x[1]))

print(queue)

for i in queue[:k]: # 리스트 안의 튜플
    print(i[0],end=' ')


#print(queue[:k][0]) 이게 안되는 이유


