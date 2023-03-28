import pygame
import datetime

pygame.init()
screen = pygame.display.set_mode((640, 480))

clock = pygame.image.load('mickeyclock.jpg')
clock = pygame.transform.scale(clock, (640, 480))
hand1 = pygame.image.load('hand1.PNG')
hand1 = pygame.transform.scale(hand1, (460, 460))
hand2 = pygame.image.load('hand2.PNG')
hand2 = pygame.transform.scale(hand2, (450, 450))

check = True
date = datetime.datetime.now()
mins = date.minute
secs = date.second
print("\nCurrent time:", mins, secs)
angle1 = 0 - (secs * 6) + (10 * 6)
angle2 = 0 - (mins * 6) - (9 * 6)


while check:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            check = False

    screen.fill((255, 255, 255))

    hand1_copy = pygame.transform.rotate(hand1, angle1)
    hand2_copy = pygame.transform.rotate(hand2, angle2)

    screen.blit(clock, (0, 0))
    screen.blit(hand1_copy, (320 - int(hand1_copy.get_width() / 2), 240 - int(hand1_copy.get_height() / 2)))

    if ((angle1 - (11 * 6)) % 360) == 0:
        angle2 -= 6
        screen.blit(hand2_copy, (320 - int(hand2_copy.get_width() / 2), 240 - int(hand2_copy.get_height() / 2)))
    else:
        screen.blit(hand2_copy, (320 - int(hand2_copy.get_width() / 2), 240 - int(hand2_copy.get_height() / 2)))

    angle1 -= 6

    pygame.display.flip()
    pygame.time.Clock().tick(1)
