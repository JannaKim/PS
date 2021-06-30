a, b = map(int, input().split())
'''
x<=n(n+1)/2
0 <= n^2 + n - 2 * x
'''
n = ((-1 + (1 + 8 * a))**(0.5) + 0.5) // 2
#print(n)

i, j = 1 , 0
ans = 0
while j <= b:
    ans += i ** 2
    #print(j, b, j + (i ** 2), ans)
    j += i
    if b < j:
        ans -= (i) * (j - b)
        break
    
    i += 1

i, j = 1 , 0
tmp = 0   
a -= 1
while j <= a:
    tmp += i ** 2
    #print(j, a, j + (i ** 2), tmp)
    j += i
    if a < j:
        #print(a, j, tmp)
        tmp -= (i) * (j - a)
        break
    i += 1

print(ans - tmp)