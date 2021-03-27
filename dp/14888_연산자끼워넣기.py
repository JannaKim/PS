n= int(input())
L= [*map(int, input().split())]
a_s_m_d= [*map(int, input().split())]
oper=[]
for _ in range(a_s_m_d[0]):
    oper.append('+')
for _ in range(a_s_m_d[1]):
    oper.append('-')
for _ in range(a_s_m_d[2]):
    oper.append('*')
for _ in range(a_s_m_d[3]):
    oper.append('//')

Len= len(oper)
chk= [False]*Len
mn=1e10
mx=-1e10
def backtrack(i,sm):
    
    if i==Len:
        global mx,mn
        mn= min(mn, sm)
        mx= max(mx, sm)
        return
    for j in range(Len):
        if not chk[j]:
            chk[j]=True
            backtrack(i+1,int(eval(str(sm)+oper[j]+str(L[i+1]))))
            chk[j]=False

backtrack(0,L[0])
print(mx)
print(mn)
