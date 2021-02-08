eq= input().split('+')
part=[]
for a in eq:
    startsWMinus=False
    if a[0]=='-':
        startsWMinus=True
    b= a.split('-')
    chunk=[]
    for c in b: # c: pure a*x^b
        if not c:
            continue
        end=-1
        isX=False
        n=0
        for i, d in enumerate(c): # find pure num
            if d=='x':
                end= i
                isX= True
                break
            n= len(c)-i
        if end>0: # num and x
            if int(c[:end])//n==1:
                chunk.append('x'*n)
            else:
                chunk.append(str(int(c[:end])//n)+ 'x'*n)
        elif not end: # only x
            chunk.append(str(1//n)+ 'x'*n)
        else: # only num
            if c=='1':
                chunk.append('x')
            elif c!='0':
                chunk.append(c+'x')
    if startsWMinus and len(chunk)==1:
        part.append('-'+chunk[0])
    elif startsWMinus:
        part.append('-'+'-'.join(chunk))
    else:
        part.append('-'.join(chunk))
if not '+'.join(part):
    print('W')
else:
    print('+'.join(part)+'+W')
