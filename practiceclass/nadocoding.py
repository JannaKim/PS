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
        Unit.__init__(self, name, hp, speed) # defaulthp도 가져오나? ㄴㄴ
        self.damage = damage
        self.defaulthp=hp
        print(f'{self.name}({self.hp}/{self.defaulthp})[s:{self.speed} d:{self.damage}] 어택유닛이 생성되었습니다 ')

    def attack(self, location):
        print(f"{self:name}: {self:location} 방향으로 적군을 공격합니다. [공격력 {self:damage}]")


class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "Marine", 40, 1, 5)
        self.defaulthp = 40
        # 스팀팩: 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소
        print(f'{self.name}({self.hp}/{self.defaulthp})[s:{self.speed} d:{self.damage}] 마린이 생성되었습니다 ')

    def steampack(self):
        print('Marine({self.hp}/{self.defaulthp}) 스팀팩 사용하려 합니다.')
        if self.hp>10:
            self.hp-=10
            print(f'Marine이 스팀팩을 사용했습니다. Marine({self.hp}/{self.defaulthp})')
        else:
            print('Marine: 체력이 부족하여 스팀팩을 사용하지 않았습니다')

class Tank(AttackUnit):
    seize_developed = False

    # 시즈모드: 탱크를 지상에 고정시켜 이동불가. 공격력 2배
    def __init__(self):
        AttackUnit.__init__(self, "Tank", 150, 1, 35)
        self.defaulthp = 150
        self.seizemode = False
    def set_seize_mode(self):
        if Tank.seize_developed== False:
            return
        
        # 현재 시드모드가 아닐 때 -> 시즈모드
        if self.seize_mode == False:
            print("Tank 시즈모드 전환합니다")
            self.damage *=2
            self.seize_mode = True

        # 현재 시드모드 일때 -> 시즈모드 해제
        else:
            print("Tank 시즈모드 해제합니다")
            self.damage /=2
            self.seize_mode = False


class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) #지상 speed 0
        self.defaulthp = hp
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("공중 유닛 이동")
        self.fly(self.name, location)

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "Wraith", 80, 20, 5)
        self.clocked = False # 클로킹 모드 (해제 상태)

    def clocking(self):
        if self.clocked ==True:
            print("Clocking mode on")
            self.clocked = False
        else:
            print("Clocking mode released")
            self.clocked =True


        


class FlyableUnit(Flyable, Unit):
    def __init__(self):
        Unit.__init__(self)
        Flyable.__init__(self) 


dropship = FlyableUnit()