class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print(f'{self.name} 유닛이 생성되었습니다')
        self.defaulthp=hp

    def move(self, location):
        print("[지상 유닛 이동]")
        print(f"{self.name} : {location} 방향으로 이동합니다. [속도 {self.speed}]")

    def damaged(self, damage):
        print(f"{self.name}({self.hp}/{self.defaulthp}) : {damage} 데미지를 입었습니다")
        self.hp-=damage
        if self.hp<=0:
            print(f"{self.name}(0/{self.defaulthp}) : 파괴되었습니다.")
        else:
            print(f"-> {self.name}({self.hp}/{self.defaulthp})")
    
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, defaulthp, speed)
        self.damage = damage

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        Unit.__init__(self)
        Flyable.__init__(self)


dropship = FlyableUnit()