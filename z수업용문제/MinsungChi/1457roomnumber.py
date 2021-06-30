n = input()
L = [0] * 11
for i in range(0,len(n)):
    L[int(n[i])] += 1
L[10] = ((L[9] + L[6]) // 2 + (L[9] + L[6]) % 2)
L[6] = 0
L[9] = 0

print(max(L))



# + - = // % > > : 앞 뒤에 스ㅠㅔ이스 바
# , a, b  0, 0, 0, 0