import pygame as pg
import pygame.time

pg.init()

screen = pg.display.set_mode((1280,720),pg.RESIZABLE)
clock = pygame.time.Clock()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

pg.quit()

#TODO: the game