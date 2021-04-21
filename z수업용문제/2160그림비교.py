mx=0
ans=0
n= int(input())
pictures= []
for i in range(n):
    pic=''
    for _ in range(5):
        pic+=input()
    pictures.append(pic)

for i in range(n):
    for j in range(i+1,n):
        score=0
        for a, b in zip(pictures[i], pictures[j]):
            if a==b:
                score+=1
        if score>mx:
            mx=score
            ans=[i+1,j+1]
print(*ans)
