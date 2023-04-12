import pygame

# Other var-s
LINEMOD = 0
ERASERMOD = 0
CIRCLEMOD = 0
RECTMOD = 0
SQMOD = 0
RHMOD = 0
ETRMOD = 0
RTRMOD = 0


# Buttons for design
eraserbutton = pygame.image.load('Eraser.PNG')
eraserbutton = pygame.transform.scale(eraserbutton, (40, 40))
eraserbuttonrect = eraserbutton.get_rect()
eraserbuttonrect.topleft = (40, 40)
linebutton = pygame.image.load('Pencil.PNG')
linebutton = pygame.transform.scale(linebutton, (40, 40))
linebuttonrect = linebutton.get_rect()
linebuttonrect.topleft = (90, 40)
f5button = pygame.image.load('F5.PNG')
f5button = pygame.transform.scale(f5button, (40, 40))
f5buttonrect = f5button.get_rect()
f5buttonrect.topleft = (240, 40)

sqbutton = pygame.image.load('Square.PNG')
sqbutton = pygame.transform.scale(sqbutton, (40, 40))
sqbuttonrect = sqbutton.get_rect()
sqbuttonrect.topleft = (40, 90)
rtrbutton = pygame.image.load('Rtriangle.PNG')
rtrbutton = pygame.transform.scale(rtrbutton, (40, 40))
rtrbuttonrect = rtrbutton.get_rect()
rtrbuttonrect.topleft = (90, 90)
etrbutton = pygame.image.load('Etriangle.PNG')
etrbutton = pygame.transform.scale(etrbutton, (40, 40))
etrbuttonrect = etrbutton.get_rect()
etrbuttonrect.topleft = (140, 90)
rhombutton = pygame.image.load('Rhombus.PNG')
rhombutton = pygame.transform.scale(rhombutton, (40, 40))
rhombuttonrect = rhombutton.get_rect()
rhombuttonrect.topleft = (190, 90)
circlebutton = pygame.image.load('Circle.PNG')
circlebutton = pygame.transform.scale(circlebutton, (40, 40))
circlebuttonrect = circlebutton.get_rect()
circlebuttonrect.topleft = (140, 40)
rectbutton = pygame.image.load('Rect.PNG')
rectbutton = pygame.transform.scale(rectbutton, (40, 40))
rectbuttonrect = rectbutton.get_rect()
rectbuttonrect.topleft = (190, 40)


