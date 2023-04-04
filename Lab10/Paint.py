import pygame

LINEMOD = 1
ERASERMOD = 0


def main():
    global LINEMOD
    global ERASERMOD
    pygame.init()
    screen = pygame.display.set_mode((900, 700))
    clock = pygame.time.Clock()

    font_small = pygame.font.SysFont("Verdana", 15)
    mods = font_small.render("Mods:   1 - Circle   2 - Rectangle   "
                             "3 - Line mode   4 - Eraser mode   5 - Erase all", True, (255, 255, 255))
    colors = font_small.render("Colors:   y - Yellow   r - Red   b - Blue   g - Green   "
                               "p - Pink   v - Violet   c - Cosmic Latte (White)   o - Orange", True, (255, 255, 255))
    setts = font_small.render("Set:   lmb - Thicker   rmb - Thinner   "
                              "alt + f4 - Quit   ctrl + w - Quit", True, (255, 255, 255))
    screen.blit(mods, (10, 635))
    screen.blit(colors, (10, 655))
    screen.blit(setts, (10, 675))

    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []

    while True:
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

                if event.key == pygame.K_1:
                    drawCircle(screen, mode, position, radius)
                if event.key == pygame.K_2:
                    drawRect(screen, mode, position, radius)

                if event.key == pygame.K_3:
                    if ERASERMOD:
                        ERASERMOD = not ERASERMOD
                    LINEMOD = not LINEMOD
                    points = []
                if event.key == pygame.K_4:
                    if LINEMOD:
                        LINEMOD = not LINEMOD
                    if ERASERMOD:
                        ERASERMOD = not ERASERMOD
                        points = []
                    else:
                        ERASERMOD = not ERASERMOD
                        points = []
                if event.key == pygame.K_5:
                    LINEMOD = not LINEMOD
                    ERASERMOD = not ERASERMOD
                    screen.fill((0, 0, 0))
                    screen.blit(mods, (10, 635))
                    screen.blit(colors, (10, 655))
                    screen.blit(setts, (10, 675))

                # determine if a letter key was pressed
                if event.key == pygame.K_r:
                    mode = 'red'
                    points = []
                elif event.key == pygame.K_g:
                    mode = 'green'
                    points = []
                elif event.key == pygame.K_b:
                    mode = 'blue'
                    points = []
                elif event.key == pygame.K_v:
                    mode = 'violet'
                    points = []
                elif event.key == pygame.K_p:
                    mode = 'pink'
                    points = []
                elif event.key == pygame.K_y:
                    mode = 'yellow'
                    points = []
                elif event.key == pygame.K_c:
                    mode = 'white'
                    points = []
                elif event.key == pygame.K_o:
                    mode = 'orange'
                    points = []

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # left click grows radius
                    radius = min(200, radius + 1)
                elif event.button == 3:  # right click shrinks radius
                    radius = max(1, radius - 1)

            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list
                position = event.pos
                points = points + [position]
                points = points[-256:]

        # draw all points
        if LINEMOD:
            i = 0
            while i < len(points) - 1:
                drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
                i += 1

        if ERASERMOD:
            i = 0
            while i < len(points) - 1:
                drawLineEraser(screen, points[i], points[i + 1], radius)
                i += 1

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


def drawLineBetween(screen, index, start, end, width, color_mode):
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


def drawCircle(screen, color_mode, pos, width):
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

    pygame.draw.circle(screen, color, pos, width)


def drawRect(screen, color_mode, pos, width):
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

    pygame.draw.rect(screen, color, (pos[0], pos[1], width * 2, width * 2))


main()
