import pygame
import random

#게임변수 초기화
#게임 화면
pygame.init()
screen = pygame.display.set_mode((480, 640))

#게임루프
running = True
while running:
    #배경 색 지정
    screen.fill((255,255,255))

    #키보드,마우스 이벤트
    for event in pygame.event.get():
        # X버튼 클릭하면 게임 종료
    if event.type==pygame.QUIT:
        pygame.quit()
        exit(0)
        #게임요소 상태 변경

        #화면 전체 업데이트
        pygame.display.flip()

        #게임 종료화면

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
