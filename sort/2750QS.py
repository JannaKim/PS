n=int(input())
ls= [int(input()) for _ in range(n)]

def QS(a, b):
    if a>=b: return
    start =a
    end= b
    p= ls[(start+end)//2]
    while start<=end:
        while ls[start]<p: start+=1
        while ls[end]>p:  end-=1
        if start<=end:
            ls[start], ls[end]= ls[end], ls[start]
            start+=1
            end-=1

    QS(a, end)
    QS(start, b)

QS(0,n-1)

[print(el) for el in ls]
