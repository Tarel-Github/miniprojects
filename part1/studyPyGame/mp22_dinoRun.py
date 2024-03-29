# dinoRun
import pygame
import os
import random

pygame.init()

ASSETS = './studyPyGame/Assets/'
SCREEN_WIDTH = 1100 # 게임 윈도우 넓이
SCREEN_HEIGHT = 600 # 게임 윈도우 높이
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
icon = pygame.image.load('./studyPyGame/dinoRun.png')
pygame.display.set_icon(icon)

# 배경 이미지
BG = pygame.image.load(os.path.join(f'{ASSETS}Other', 'Track.png'))

# 공룡 이미지
RUNNING = [pygame.image.load(os.path.join(f'{ASSETS}Dino/DinoRun1.png')),
           pygame.image.load(os.path.join(f'{ASSETS}Dino/DinoRun2.png')),]
DUCKING = [pygame.image.load(os.path.join(f'{ASSETS}Dino/DinoDuck1.png')),
           pygame.image.load(os.path.join(f'{ASSETS}Dino/DinoDuck2.png')),] # Dodge
JUMPING = pygame.image.load(os.path.join(f'{ASSETS}Dino/DinoJump.png'))
START = pygame.image.load(os.path.join(f'{ASSETS}Dino/DinoStart.png')) # 첫시작 이미지
DEAD = pygame.image.load(os.path.join(f'{ASSETS}Dino/DinoDead.png')) # 죽음 이미지

# 구름 이미지
CLOUD = pygame.image.load(os.path.join(f'{ASSETS}Other/Cloud.png'))

# 익룡 이미지
BIRD = [pygame.image.load(os.path.join(f'{ASSETS}Bird/Bird1.png')),
        pygame.image.load(os.path.join(f'{ASSETS}Bird/Bird2.png')),]

# 선인장이미지 로드
LARGE_CACTUS = [pygame.image.load(os.path.join(f'{ASSETS}Cactus/LargeCactus1.png')),
                pygame.image.load(os.path.join(f'{ASSETS}Cactus/LargeCactus2.png')),
                pygame.image.load(os.path.join(f'{ASSETS}Cactus/LargeCactus3.png')),]

SMALL_CACTUS = [pygame.image.load(os.path.join(f'{ASSETS}Cactus/SmallCactus1.png')),
                pygame.image.load(os.path.join(f'{ASSETS}Cactus/SmallCactus2.png')),
                pygame.image.load(os.path.join(f'{ASSETS}Cactus/SmallCactus3.png')),]



