import pygame

pygame.init()
win = pygame.display.set_mode((1000, 500))

bg_img = pygame.image.load('./studyPyGame/Assets/Background.png')
BG = pygame.transform.scale(bg_img, (1000, 500)) # 스케일 업
pygame.display.set_caption('게임만들기')
icon = pygame.image.load('./studyPyGame/game.png')
pygame.display.set_icon(icon)

width = 1000
loop = 0
run = True
while run :
    win.fill((0,0,0))

    # 이벤트 = 시그널
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # 배경음
    win.blit(BG,(0,0))

    pygame.display.update()
