import pygame
from os import path
pygame.init()

# Se crea la ventana donde se va a mostrar todo y se le define el tamaño 
win = pygame.display.set_mode((500,480))

# Se le pone un titulo a la ventana 
pygame.display.set_caption("Primer Pygame")

bg = pygame.image.load(path.join('Sprites','bg.jpg'))

char = pygame.image.load(path.join('Sprites', 'standing.png'))

# Clock speed
clock = pygame.time.Clock()

class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isjumping = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = False
        self.hitbox = (self.x + 20, self.y + 10, 28, 55) 

        # Cargamos las imagenes que utuilizaremos como sprites
        self.walkRight = [pygame.image.load(path.join('Sprites','R1.png')), pygame.image.load(path.join('Sprites','R2.png')), pygame.image.load(path.join('Sprites','R3.png')),
                      pygame.image.load(path.join('Sprites','R4.png')), pygame.image.load(path.join('Sprites','R5.png')), pygame.image.load(path.join('Sprites','R6.png')),
                      pygame.image.load(path.join('Sprites','R7.png')), pygame.image.load(path.join('Sprites','R8.png')), pygame.image.load(path.join('Sprites','R9.png'))]

        self.walkLeft =  [pygame.image.load(path.join('Sprites','L1.png')), pygame.image.load(path.join('Sprites','L2.png')), pygame.image.load(path.join('Sprites','L3.png')),
                      pygame.image.load(path.join('Sprites','L4.png')), pygame.image.load(path.join('Sprites','L5.png')), pygame.image.load(path.join('Sprites','L6.png')),
                      pygame.image.load(path.join('Sprites','L7.png')), pygame.image.load(path.join('Sprites','L8.png')), pygame.image.load(path.join('Sprites','L9.png'))]

    def draw(self, win):
        
        
        # Dibujamos los sprites
        if self.walkCount + 1 >= 27:
            man1.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(self.walkLeft[self.walkCount//3], (self.x,man1.y))
                self.walkCount += 1    
            elif self.right:
                win.blit(self.walkRight[self.walkCount//3], (self.x,man1.y))
                self.walkCount +=1
        else:
            if self.right:
                win.blit(self.walkRight[0], (self.x, self.y))
            else:
                win.blit(self.walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 20, self.y + 10, 28, 55)        
        pygame.draw.rect(win, (255, 0, 255), self.hitbox, 1)

            #win.blit(char, (self.x,self.y))

class Projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing
        self.hitbox = (self.x + 17, self.y + 11, 29, 52) 

    def draw(self,win):
        # ASi se dibuja un circulo en pygame:
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

class Enemy(object):
    walkRight = [pygame.image.load(path.join('Sprites','R1E.png')), pygame.image.load(path.join('Sprites','R2E.png')), pygame.image.load(path.join('Sprites','R3E.png')),
                 pygame.image.load(path.join('Sprites','R4E.png')), pygame.image.load(path.join('Sprites','R5E.png')), pygame.image.load(path.join('Sprites','R6E.png')),
                 pygame.image.load(path.join('Sprites','R7E.png')), pygame.image.load(path.join('Sprites','R8E.png')), pygame.image.load(path.join('Sprites','R9E.png')),
                 pygame.image.load(path.join('Sprites','R10E.png')), pygame.image.load(path.join('Sprites','R11E.png'))]

    walkLeft =  [pygame.image.load(path.join('Sprites','L1E.png')), pygame.image.load(path.join('Sprites','L2E.png')), pygame.image.load(path.join('Sprites','L3E.png')),
                 pygame.image.load(path.join('Sprites','L4E.png')), pygame.image.load(path.join('Sprites','L5E.png')), pygame.image.load(path.join('Sprites','L6E.png')),
                 pygame.image.load(path.join('Sprites','L7E.png')), pygame.image.load(path.join('Sprites','L8E.png')), pygame.image.load(path.join('Sprites','L9E.png')),
                 pygame.image.load(path.join('Sprites','L10E.png')), pygame.image.load(path.join('Sprites','L11E.png'))]
    
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pathh = [x, end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)

    def draw(self, win):

        self.move()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0
        
        if self.vel > 0:
            win.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)  
        pygame.draw.rect(win, (255, 0, 0), self.hitbox , 1)

    def move(self):
        if self.vel > 0:
            if self.x < self.pathh[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        
        else:
            if self.x > self.pathh[0] - self.vel:
                self.x += self.vel
            
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0

    def hit(self):
        print("hit")

def redrawGameWindow():
    # Para poder mostrarlo se hacer un refresco a la pantalla
    win.blit(bg, (0,0)) # Colocamos la imagen bg de fondo 
    man1.draw(win) 
    enemy1.draw(win)

    for bullet in bullets:
        bullet.draw(win)

    # Codigo de como dibujar un rectangulo
    #pygame.draw.rect(win, (255,0,0), (x, y, width, height))
    
    pygame.display.update()   

# Ceamoos el caracter
#             posx posy 
man1 = Player(300, 410, 64, 64)
enemy1 = Enemy(100, 420, 64, 64, 200)
# Cramos las balas 
bullets = []
bulletavailable = True
bulletcooldown = 4

# This is the main loop 
run = True
while run:
    clock.tick(27)
    
    if bulletavailable == False:
        bulletcooldown -= 1
        bulletavailable = True if bulletcooldown == 0 else False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for x, bullet in enumerate(bullets):
        if bullet.y - bullet.radius < enemy1.hitbox[1] + enemy1.hitbox[3] and  bullet.y + bullet.radius > enemy1.hitbox[1]:
            if bullet.x + bullet.radius > enemy1.hitbox[0] and bullet.x - bullet.radius < enemy1.hitbox[0] + enemy1.hitbox[2]:
                enemy1.hit()
                bullets.pop(x)
        
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(x)


    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and bulletavailable:
        bulletcooldown = 4
        facing = 1 if man1.right else -1           
        if len(bullets) < 5:
            bulletavailable = False
            bullets.append(Projectile(round(man1.x + man1.width//2), round(man1.y + man1.height//2), 6, (255,255,255), facing))

    if keys[pygame.K_LEFT] and man1.x > 0:
        man1.x -= man1.vel       
        man1.left = True
        man1.right = False
        man1.standing = False
    
    elif keys[pygame.K_RIGHT] and man1.x < (500 - man1.width):
        man1.x += man1.vel
        man1.right = True
        man1.left = False
        man1.standing = False
    
    else:
        man1.standing = True
        man1.walkcount = 0

    if not(man1.isjumping):
        if keys[pygame.K_UP]:
            man1.isjumping = True
            man1.right = False
            man1.left = False

    else:
        if man1.jumpCount >= -10:
            neg = 1
            if man1.jumpCount < 0:
                neg = -1
            y_ayer = man1.y
            man1.y -= (man1.jumpCount ** 2) * 0.5 * neg
            y_dif = abs(man1.y - y_ayer)
            man1.jumpCount -= 1

        else:
            man1.isjumping = False
            man1.jumpCount = 10        

    # Llamamos la funcion que dibuja     
    redrawGameWindow()


pygame.quit()    