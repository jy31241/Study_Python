import pygame
import random

#게임변수 초기화
#게임 화면
pygame.init()
screen = pygame.display.set_mode((480, 640))

#시간관련 변수
FPS = 60
fpsClock = pygame.time.Clock()
asteroidtimer = 200

#소행성 위치 변수
asteroids = [[20,0,0]]

try:
#그림과 효과음 삽입
    #그림삽입
    spaceshipimg = pygame.image.load("./img/spaceship.png")
    asteroid0 = pygame.image.load("./img/asteroid00.png")
    asteroid1 = pygame.image.load("./img/asteroid01.png")
    asteroid2 = pygame.image.load("./img/asteroid02.png")
    asteroidimgs = (asteroid0,asteroid1,asteroid2)
    gameover = pygame.image.load("./img/gameover.jpg")

    #효과음 삽입
    #takeoffsound = pygame.mixer.Sound("./img/Super.wav")
    #landingsound = pygame.mixer.Sound("./img/kkk.wav")
    #takeoffsound.play()
except Exception as err:
    print('그림 효과음에 문제가 있습니다.: ', err)
    pygame.quit()
    exit(0)

#점수
score = 0
#점수 출력
def text(arg, x, y):
    font = pygame.font.Font(None,24)
    text = font.render("Score :"+ str(arg).zfill(6), True, (0,0,0)) #점수 6자리/ 검은색
    textRect = text.get_rect()
    textRect.centerx = x
    textRect.centery = y
    screen.blit(text, textRect)

#------------------------게임루프----------------------------
running = True
while running:
    #배경 지정
    background = pygame.image.load("./img/background.png")
    screen.blit(background,(0,0))

    #키보드,마우스 이벤트
    for event in pygame.event.get():
    # X버튼 클릭하면 게임 종료
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)
    #점수증가,게임속도 증가
    score +=15
    text(score,400,10)
    if score % 100 == 0:
        FPS +=2

    #게임요소 상태 변경
        #spaceship 위치/그리기
    position = pygame.mouse.get_pos()
    spaceshippos = (position[0], 600)
    screen.blit(spaceshipimg,spaceshippos)
        #spaceship 사각형
    spaceshiprect = pygame.Rect(spaceshipimg.get_rect())
    spaceshiprect.left = spaceshippos[0]
    spaceshiprect.top = spaceshippos[1]
    #landingsound.play()

    #asteroids 추가하기
    asteroidtimer -=10
    if asteroidtimer <=0:
        asteroids.append([random.randint(5,475),0,random.randint(0,2)]) #소행성 x좌표/y좌표/종류
        asteroidtimer = random.randint(50,200)

    #모든 asteroids 이동
    index = 0
    for stone in asteroids :
        #이동속도- 행성 떨어지는 속도
        stone[1]+=10
        #spaceship에 닿지 않았을 때 640아래로 내려갔을 때
        if stone[1]>640:
            asteroids.pop(index)
        #닿았을 때
        stonerect = pygame.Rect(asteroidimgs[stone[2]].get_rect())
        stonerect.left = stone[0]
        stonerect.top = stone[1]
        if stonerect.colliderect(spaceshiprect):
            #landingsound.play()
            asteroids.pop(index)
            running = False

        #asteroid 그리기
        screen.blit(asteroidimgs[stone[2]], (stone[0],stone[1]))#이미지/스톤 x,y좌표
        index +=1

    #게임속도
    fpsClock.tick(FPS)

    #화면 전체 업데이트
    pygame.display.flip()

    #게임 종료화면
screen.blit(gameover, (80,30))
text(score,screen.get_rect().centerx,screen.get_rect().centery)
pygame.display.flip()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