def main():
    global LINEMOD
    global ERASERMOD
    global CIRCLEMOD
    global RECTMOD
    global SQMOD
    global RTRMOD
    global ETRMOD
    global RHMOD
    pygame.init()
    screen = pygame.display.set_mode((900, 700))
    clock = pygame.time.Clock()

    # Drawing icons
    def drawicons():
        pygame.draw.rect(screen, (255, 255, 255), (30, 30, 260, 110))
        screen.blit(eraserbutton, eraserbuttonrect)
        screen.blit(linebutton, linebuttonrect)
        screen.blit(circlebutton, circlebuttonrect)
        screen.blit(rectbutton, rectbuttonrect)
        screen.blit(f5button, f5buttonrect)
        screen.blit(sqbutton, sqbuttonrect)
        screen.blit(rtrbutton, rtrbuttonrect)
        screen.blit(etrbutton, etrbuttonrect)
        screen.blit(rhombutton, rhombuttonrect)
        pygame.draw.rect(screen, (255, 255, 255), (440, 30, 170, 90))
        pygame.draw.rect(screen, (250, 100, 100), (450, 40, 30, 30))
        pygame.draw.rect(screen, (100, 100, 250), (490, 40, 30, 30))
        pygame.draw.rect(screen, (100, 250, 100), (530, 40, 30, 30))
        pygame.draw.rect(screen, (165, 70, 255), (570, 40, 30, 30))
        pygame.draw.rect(screen, (255, 131, 195), (450, 80, 30, 30))
        pygame.draw.rect(screen, (255, 248, 231), (490, 80, 30, 30))
        pygame.draw.rect(screen, (255, 179, 71), (530, 80, 30, 30))
        pygame.draw.rect(screen, (255, 211, 66), (570, 80, 30, 30))

    # Color buttons
    redbutton = pygame.draw.rect(screen, (250, 100, 100), (450, 40, 30, 30))
    bluebutton = pygame.draw.rect(screen, (100, 100, 250), (490, 40, 30, 30))
    greenbutton = pygame.draw.rect(screen, (100, 250, 100), (530, 40, 30, 30))
    purplebutton = pygame.draw.rect(screen, (165, 70, 255), (570, 40, 30, 30))
    pinkbutton = pygame.draw.rect(screen, (255, 131, 195), (450, 80, 30, 30))
    whitebutton = pygame.draw.rect(screen, (255, 248, 231), (490, 80, 30, 30))
    orangebutton = pygame.draw.rect(screen, (255, 179, 71), (530, 80, 30, 30))
    yellowbutton = pygame.draw.rect(screen, (255, 211, 66), (570, 80, 30, 30))

    radius = 15
    mode = 'blue'
    points = []

    while True:
        drawicons()

        pressed = pygame.key.get_pressed()

        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            # determine if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return

                if event.key == pygame.K_UP:  # Up arrow grows radius
                    radius = min(200, radius + 1)
                elif event.key == pygame.K_DOWN:  # Down arrow shrinks radius
                    radius = max(1, radius - 1)

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Color mods selection
                if event.button == 1 and redbutton.collidepoint(pygame.mouse.get_pos()):
                    mode = 'red'
                    points = []
                if event.button == 1 and greenbutton.collidepoint(pygame.mouse.get_pos()):
                    mode = 'green'
                    points = []
                if event.button == 1 and bluebutton.collidepoint(pygame.mouse.get_pos()):
                    mode = 'blue'
                    points = []
                if event.button == 1 and purplebutton.collidepoint(pygame.mouse.get_pos()):
                    mode = 'violet'
                    points = []
                if event.button == 1 and pinkbutton.collidepoint(pygame.mouse.get_pos()):
                    mode = 'pink'
                    points = []
                if event.button == 1 and yellowbutton.collidepoint(pygame.mouse.get_pos()):
                    mode = 'yellow'
                    points = []
                if event.button == 1 and whitebutton.collidepoint(pygame.mouse.get_pos()):
                    mode = 'white'
                    points = []
                if event.button == 1 and orangebutton.collidepoint(pygame.mouse.get_pos()):
                    mode = 'orange'
                    points = []

                # Mods (line, eraser, shapes)
                if event.button == 1 and linebuttonrect.collidepoint(pygame.mouse.get_pos()):
                    if ERASERMOD:
                        ERASERMOD = not ERASERMOD
                    if CIRCLEMOD:
                        CIRCLEMOD = not CIRCLEMOD
                    if RECTMOD:
                        RECTMOD = not RECTMOD
                    if RTRMOD:
                        RTRMOD = not RTRMOD
                    if ETRMOD:
                        ETRMOD = not ETRMOD
                    if RHMOD:
                        RHMOD = not RHMOD
                    if SQMOD:
                        SQMOD = not SQMOD
                    LINEMOD = not LINEMOD
                    points = []

                if event.button == 1 and eraserbuttonrect.collidepoint(pygame.mouse.get_pos()):
                    if LINEMOD:
                        LINEMOD = not LINEMOD
                    if CIRCLEMOD:
                        CIRCLEMOD = not CIRCLEMOD
                    if RECTMOD:
                        RECTMOD = not RECTMOD
                    if RTRMOD:
                        RTRMOD = not RTRMOD
                    if ETRMOD:
                        ETRMOD = not ETRMOD
                    if RHMOD:
                        RHMOD = not RHMOD
                    if SQMOD:
                        SQMOD = not SQMOD
                    ERASERMOD = not ERASERMOD
                    points = []

                if event.button == 1 and f5buttonrect.collidepoint(pygame.mouse.get_pos()):
                    if LINEMOD:
                        LINEMOD = not LINEMOD
                    if ERASERMOD:
                        ERASERMOD = not ERASERMOD
                    screen.fill((0, 0, 0))
                    drawicons()

                if event.button == 1 and circlebuttonrect.collidepoint(pygame.mouse.get_pos()):
                    if LINEMOD:
                        LINEMOD = not LINEMOD
                    if ERASERMOD:
                        ERASERMOD = not ERASERMOD
                        points = []
                    if RECTMOD:
                        RECTMOD = not RECTMOD
                    if RTRMOD:
                        RTRMOD = not RTRMOD
                    if ETRMOD:
                        ETRMOD = not ETRMOD
                    if RHMOD:
                        RHMOD = not RHMOD
                    if SQMOD:
                        SQMOD = not SQMOD
                    CIRCLEMOD = not CIRCLEMOD

                if event.button == 1 and rectbuttonrect.collidepoint(pygame.mouse.get_pos()):
                    if LINEMOD:
                        LINEMOD = not LINEMOD
                    if ERASERMOD:
                        ERASERMOD = not ERASERMOD
                        points = []
                    if CIRCLEMOD:
                        CIRCLEMOD = not CIRCLEMOD
                    if RTRMOD:
                        RTRMOD = not RTRMOD
                    if ETRMOD:
                        ETRMOD = not ETRMOD
                    if RHMOD:
                        RHMOD = not RHMOD
                    if SQMOD:
                        SQMOD = not SQMOD
                    RECTMOD = not RECTMOD

                if event.button == 1 and sqbuttonrect.collidepoint(pygame.mouse.get_pos()):
                    if LINEMOD:
                        LINEMOD = not LINEMOD
                    if ERASERMOD:
                        ERASERMOD = not ERASERMOD
                        points = []
                    if RECTMOD:
                        RECTMOD = not RECTMOD
                    if RTRMOD:
                        RTRMOD = not RTRMOD
                    if ETRMOD:
                        ETRMOD = not ETRMOD
                    if RHMOD:
                        RHMOD = not RHMOD
                    if CIRCLEMOD:
                        CIRCLEMOD = not CIRCLEMOD
                    SQMOD = not SQMOD

                if event.button == 1 and rhombuttonrect.collidepoint(pygame.mouse.get_pos()):
                    if LINEMOD:
                        LINEMOD = not LINEMOD
                    if ERASERMOD:
                        ERASERMOD = not ERASERMOD
                        points = []
                    if RECTMOD:
                        RECTMOD = not RECTMOD
                    if RTRMOD:
                        RTRMOD = not RTRMOD
                    if ETRMOD:
                        ETRMOD = not ETRMOD
                    RHMOD = not RHMOD
                    if CIRCLEMOD:
                        CIRCLEMOD = not CIRCLEMOD
                    if SQMOD:
                        SQMOD = not SQMOD

                if event.button == 1 and rtrbuttonrect.collidepoint(pygame.mouse.get_pos()):
                    if LINEMOD:
                        LINEMOD = not LINEMOD
                    if ERASERMOD:
                        ERASERMOD = not ERASERMOD
                        points = []
                    if RECTMOD:
                        RECTMOD = not RECTMOD
                    if ETRMOD:
                        ETRMOD = not ETRMOD
                    if RHMOD:
                        RHMOD = not RHMOD
                    if CIRCLEMOD:
                        CIRCLEMOD = not CIRCLEMOD
                    if SQMOD:
                        SQMOD = not SQMOD
                    RTRMOD = not RTRMOD

                if event.button == 1 and etrbuttonrect.collidepoint(pygame.mouse.get_pos()):
                    if LINEMOD:
                        LINEMOD = not LINEMOD
                    if ERASERMOD:
                        ERASERMOD = not ERASERMOD
                        points = []
                    if RECTMOD:
                        RECTMOD = not RECTMOD
                    if RHMOD:
                        RHMOD = not RHMOD
                    if CIRCLEMOD:
                        CIRCLEMOD = not CIRCLEMOD
                    if SQMOD:
                        SQMOD = not SQMOD
                    if RTRMOD:
                        RTRMOD = not RTRMOD
                    ETRMOD = not ETRMOD

                # Taking first position if in shape mode and mouse clicked
                if event.button == 1 and CIRCLEMOD or RECTMOD or SQMOD or RHMOD or RTRMOD or ETRMOD:
                    coord1 = position

            # Taking second position and drawing shapes when mouse button released
            if event.type == pygame.MOUSEBUTTONUP:
                if CIRCLEMOD:
                    circlecoord2 = position
                    drawCircle(screen, mode, coord1, circlecoord2)
                    drawicons()
                if RECTMOD:
                    rectcoord2 = position
                    drawRect(screen, mode, coord1, rectcoord2)
                    drawicons()
                if SQMOD:
                    sqcoord2 = position
                    drawSquare(screen, mode, coord1, sqcoord2)
                    drawicons()
                if RHMOD:
                    rhcoord2 = position
                    drawRhombus(screen, mode, coord1, rhcoord2)
                    drawicons()
                if RTRMOD:
                    rtrcoord2 = position
                    drawRtriangle(screen, mode, coord1, rtrcoord2)
                    drawicons()
                if ETRMOD:
                    etrcoord2 = position
                    drawEtriangle(screen, mode, coord1, etrcoord2)
                    drawicons()

            # Taking all points to draw line
            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list
                if not linebuttonrect.collidepoint(pygame.mouse.get_pos()):
                    position = event.pos
                    points = points + [position]
                    points = points[-256:]

        # Draw all points
        if LINEMOD:
            i = 0
            while i < len(points) - 1:
                drawLineBetween(screen, points[i], points[i + 1], radius, mode)
                i += 1
            drawicons()

        if ERASERMOD:
            i = 0
            while i < len(points) - 1:
                drawLineEraser(screen, points[i], points[i + 1], radius)
                i += 1
            drawicons()

        pygame.display.flip()
        clock.tick(60)


