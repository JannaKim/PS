import sys; input= lambda: sys.stdin.readline().strip()

n= int(input())

wei=[0]*26
words=[]
for _ in range(n):
    a=input()
    words.append(a)
    for idx, el in enumerate(a[::-1]):
        ths=ord(el)-65
        wei[ths]+=10**idx
q=[]
for i in range(26):
    if wei[i]>0:
        q.append((wei[i], i))
q.sort(reverse= True)
dic={}
for idx, (a, b) in enumerate(q):
    dic[chr(b+65)]=9-idx

def calculate():
    S=0
    for i in range(n):
        for idx, el in enumerate(words[i][::-1]):
            S+=dic[el]*10**idx
    return S       
print(calculate())