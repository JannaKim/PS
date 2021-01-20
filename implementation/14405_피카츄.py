S = input()
A = S.replace('pi','')
B = S.replace('ka','')
C = S.replace('chu','')

if len(A+B+C)==2*len(S):
    print("YES")

else:
    print("NO")


# 반례 kpia