def drawLineEraser(screen, start, end, width):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, (0, 0, 0), (x, y), width)


def drawLineBetween(screen, start, end, width, color_mode):
    if color_mode == 'blue':
        color = (100, 100, 250)
    elif color_mode == 'red':
        color = (250, 100, 100)
    elif color_mode == 'green':
        color = (100, 250, 100)
    elif color_mode == 'violet':
        color = (165, 70, 255)
    elif color_mode == 'pink':
        color = (255, 131, 195)
    elif color_mode == 'yellow':
        color = (255, 211, 66)
    elif color_mode == 'white':
        color = (255, 248, 231)
    elif color_mode == 'orange':
        color = (255, 179, 71)

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)


def drawRhombus(screen, color_mode, pos1, pos2):
    if color_mode == 'blue':
        color = (100, 100, 250)
    elif color_mode == 'red':
        color = (250, 100, 100)
    elif color_mode == 'green':
        color = (100, 250, 100)
    elif color_mode == 'violet':
        color = (165, 70, 255)
    elif color_mode == 'pink':
        color = (255, 131, 195)
    elif color_mode == 'yellow':
        color = (255, 211, 66)
    elif color_mode == 'white':
        color = (255, 248, 231)
    elif color_mode == 'orange':
        color = (255, 179, 71)

    points = [(pos1[0] + (pos2[0] - pos1[0]) / 2, pos1[1]), (pos2[0], pos1[1] + (pos2[1] - pos1[1]) / 2), (pos1[0] + (pos2[0] - pos1[0]) / 2, pos2[1]), (pos1[0], pos1[1] + (pos2[1] - pos1[1]) / 2)]
    pygame.draw.polygon(screen, color, points)


