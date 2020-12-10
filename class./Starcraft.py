class Unit:
    def __init__(self, name, hp, damage):
        self.name= name
        self.hp= hp
        self.damage= damage
        print(self.name, self.hp, self.damage) #??

    #def Attack(self):


class NoDamageUnit(Unit):
    def __init__(self, name, hp):
        self.name= name
        self.hp= hp
        print(self.name, self.hp)


one = Unit("Obj_1", 100, 1)
two = Unit("Obj_2", 50, 3)

#one.Attack()
