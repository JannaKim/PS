def game_start():
    print("[note] new game")

def game_over(gg_player):
    print(f"Player[{gg_player}]: gg")
    print(f"[{gg_player}] went out.")

class Unit:
    def __init__(self, name, hp, damage):
        
        self.name= name
        self.hp= hp
        self.damage= damage
        # self.defaulthp 불가??
        self.defaulthp=hp
        print(f"{self.name}({self.hp}/{hp})[{self.damage}] is created.") 

    def attack(self, target):
        print(f"{self.name}({self.hp}/{self.defaulthp})[{self.damage}] aims {target.name}({target.hp}/{target.defaulthp})[{target.damage}].") 
        target.hp-=self.damage
        if target.hp>0:
            print(f"{target.name} is damaged.\n{target.name}({target.hp}/{target.defaulthp})[{target.damage}]") 
        else:
            print(f"{target.name} is destroyed.\n{target.name}({'0'}/{target.defaulthp})[{target.damage}]") 
            return True
        return False



class NoDamageUnit(Unit):
    def __init__(self, name, hp):
        Unit.__init__(self, name, hp, 0)
        print(f"{self.name}({self.hp}/{Unit.defaulthp}[{self.damage}]) is created.") 



game_start()
one = Unit("Medic", 40, 7)
two = Unit("Firebat", 60, 16)

while not one.attack(two): continue
game_over(two.name)


attack_units = []
attack_units.append(one)


