import pygame as pg
# the rendere will render stuff on the screen based on a que with a priority system

class Renderer:
    def __init__(self,screen):
        self.screen = screen
        self.queue = list()

    def addToQue(self,renderItem,renderType,priority): #renderItem = (ItemType, Item)
        #TODO: Check if renderItem is renderable
        self.queue.append((priority,renderItem,renderType))

    #TODO: Remove this when not needed anymore
    def sortQue(self):
        self.queue.sort()
    def renderQue(self):
        self.queue.sort()
        for item in self.queue:
            match item(2):
                case 1:
                    self.renderText(item(1))
                case 2:
                    self.renderRect(item(1))
                case 3:
                    self.renderImage(item(1))
                case 4:
                    self.renderPolygon(item(1))
                case 5:
                    self.renderLine(item(1))
                case 6:
                    self.renderCircle(item(1))
                case 7:
                    self.renderElypse(item(1))

    def renderText(self,Item):
        #TODO: implement text rendering
        return
    def renderRect(self,Item):
        #TODO: implement Rect rendering
        return
    def renderImage(self,Item):
        #TODO: implement image rendering
        return
    def renderPolygon(self,Item):
        #TODO: implement Polygon rendering
        return
    def renderLine(self,Item):
        #TODO: implement Line rendering
        return
    def renderCircle(self,Item):
        #TODO: implement Circle rendering
        return
    def renderElypse(self,Item):
        #TODO: implement Elypse rendering
        return
