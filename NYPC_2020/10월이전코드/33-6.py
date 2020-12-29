import pygame, sys, random

class Car(pygame.sprite.Sprite):
    def __init__(self, y_location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("car1.png")
        self.rect = self.image.get_rect()
        self.speed = random.randint(1,10)
        self.rect.x = SCREEN_WIDTH
        self.rect.y = y_location
        
    def update(self):
        self.rect.x = self.rect.x - self.speed
        if self.rect.x < 0:
            self.rect.x = SCREEN_WIDTH
            self.speed = random.randint(1,10)


def printText(string, x, y):
    text = pygame.font.SysFont('Comic Sans MS', 20)
    textsurface = text.render(string, False, YELLOW)
    screen.blit(textsurface, (x, y))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("man.png")
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH/2
        self.rect.y = 0
        
    def update(self):
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > SCREEN_LENGTH - 60:
            self.rect.y = SCREEN_LENGTH - 60
        elif self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > SCREEN_WIDTH - 30:
            self.rect.x = SCREEN_WIDTH - 30

    def goLeft(self):
        self.rect.x -= 5
    def goRight(self):
        self.rect.x += 5
    def goUp(self):
        self.rect.y -= 5
    def goDown(self):
        self.rect.y += 5


pygame.init()

WHITE=(255,255,255)
YELLOW=(255,255,0)
SCREEN_WIDTH = 800
SCREEN_LENGTH = 600
size=[SCREEN_WIDTH,SCREEN_LENGTH]
screen = pygame.display.set_mode(size)
screen.fill(WHITE)
clock = pygame.time.Clock()

figureGroup = pygame.sprite.Group()
exfigure1 = Car(100)
figureGroup.add(exfigure1)
exfigure2 = Car(150)
figureGroup.add(exfigure2)
exfigure3 = Car(200)
figureGroup.add(exfigure3)
exfigure4 = Car(250)
figureGroup.add(exfigure4)
exfigure5 = Car(300)
figureGroup.add(exfigure5)
character = Player()
figureGroup.add(character)

count = 0
while True:
    clock.tick(60)
    figureGroup.update()
    figureGroup.draw(screen)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]==1:
        character.goLeft()
    if keys[pygame.K_RIGHT]==1:
        character.goRight()
    if keys[pygame.K_UP]==1:
        character.goUp()
    if keys[pygame.K_DOWN]==1:
        character.goDown()

    hitBlockList = pygame.sprite.spritecollide(character, figureGroup, False)
    printText(str(hitBlockList),100,100)

    if len(hitBlockList) > 1:
        character.rect.x = SCREEN_WIDTH/2
        character.rect.y = 0
        printText("GAME OVER",200,100)
        for block in hitBlockList:
            count += 1
        # count 를 피규어 그룹 말고 다른곳에 넣어야 리스트 길이 측정가능5
        if count > 5 :
            pygame.quit()
            sys.exit()
       
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    screen.fill(WHITE)
