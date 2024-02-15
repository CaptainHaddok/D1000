import pygame as pg
import pygame.time
import Renderer

pg.init()

screen = pg.display.set_mode((1280,720),pg.RESIZABLE)
clock = pygame.time.Clock()

Renderer = Renderer.Renderer(screen)

#testcode to make que working
Renderer.addToQue("Biem",1,2)
Renderer.addToQue("Bam", 10,2)
Renderer.addToQue("Test",3,2)
Renderer.addFont(pg.font.Font("fonts/Inlanders.otf",20),"testfont")


print(Renderer.queue)
Renderer.sortQue()
print(Renderer.queue)






running = False #game running or not
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

pg.quit()

#TODO: the game