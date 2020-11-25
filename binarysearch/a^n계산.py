def power(a, n):# a^n
    if n==0:
        return 1
    elif n==1:
        return a
    else:
        x = power(a,n//2)
    
        if n%2:
            return x*x*a
        else:
            return x*x
 
print(power(3,3))