class Dino: # 공룡 클래스
    X_POS = 80; Y_POS = 310; Y_POS_DUCK = 340; JUMP_VEL = 9.0

    def __init__(self) -> None:
        self.run_img = RUNNING; self.duck_img = DUCKING; self.jump_img = JUMPING
        self.dino_run = True; self.dino_duck = False; self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL # 점프 초기값은 9.0
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect() # 이미지 사각형 정보
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def update(self, userInput) -> None:
        if self.dino_run:
            self.run()
        elif self.dino_duck:
            self.duck()
        elif self.dino_jump:
            self.jump()

        if self.step_index >= 10: self.step_index = 0 # 애니메이션 스텝

        if userInput[pygame.K_UP] and not self.dino_jump: # 점프
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = True
            self.dino_rect.y = self.Y_POS # 이게 없으면 화살표 윗키를 쭉 누르고 있을때 공룡이 하늘로 날아감
        elif userInput[pygame.K_DOWN] and not self.dino_jump: # 수구리
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):# 런
            self.dino_run = True
            self.dino_duck = False
            self.dino_jump = False

    def run(self):
        self.image = self.run_img[self.step_index // 5] # run_img 10 0, 1
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS        
        self.step_index += 1
    
    def duck(self):
        self.image = self.duck_img[self.step_index // 5] # duck_img
        self.dino_rect = self.image.get_rect() # 이미지 사각형 정보
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK # 이미지 높이가 작으니까
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -self.JUMP_VEL: # -9.0이 되면 점프 중단
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL # 9.0으로 초기화

    def draw(self, SCREEN) -> None:
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

class Cloud: # 구름 클래스
    def __init__(self) -> None: # 클래스를 만들면 무조건 init을 추가할 것(설령 초기화 할 것이 없다고 해도)
        self.x = SCREEN_WIDTH + random.randint(300, 500)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self) -> None:
        self.x -= game_speed
        if self.x < -self.width: # 화면밖으로 벗어나면
            self.x = SCREEN_WIDTH + random.randint(1300, 2000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN) -> None:
        SCREEN.blit(self.image, ( self.x, self.y ))

class Obstacle: # 장애물 클래스 (부모)
    def __init__(self, image, type) -> None:
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH # 1100

    def update(self) -> None:
        self.rect.x -= game_speed
        if self.rect.x <= -self.rect.width: # 왼쪽 화면 밖으로 벗어나면
            obstacles.pop() # 장애물 리스트에 하나 꺼내오기

    def draw(self, SCREEN) -> None:
        SCREEN.blit(self.image[self.type], self.rect)

class Bird(Obstacle): # 장애물 클래스 상속한 클래스
    def __init__(self, image) -> None:
        self.type = 0 # 새는 타입 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0 # 0이미지로 시작

    def draw(self, SCREEN) -> None:
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index // 5], self.rect)
        self.index += 1

class LargeCactus(Obstacle):
    def __init__(self, image) -> None:
        self.type = random.randint(0, 2) # 큰 선인장의 종류가 3개라서 그 중 하나를 고름
        super().__init__(image, self.type)
        self.rect.y = 300

class SmallCactus(Obstacle):
    def __init__(self, image) -> None:
        self.type = random.randint(0, 2) # 작은 선인장의 종류가 3개라서 그 중 하나를 고름
        super().__init__(image, self.type)
        self.rect.y = 325


def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0 # 게임 점수
    run = True
    clock = pygame.time.Clock()
    dino = Dino() # 공룡객체 생성
    cloud = Cloud() # 구름객체 생성
    game_speed = 14
    obstacles = [] # 장애물 리스트
    death_count = 0

    font = pygame.font.Font(f'{ASSETS}NanumGothicBold.ttf', size = 20) # 폰트와 크기

    def score():# 함수 내 함수 (점수 표시)
        global points, game_speed
        points += 1
        if points % 100 == 0: # 100점 단위로
            game_speed += 1 # 점수가 높아지면 속도 증가

        txtScore = font.render(f'SCORE : {points}', True, (83,83,83)) # 공룡과 같은 색으로 폰트색을 변경
        txtRect = txtScore.get_rect()
        txtRect.center = (1000, 40)
        SCREEN.blit(txtScore, txtRect)
    # 함수 내 함수 (배경 그리기)
    def background(): # 배경(땅바닥)만 update, draw를 동시에 해주는 함수
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width() #2404
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            x_pos_bg = 0

        x_pos_bg -= game_speed

        
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((255,255,255)) # 배경 흰색
        userInput = pygame.key.get_pressed()
        
        background()
        score()

        cloud.draw(SCREEN) # 구름 애니메이션
        cloud.update() # 구름이 공룡보다 먼저 그려져야함

        dino.draw(SCREEN) # 공룡 그리기
        dino.update(userInput)
                
        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1: # 큰 선인장
                obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2: # 새
                obstacles.append(Bird(BIRD))

        for obs in obstacles:
            obs.draw(SCREEN)
            obs.update()
            # 충돌감지
            if dino.dino_rect.colliderect(obs.rect):
                #pygame.draw.rect(SCREEN, (255,0,0), dino.dino_rect, 3) # 충돌시 붉게 처리
                pygame.time.delay(1500) # 1.5초 딜레이
                death_count += 1 # 사망
                menu(death_count) # 메인 메뉴 화면으로 전환
                
        clock.tick(30) # 30이 기본, 숫자를 올리면 빨라짐
        pygame.display.update()

def menu(death_count): # 메뉴함수
    global points, font
    run = True
    font = pygame.font.Font(f'{ASSETS}NanumGothicBold.ttf', size = 20) # 폰트와 크기

    while run:
        SCREEN.fill((255, 255, 255))

        if death_count == 0: # 최초의 경우
            text = font.render('시작하려면 아무키나 누르세요', True, (83, 83, 83))
            SCREEN.blit(START, (SCREEN_WIDTH // 2 -20, SCREEN_HEIGHT //2 -140))
        elif death_count > 0: # 사-망
            text = font.render('재시작하려면 아무키나 누르세요', True, (83, 83, 83))
            score = font.render(f'SCORE: {points}', True, (83, 83, 83))
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT //2 + 50)
            SCREEN.blit(score, scoreRect)
            SCREEN.blit(DEAD, (SCREEN_WIDTH // 2 -20, SCREEN_HEIGHT //2 -140))

            
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT //2)
        SCREEN.blit(text, textRect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main()

if __name__ =="__main__":
    menu(death_count = 0)

