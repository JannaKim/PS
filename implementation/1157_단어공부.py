s = input()
s=s.upper()
dic={}
for i in range(65,91):
    dic[chr(i)]=0
mx=0
for el in s:
    dic[el]+=1
    mx=max(dic[el], mx)

ans=[]
for k, v in dic.items():
    if v==mx:
        ans.append(k)

if len(ans)>1:
    print('?')
else:
    print(*ans)



