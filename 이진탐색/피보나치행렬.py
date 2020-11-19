def mul(n):
    if n==0:
        return [[1,0],[0,1]]
    elif n==1:
        return [[1,1], [1,0]]
    else:
        A = mul(n//2)
        a = A[0][0]
        b = A[0][1]
        c = A[1][0]
        d = A[1][1]
        if n%2:
            return [[a**2+ b*c+ a*b+ b*d, a**2+ b*c], [a*c+ c*d+ b*c+ d**2, a*c+ c*d]]
        else:   
            return [[a**2+b*c, a*b+b*d], [a*c+c*d, b*c+d**2]]

N = int(input())
if N==0:
    print(0)
elif N==1:
    print(1)
else:
    print(mul(N-1)[0][0]%(int(1e6)))