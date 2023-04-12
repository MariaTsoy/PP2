# Imports
import pygame
import sys
from pygame.locals import *
import random
import time

# Initializing
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE = (0, 0, 255)
RED = (255, 100, 100)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCOREENEMY = 0
SCORECOINS = 0
COINCOLLECTED = 0
NEWCOIN = 1
SCORECOINCHECK = 0
HEVCOINCOLLECTED = 0
NEWHEVCOIN = 1
SCOREHEVCOINCHECK = 0
MUSICPLAYG = 0
COINVISIBLE = 1
HEVCOINVISIBLE = 1

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Background
background = pygame.image.load("AnimatedStreet.png")

# Create a white screen
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        global SCOREENEMY
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > 680:
            SCOREENEMY += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Coin.PNG")
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, SCREEN_WIDTH - 30), 0)

    def move(self):
        global SCORECOINS
        global COINCOLLECTED

        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > 650:
            self.rect.top = 0
            COINCOLLECTED = 0
            self.rect.center = (random.randint(30, SCREEN_WIDTH - 30), 0)
            global SCORECOINCHECK
            SCORECOINCHECK = 0
        if self.rect.bottom < 100:
            global NEWCOIN
            NEWCOIN = 1


class HeavyCoin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Coins.PNG")
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, SCREEN_WIDTH - 30), 0)

    def move(self):
        global SCORECOINS
        global HEVCOINCOLLECTED

        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > 650:
            self.rect.top = 0
            HEVCOINCOLLECTED = 0
            self.rect.center = (random.randint(30, SCREEN_WIDTH - 30), 0)
            global SCOREHEVCOINCHECK
            SCOREHEVCOINCHECK = 0
        if self.rect.bottom < 100:
            global NEWHEVCOIN
            NEWHEVCOIN = 1


# Play and stop music functions
def play_music():
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play()


def stop_music():
    pygame.mixer.music.stop()


# Setting up Sprites
P1 = Player()
E1 = Enemy()
C1 = Coin()
HC1 = HeavyCoin()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
heavy_coins = pygame.sprite.Group()
heavy_coins.add(HC1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

# Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)


while True:
    # Play music at the beginning
    if not MUSICPLAYG:
        play_music()
        MUSICPLAYG = 1

    # Cycles through all events occuring
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.2
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Print background and scores
    DISPLAYSURF.blit(background, (0, 0))
    scores_en = font_small.render(str(SCOREENEMY), True, BLACK)
    DISPLAYSURF.blit(scores_en, (10, 10))
    scores_coin = font_small.render("Coins: " + str(SCORECOINS), True, BLACK)
    DISPLAYSURF.blit(scores_coin, (SCREEN_WIDTH - 100, 10))

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    # To quit if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        stop_music()
        time.sleep(1/3)
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(1)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Move coins
    C1.move()
    HC1.move()

    # If collected coin
    if pygame.sprite.spritecollideany(P1, coins):
        if COINVISIBLE:
            pygame.mixer.Sound('coin.mp3').play()
            SCORECOINCHECK = 1
            COINCOLLECTED = 1

    if pygame.sprite.spritecollideany(P1, heavy_coins):
        if HEVCOINVISIBLE:
            pygame.mixer.Sound('coin.mp3').play()
            SCOREHEVCOINCHECK = 1
            HEVCOINCOLLECTED = 1

    # Continue displaying coin if not and if it does not collide with enemy
    # Plus score if collected
    if not COINCOLLECTED:
        if not pygame.sprite.spritecollideany(E1, coins):
            for entity in coins:
                DISPLAYSURF.blit(entity.image, entity.rect)
                COINVISIBLE = 1
        else:
            COINVISIBLE = 0
    else:
        if SCORECOINCHECK == 1 and NEWCOIN == 1:
            SCORECOINS += 1
            NEWCOIN = 0

    if not HEVCOINCOLLECTED:
        if not pygame.sprite.spritecollideany(E1, heavy_coins):
            if not pygame.sprite.spritecollideany(C1, heavy_coins):
                for entity in heavy_coins:
                    DISPLAYSURF.blit(entity.image, entity.rect)
                    HEVCOINVISIBLE = 1
            else:
                HEVCOINVISIBLE = 0
        else:
            HEVCOINVISIBLE = 0
    else:
        if SCOREHEVCOINCHECK == 1 and NEWHEVCOIN == 1:
            SCORECOINS += 3
            NEWHEVCOIN = 0

    pygame.display.update()
    FramePerSec.tick(FPS)