def drawRtriangle(screen, color_mode, pos1, pos2):
    if color_mode == 'blue':
        color = (100, 100, 250)
    elif color_mode == 'red':
        color = (250, 100, 100)
    elif color_mode == 'green':
        color = (100, 250, 100)
    elif color_mode == 'violet':
        color = (165, 70, 255)
    elif color_mode == 'pink':
        color = (255, 131, 195)
    elif color_mode == 'yellow':
        color = (255, 211, 66)
    elif color_mode == 'white':
        color = (255, 248, 231)
    elif color_mode == 'orange':
        color = (255, 179, 71)

    points = [(pos1[0], pos1[1]), (pos2[0], pos2[1]), (pos1[0], pos2[1])]
    pygame.draw.polygon(screen, color, points)


def drawEtriangle(screen, color_mode, pos1, pos2):
    if color_mode == 'blue':
        color = (100, 100, 250)
    elif color_mode == 'red':
        color = (250, 100, 100)
    elif color_mode == 'green':
        color = (100, 250, 100)
    elif color_mode == 'violet':
        color = (165, 70, 255)
    elif color_mode == 'pink':
        color = (255, 131, 195)
    elif color_mode == 'yellow':
        color = (255, 211, 66)
    elif color_mode == 'white':
        color = (255, 248, 231)
    elif color_mode == 'orange':
        color = (255, 179, 71)

    points = [(pos1[0] + (pos2[0] - pos1[0]) / 2, pos1[1]), (pos2[0], pos2[1]), (pos1[0], pos2[1])]
    pygame.draw.polygon(screen, color, points)


