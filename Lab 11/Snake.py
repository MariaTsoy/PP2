# Imports
import pygame
import time
import random
import sys

# Initializg
pygame.init()

# Create screen
screen = pygame.display.set_mode((800, 500))

# Setting FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Program global vars
GREEN = (100, 200, 100)
BLACK = (0, 0, 0)
SCORE = 0
SCOREAPPLECHECK = 0
APPLECOLLECTED = 0
NEWAPPLE = 1
SCOREFRUITS = 0
SCOREPEARCHECK = 0
PEARCOLLECTED = 0
NEWPEAR = 1
SCOREBANANACHECK = 0
BANANACOLLECTED = 0
NEWBANANA = 1
NOBANANATIME = 0
SCORE4 = 4
SCOREUNDER4 = 8
LEVEL = 1
LENGTH = 1
ALLSNAKE = []
DIR = 0
KEYBEFORE = 0
MUSICPLAYG = 0
SPEED = 3
check = 1
x = 100
y = 80

# Setting up fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("GAMOVER", True, BLACK)


class apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Apple.PNG")
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(25, 800 - 25), random.randint(25, 500 - 25))

    def move(self):
        global NEWAPPLE
        global APPLECOLLECTED
        if not NEWAPPLE:
            APPLECOLLECTED = 0
            self.rect = self.image.get_rect()
            self.rect.center = (random.randint(25, 800 - 25), random.randint(25, 500 - 25))
            NEWAPPLE = 1


class pear(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Pear.PNG")
        self.image = pygame.transform.scale(self.image, (30, 20))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(25, 800 - 25), random.randint(25, 500 - 25))

    def move(self):
        global NEWPEAR
        global PEARCOLLECTED
        if not NEWPEAR:
            PEARCOLLECTED = 0
            self.rect = self.image.get_rect()
            self.rect.center = (random.randint(25, 800 - 25), random.randint(25, 500 - 25))
            NEWPEAR = 1


class banana(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Banana.PNG")
        self.image = pygame.transform.scale(self.image, (20, 25))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(25, 800 - 25), random.randint(25, 500 - 25))

    def move(self):
        global NEWBANANA
        global BANANACOLLECTED
        if not NEWBANANA:
            BANANACOLLECTED = 0
            self.rect = self.image.get_rect()
            self.rect.center = (random.randint(25, 800 - 25), random.randint(25, 500 - 25))
            NEWBANANA = 1


class snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.draw.rect(screen, GREEN, [x, y, 20, 20])
        self.rect = pygame.Rect(x, y, 20, 20)

    def move(self, all_snake):
        for i in all_snake:
            pygame.draw.rect(screen, GREEN, [i[0], i[1], 20, 20])
        self.rect = pygame.Rect(x, y, 20, 20)


# Function for quitting after game over
def quit():
    stop_music()
    time.sleep(1/3)
    screen.fill((240, 80, 90))
    screen.blit(game_over, (235, 200))
    pygame.mixer.music.load("sadsound.wav")
    pygame.mixer.music.play()
    pygame.display.update()
    time.sleep(3)
    pygame.quit()
    sys.exit()


# Play music
def play_music():
    pygame.mixer.music.load("music2.mp3")
    pygame.mixer.music.play()


# Stop music
def stop_music():
    pygame.mixer.music.stop()


# Objects from our classes
A1 = apple()
apples = pygame.sprite.Group()
apples.add(A1)
P1 = pear()
pears = pygame.sprite.Group()
pears.add(P1)
B1 = banana()
bananas = pygame.sprite.Group()
bananas.add(B1)
H1 = snake()
heads = pygame.sprite.Group()
heads.add(H1)

while check:
    # Quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            check = 0

        # Choosing direction
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            if KEYBEFORE != pygame.K_w and KEYBEFORE != pygame.K_s:
                y -= 20
                KEYBEFORE = pygame.K_w
                DIR = "up"
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            if KEYBEFORE != pygame.K_a and KEYBEFORE != pygame.K_d:
                x -= 20
                KEYBEFORE = pygame.K_a
                DIR = "left"
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            if KEYBEFORE != pygame.K_s and KEYBEFORE != pygame.K_w:
                y += 20
                KEYBEFORE = pygame.K_s
                DIR = "down"
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            if KEYBEFORE != pygame.K_d and KEYBEFORE != pygame.K_a:
                x += 20
                KEYBEFORE = pygame.K_d
                DIR = "right"

    # Play music at the beginning
    if not MUSICPLAYG:
        play_music()
        MUSICPLAYG = 1

    # Yellow background
    screen.fill((255, 255, 100))

    # Showing score and level
    score = font_small.render("Score: " + str(SCOREFRUITS), True, BLACK)
    screen.blit(score, (800 - 110, 10))
    level = font_small.render("Level: " + str(LEVEL), True, BLACK)
    screen.blit(level, (10, 10))

    # Moving objects
    H1.move(ALLSNAKE)
    A1.move()
    P1.move()
    B1.move()

    # Continue moving in chosen direction
    if DIR == "down":
        y += SPEED
    elif DIR == "up":
        y -= SPEED
    elif DIR == "left":
        x -= SPEED
    elif DIR == "right":
        x += SPEED

    # Game over if hit wall or self
    if y >= 480 or y <= 0 or x >= 780 or x <= 0:
        quit()
    for i in ALLSNAKE[:-1]:
        if x == ALLSNAKE[-1]:
            quit()

    # Append current coordinates of head to coordinates of all snake
    current_head = []
    current_head.append(x)
    current_head.append(y)
    ALLSNAKE.append(current_head)

    # Delete the end of a snake if length didn't grow
    if len(ALLSNAKE) > LENGTH:
        del ALLSNAKE[0]

    # If collected fruit: +length, +score
    if pygame.sprite.spritecollideany(H1, apples):
        pygame.mixer.Sound('coin.mp3').play()
        APPLECOLLECTED = 1
        LENGTH += 1

    if pygame.sprite.spritecollideany(H1, pears):
        pygame.mixer.Sound('coin.mp3').play()
        PEARCOLLECTED = 1
        LENGTH += 1

    if pygame.sprite.spritecollideany(H1, bananas):
        if NOBANANATIME < 240:
            pygame.mixer.Sound('coin.mp3').play()
            BANANACOLLECTED = 1
            LENGTH += 1

    # Level up if score >= 4. Speed up
    if SCOREFRUITS >= SCORE4 and SCOREFRUITS < SCOREUNDER4:
        FPS += 10
        LEVEL += 1
        SCORE4 += 4
        SCOREUNDER4 += 4

    # Continue displaying fruit if not collected
    # Plus score if collected + making new fruit
    if not APPLECOLLECTED:
        for entity in apples:
            screen.blit(entity.image, entity.rect)
    else:
        if NEWAPPLE == 1:
            SCOREFRUITS += 1
            NEWAPPLE = 0

    if not PEARCOLLECTED:
        for entity in pears:
            screen.blit(entity.image, entity.rect)
    else:
        if NEWPEAR == 1:
            SCOREFRUITS += 4
            NEWPEAR = 0

    # No banana if not banana time > 240 and < 600
    if not BANANACOLLECTED:
        if NOBANANATIME < 240:
            for entity in bananas:
                screen.blit(entity.image, entity.rect)
                NOBANANATIME += 1
        else:
            if NOBANANATIME < 600:
                NOBANANATIME += 1
            else:
                NOBANANATIME = 0
    else:
        NOBANANATIME = 240
        if NEWBANANA == 1:
            SCOREFRUITS += 2
            NEWBANANA = 0

    pygame.display.update()
    FramePerSec.tick(FPS)
