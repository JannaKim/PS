mp = [[1]*10 for _ in range(8)]


def f(Obj, Obj_info):
    name = Obj_info[0]
    cur_x = Obj_info[1]
    cur_y = Obj_info[2]
    dest_x = Obj_info[3]
    dest_y = Obj_info[4]
    if mp[(cur_y+8)%8][(cur_x+10)%10]== 1:
        Obj.score+=1
    mp[(cur_y+8)%8][(cur_x+10)%10]
    if mp[(dest_y+8)%8][(dest_x+10)%10]== 1:
        Obj.score+=1
    mp[(dest_y+8)%8][(dest_x+10)%10]= name

    

class setplayer:
    def __init__(self, name, x, y):
        self.name= name
        self.x= x
        self.y= y
        self.score=0

    def draw(self,x,y):
        prev_x=self.x
        prev_y=self.y
        return((self.name,prev_x,prev_y,x,y))






player1= setplayer('$',1,1)
f(player1,player1.draw(1,1))
[print(*el) for el in mp]
print()

player2= setplayer('%',8,2)
f(player2,player2.draw(8,2))
[print(*el) for el in mp]
print()


