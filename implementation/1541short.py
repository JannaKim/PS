s= input().split('-')

ans=[]
for chunk in s:
    s=0
    for operand in chunk.split('+'):
        s+=int(operand)
    ans.append(str(s))

print(eval('-'.join(ans)))
