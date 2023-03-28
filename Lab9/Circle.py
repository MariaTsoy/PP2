import pygame

pygame.init()
screen = pygame.display.set_mode((800, 500))

check = 1
blue = True
x = 100
y = 80

while check:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: check = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: blue = not blue
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            if y >= 45:
                y -= 20
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            if x >= 45:
                x -= 20
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            if y <= 455:
                y += 20
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            if x <= 755:
                x += 20
    if blue: color = (110, 110, 170)
    else: color = (170, 110, 170)

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, color, (x, y), 25)

    pygame.display.flip()
    pygame.time.Clock().tick(60)
