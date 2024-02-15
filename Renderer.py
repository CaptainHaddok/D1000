import pygame as pg
# the rendere will render stuff on the screen based on a que with a priority system

class Renderer:
    def __init__(self,screen):
        self.screen = screen
        self.queue = list()
        self.fontList = dict()

    def addToQue(self,renderItem,renderType,priority): #renderItem = (ItemType, Item)
        #TODO: Check if renderItem is renderable
        self.queue.append((priority,renderItem,renderType)) #(priority, item, type)
    def addText(self,priority,text,fontname):
        self.queue.append((priority,(text,fontname),1))
        pass
    def addRect(self):
        # TODO: implement
        pass
    def addImage(self):
        # TODO: implement
        pass
    def addPolygon(self):
        # TODO: implement
        pass
    def addLine(self):
        # TODO: implement
        pass
    def addCircle(self):
        # TODO: implement
        pass
    def addElypse(self):
        # TODO: implement
        pass

    #TODO: Remove this when not needed anymore
    def sortQue(self):
        self.queue.sort()
    def renderQue(self):
        self.queue.sort()
        for item in self.queue:
            if item(2) == 1:
                self.__renderText(item(1))
            elif item(2) == 2:
                self.__renderRect(item(1))
            elif item(2) == 3:
                self.__renderImage(item(1))
            elif item(2) == 4:
                self.__renderPolygon(item(1))
            elif item(2) == 5:
                self.__renderLine(item(1))
            elif item(2) == 6:
                self.__renderCircle(item(1))
            elif item(2) == 7:
                self.__renderElypse(item(1))
    def __renderText(self,Item):
        #TODO: implement text rendering
        return
    def __renderRect(self,Item):
        #TODO: implement Rect rendering
        return
    def __renderImage(self,Item):
        #TODO: implement image rendering
        return
    def __renderPolygon(self,Item):
        #TODO: implement Polygon rendering
        return
    def __renderLine(self,Item):
        #TODO: implement Line rendering
        return
    def __renderCircle(self,Item):
        #TODO: implement Circle rendering
        return
    def __renderElypse(self,Item):
        #TODO: implement Elypse rendering
        return
    def addFont(self,font,fontname):
        self.fontList[fontname] = font