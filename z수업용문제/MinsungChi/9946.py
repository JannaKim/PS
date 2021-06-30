a=1
while True:
    
    L=[0]*26
    M=[0]*26
    n= input()
    m= input()
    if n=='END' and m=='END':
        break
    for i in range(0,len(n)):
        L[ord(n[i])-97]+=1
    for k in range(0,len(m)):
        M[ord(m[k])-97]+=1
    if M==L:
        print(f'Case {a}: same')
    else: 
        print(f'Case {a}: different')
    a=a+1