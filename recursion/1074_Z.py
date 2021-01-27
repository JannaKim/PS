n, r, c= map(int, input().split())
ans=0
sy=sx=0
ey=ex=2**n-1
while sy!=ey and sx!=ex:
    little= ((ey-sy+1)//2)**2
    if r<=(sy+ey)//2:
        if c<=(sx+ex)//2:
            ey= (sy+ey)//2
            ex= (sx+ex)//2
        else:
            sx= (sx+ex)//2+1
            ey= (sy+ey)//2
            ans+=little
    else:
        if c<=(sx+ex)//2:
            sy= (sy+ey)//2+1
            ex= (sx+ex)//2
            ans+=2*little
        else:
            sy= (sy+ey)//2+1
            sx= (sx+ex)//2+1
            ans+=3*little
print(ans)

# n 100이상일 때 재귀: 50초 반목문: 1초대