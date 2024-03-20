import pygame
import random

pygame.init()

#game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Drag And Drop')

active_box = None


boxes = []
y=60
for j in range(2):
    x=10
    if(j!=0):
        y+=35
    for i in range(5):
        if(i!=0):
            x +=35
        w = 30
        h = 30
        box = pygame.Rect(x, y, w, h)
        boxes.append(box)

run = True
while run:
    screen.fill("turquoise1")
    #update and draw items
    for box in boxes:
        pygame.draw.rect(screen, "purple", box)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for num, box in enumerate(boxes):
                    if box.collidepoint(event.pos):
                        active_box = num

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                active_box = None

        if event.type == pygame.MOUSEMOTION:
            if active_box != None:
                boxes[active_box].move_ip(event.rel)

        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()