C = [3,2,1,2,3,3,3,3,1,1,3,1,3,3,1,2,2,2,1,2,1,1,2,2,2,1]
s = input()
S=[]
for el in s:
    S.append(C[ord(el)-65])

while len(S)>1:
    A=[]
    for i in range(1,len(S),2):
        A.append((S[i-1]+S[i])%10)
    if len(S)%2:
        A.append(S[-1])
    S=A[:]
if len(S)==1:
    if S[0]%2:
        print("I'm a winner!")
    else:
        print("You're the winner?")
else:
    ans=(S[0]+S[1])%10
    if ans%2:
        print("I'm a winner!")
    else:
        print("You're the winner?")


