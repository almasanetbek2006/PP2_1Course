import pygame
import sys
import math
pygame.init()
WIDTH = 960
HEIGHT = 640
colorBlack = (0,0,0)
colorWhite = (255,255,255)
colorRed = (255,0,0)
colorGreen = (0,255,0)
colorBlue = (0 ,0,255)
colorYellow = (255,255,0)
screen = pygame.display.set_mode((WIDTH,HEIGHT))
base_layer = pygame.Surface((WIDTH,HEIGHT))
done = False
lastik = False
LMBpressed = False
rectangle = False
circle = False
square = False
triangle = False
diamond = False
equal_triangle = False
romb = False
color = colorWhite
prevx = 0
prevy = 0
currx = 0
curry = 0
def calculate_rect(x1,y1,x2,y2):
    return pygame.Rect(min(x1,x2),min(y1,y2),abs(x1-x2),abs(y1-y2))
def calculate_circle(x1,y1,x2,y2):
     radius =  int(math.sqrt((x2-x1)*2 + (y2-y1)*2))
     return radius
def calculate_lastik(x1,y1,x2,y2):
      return pygame.Rect(min(x1,x2),min(y1,y2),abs(x1-x2),abs(y1-y2))
def calculate_square(x1, y1, x2, y2):
    size = max(abs(x2 - x1), abs(y2 - y1))
    return pygame.Rect(min(x1,x2),min(y1,y2), size, size)
def calculate_right_triangle(x1,y1,x2,y2):
    sol_zhak = [x1,y1]
    on_zhak = [x2,y2]
    asty = [x1,y2]
    points = [sol_zhak,on_zhak,asty]
    return points

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMBpressed = True
            prevx = event.pos[0]
            prevy = event.pos[1]
        if LMBpressed:
                currx = event.pos[0]
                curry = event.pos[1]
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                lastik = True
                circle= False
                rectangle= False
            if event.key == pygame.K_r:
                rectangle = True
                circle= False
                lastik = False
            if event.key == pygame.K_c:
                 circle = True
                 rectangle= False
                 lastik= False
            if event.key == pygame.K_s:
                square = True
                circle = False
                rectangle= False
                lastik= False
            if event.key == pygame.K_t:
                triangle = True
                square = False
                circle = False
                rectangle= False
                lastik= False
            if event.key == pygame.K_u:
                equal_triangle=True
            if event.key ==pygame.K_1:
                 romb= True
            if event.key==pygame.K_b:
                color = colorBlack
            if event.key==pygame.K_y:
                color = colorYellow
            if event.key==pygame.K_q:
                color=colorRed
            if event.key==pygame.K_g:
                color = colorGreen
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBpressed = False
            if lastik:
                pygame.draw.rect(screen,colorBlack,calculate_lastik(prevx,prevy,currx,curry))
            if rectangle:
                pygame.draw.rect(screen,color,calculate_rect(prevx,prevy,currx,curry),2)
            if circle:
                radius = calculate_circle(prevx,prevy,currx,curry)
                pygame.draw.circle(screen,color,(prevx,prevy),radius,2)
            if square:
                pygame.draw.rect(screen,colorBlue,calculate_square(prevx,prevy,currx,curry),2)
            base_layer.blit(screen,(0,0))
            if triangle:
                points = calculate_right_triangle(prevx,prevy,currx,curry)
                pygame.draw.polygon(screen,color,points,2)
            
    if LMBpressed:
        screen.blit(base_layer,(0,0))
        if lastik:
            pygame.draw.rect(screen,colorYellow,calculate_lastik(prevx,prevy,currx,curry),2)
        if rectangle:
            pygame.draw.rect(screen,color,calculate_rect(prevx,prevy,currx,curry),2)
        if circle:
            radius = calculate_circle(prevx,prevy,currx,curry)
            pygame.draw.circle(screen,color,(prevx,prevy),radius,2)
        if square:
            pygame.draw.rect(screen,colorBlue,calculate_square(prevx,prevy,currx,curry),2)
        if triangle:
                points = calculate_right_triangle(prevx,prevy,currx,curry)
                pygame.draw.polygon(screen,color,points,2)

    pygame.display.flip()