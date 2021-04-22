for _ in range(4):
    q, w, e, r, t, y, u, i= map(int, input().split())
    x1= (e+q)/2
    y1= (r+w)/2
    wid1= e-x1
    hei1= r-y1
    x2= (u+t)/2
    y2= (i+y)/2
    wid2= u-x2
    hei2= i-y2
    #print(x1,y1,wid1,hei1, x2,y2,wid2,hei2)
    if abs(x1-x2)<wid1+wid2 and abs(y1-y2)<hei1+hei2:
        print('a')
    elif abs(x1-x2)==wid1+wid2 or abs(y1-y2)==hei1+hei2:
        if abs(x1-x2)==wid1+wid2 and abs(y1-y2)==hei1+hei2:
            print('c')
        else:
            print('b')
    else:
        print('d')