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

    def draw(self,other_Obj,x,y): # 다른객체 이용하는법? map바꿀떄마다 둘이 통일 시켜주면 될듯
        prev_x=self.x
        prev_y=self.y
        # mp객체 하나만 만들어서 이용하기?
        f(self, (self.name,prev_x,prev_y,x,y))







player1= setplayer('$',1,1)
#f(player1,player1.draw(1,1))
player1.draw(1,1)
[print(*el) for el in mp]
print()

player2= setplayer('%',8,2)
player1.draw(8,2)
player1.draw(player2,1,1)
[print(*el) for el in mp]
print()


