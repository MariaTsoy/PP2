import pygame

pygame.init()


def play_next():
    global songs
    songs = songs[1:] + [songs[0]]
    pygame.mixer.music.load(songs[0])
    pygame.mixer.music.play()


def play_previous():
    global songs
    songs = [songs[len(songs) - 1]] + songs[0:len(songs) - 1]
    pygame.mixer.music.load(songs[0])
    pygame.mixer.music.play()


def print_text():
    text1 = font.render('Currently playing:', True, (0, 0, 0))
    textRect1 = text1.get_rect()
    textRect1.topleft = (10, 10)
    screen.blit(text1, textRect1)
    text2 = font.render(songs[0].replace('.mp3', ''), True, (0, 0, 0))
    textRect2 = text2.get_rect()
    textRect2.center = (300, 200)
    screen.blit(text2, textRect2)
    text3 = font.render('1 - play, 0 - stop, 2 - previous, 3 - next', True, (0, 0, 0))
    textRect3 = text3.get_rect()
    textRect3.bottomleft = (10, 390)
    screen.blit(text3, textRect3)
    pygame.display.flip()


def print_nothing():
    text1 = font.render('Currently playing:', True, (0, 0, 0))
    textRect1 = text1.get_rect()
    textRect1.topleft = (10, 10)
    screen.blit(text1, textRect1)
    text2 = font.render('Nothing', True, (0, 0, 0))
    textRect2 = text2.get_rect()
    textRect2.center = (300, 200)
    screen.blit(text2, textRect2)
    text3 = font.render('1 - play, 0 - stop, 2 - previous, 3 - next', True, (0, 0, 0))
    textRect3 = text3.get_rect()
    textRect3.bottomleft = (10, 390)
    screen.blit(text3, textRect3)
    pygame.display.flip()


check = 1
music_stopped = 1
songs = ['Pornofilmy - Papa ne pei.mp3', 'Hatsune Miku - PoPiPo.mp3', 'Inabakumori - Lagtrain.mp3',
         'Hatsune Miku - Sand Planet.mp3']
screen = pygame.display.set_mode((600, 400))
font = pygame.font.Font('La Machine Company.ttf', 20)

while check:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: check = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
            pygame.mixer.music.stop()
            music_stopped = 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            pygame.mixer.music.load(songs[0])
            pygame.mixer.music.play()
            music_stopped = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
            play_next()
            music_stopped = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
            play_previous()
            music_stopped = 0

    screen.fill((255, 255, 255))
    if music_stopped:
        print_nothing()
    else:
        print_text()