def drawCircle(screen, color_mode, pos1, pos2):
    if color_mode == 'blue':
        color = (100, 100, 250)
    elif color_mode == 'red':
        color = (250, 100, 100)
    elif color_mode == 'green':
        color = (100, 250, 100)
    elif color_mode == 'violet':
        color = (165, 70, 255)
    elif color_mode == 'pink':
        color = (255, 131, 195)
    elif color_mode == 'yellow':
        color = (255, 211, 66)
    elif color_mode == 'white':
        color = (255, 248, 231)
    elif color_mode == 'orange':
        color = (255, 179, 71)

    pos = (pos1[0] + ((pos2[0] - pos1[0]) / 2), pos1[1] + ((pos2[1] - pos1[1]) / 2))
    width = min((pos2[0] - pos1[0]) / 2, (pos2[1] - pos1[1]) / 2)
    pygame.draw.circle(screen, color, pos, width)


def drawRect(screen, color_mode, pos1, pos2):
    if color_mode == 'blue':
        color = (100, 100, 250)
    elif color_mode == 'red':
        color = (250, 100, 100)
    elif color_mode == 'green':
        color = (100, 250, 100)
    elif color_mode == 'violet':
        color = (165, 70, 255)
    elif color_mode == 'pink':
        color = (255, 131, 195)
    elif color_mode == 'yellow':
        color = (255, 211, 66)
    elif color_mode == 'white':
        color = (255, 248, 231)
    elif color_mode == 'orange':
        color = (255, 179, 71)

    pygame.draw.rect(screen, color, (pos1[0], pos1[1], pos2[0] - pos1[0], pos2[1] - pos1[1]))


def drawSquare(screen, color_mode, pos1, pos2):
    if color_mode == 'blue':
        color = (100, 100, 250)
    elif color_mode == 'red':
        color = (250, 100, 100)
    elif color_mode == 'green':
        color = (100, 250, 100)
    elif color_mode == 'violet':
        color = (165, 70, 255)
    elif color_mode == 'pink':
        color = (255, 131, 195)
    elif color_mode == 'yellow':
        color = (255, 211, 66)
    elif color_mode == 'white':
        color = (255, 248, 231)
    elif color_mode == 'orange':
        color = (255, 179, 71)

    pos = (pos1[0], pos1[1], min(pos2[0] - pos1[0], pos2[1] - pos1[1]), min(pos2[0] - pos1[0], pos2[1] - pos1[1]))
    pygame.draw.rect(screen, color, pos)


main()
