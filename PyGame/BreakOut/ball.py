import pygame

# display
size = 1920, 1800
screen = pygame.display.set_mode(size)
pygame.display.set_caption('')
pygame.display.flip()


clock = pygame.time.Clock()
# images
playerJumpLeft = pygame.image.load('images/stay_jump/jump_left.png')
playerJumpRight = pygame.image.load('images/stay_jump/jump_right.png')
playerStand = pygame.image.load('images/stay_jump/stay.png')
playerJump = pygame.image.load('images/stay_jump/jump.png')
background_image = pygame.image.load('images/fon6.png')
walkRight = [pygame.image.load('images/walk_right/character_malePerson_walk0.png'),
             pygame.image.load('images/walk_right/character_malePerson_walk1.png'),
             pygame.image.load('images/walk_right/character_malePerson_walk2.png'),
             pygame.image.load('images/walk_right/character_malePerson_walk3.png'),
             pygame.image.load('images/walk_right/character_malePerson_walk4.png'),
             pygame.image.load('images/walk_right/character_malePerson_walk5.png'),
             pygame.image.load('images/walk_right/character_malePerson_walk6.png'),
             pygame.image.load('images/walk_right/character_malePerson_walk7.png')]

walkLeft = [pygame.image.load('images/walk_left/left_0.png'),
            pygame.image.load('images/walk_left/left_1.png'),
            pygame.image.load('images/walk_left/left_2.png'),
            pygame.image.load('images/walk_left/left_3.png'),
            pygame.image.load('images/walk_left/left_4.png'),
            pygame.image.load('images/walk_left/left_5.png'),
            pygame.image.load('images/walk_left/left_6.png'),
            pygame.image.load('images/walk_left/left_7.png')]

# player
x = int(50)
y = int(620)
width = int(192)
height = int(256)
speed = 20
lastMove = 'right'
bullets = []

# action
isJump = False
jumpCount = 10

left = True
right = False
anmCount = 0


class Bomb:
    def __init__(self, a, b, radius, color, face):
        self.a = a
        self.b = b
        self.radius = radius
        self.color = color
        self.face = face
        self.vel = 8 * face

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.a, self.b), self.radius)


def render():
    global anmCount

    screen.blit(background_image, (0, 0))

    if anmCount + 1 >= 8:
        anmCount = 0

    if left and not isJump:
        screen.blit(walkLeft[anmCount], (x, y))
        anmCount += 1
    elif right and not isJump:
        screen.blit(walkRight[anmCount], (x, y))
        anmCount += 1
    elif isJump:
        screen.blit(playerJump, (x, y))
    elif isJump and left:
        screen.blit(playerJumpLeft[anmCount], (x, y))
        anmCount += 1
    elif isJump and right:
        screen.blit(playerJumpRight[anmCount], (x, y))
        anmCount += 1
    else:
        screen.blit(playerStand, (x, y))

    for bull in bullets:
        bull.draw(screen)

    pygame.display.update()


run = True
# game loop


while run:
    clock.tick(60)

    pygame.time.delay(10)
    for event in pygame.event.get():
        if event == pygame.QUIT:
            run = False

        for bullet in bullets:
            if 2000 > bullet.a > 0:
                bullet.a += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

    button = pygame.key.get_pressed()

    if button[pygame.K_f]:
        if lastMove == 'right':
            facing = 10
        else:
            facing = -10

        if len(bullets) < 5:
            bullets.append((Bomb(round(x + width // 2), round(y + height // 2), 5, (255, 0, 0), facing)))
    if button[pygame.K_LEFT] and x > 5:
        x -= speed
        right = False
        left = True
    elif button[pygame.K_RIGHT] and x < 1925 - 192:
        x += speed
        left = False
        right = True
    else:
        left = False
        right = False
        anmCount = 0
    if not isJump:
        if button[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    render()

pygame.quit()
