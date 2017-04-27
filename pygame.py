#coding=UTF-8

import pygame

pygame.init()
ourScreen = pygame.display.set_mode((400,300))
pygame.display.set_caption("파이게임")
finish = False
colorBlue=True
x=30
y=30
clock = pygame.time.Clock()

while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        pygame.display.flip()

    if event.type==pygame.KEYDOWN and event.key == pygame.K_SPACE:
        colorBlue = not colorBlue

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y -=3
    if pressed[pygame.K_DOWN]:
        y +=3
    if pressed[pygame.K_LEFT]:
        x -=3
    if pressed[pygame.K_RIGHT]:
        x +=3
    ourScreen.fill((0,0,0))
    if colorBlue:
        color = (0,128,255)
    else:
        color = (255,255,255)
    pygame.draw.rect(ourScreen,color,pygame.Rect(x,y,60,60))
    pygame.display.flip() #update로 바꾸어도 됨

######################################################
import pygame
pygame.init()
display_width=800
display_height=600

ourScreen = pygame.display.set_mode((display_width,display_height))

myimg = pygame.image.load(r'C:\Users\stu\Desktop\py\myimage.jpg')
def myimg(x,y):
    ourScreen.blit(myimg,(x,y))

x=(display_width * 0.5)
y=(display_height * 0.5)

finished = False
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished=True
    ourScreen.fill((255,255,200))
    myimg(x,y)
    pygame.display.flip()
pygame.quit()
quit()





