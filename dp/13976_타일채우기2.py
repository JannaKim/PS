n = int(input())
ln = max(n , 2)
FULL = [0] * (ln + 1)

TWO = [0] * (ln + 1)

FULL[1] = 0
FULL[2] = 3
TWO[1] = 2


for i in range(3 , n + 1):
    
    TWO[i] = TWO[i-2] + FULL[i-1] * 2 # TWO[i-1] = B[i- 2] + FULL[i-2] * 2
    FULL[i] = TWO[i-1] + FULL[i - 2]

print(FULL[n])