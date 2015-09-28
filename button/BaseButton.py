import pygame
from definitions.colors import *


class BaseButton:
    DISPLAYSURF = None

    def __init__(self, **kwargs):
        self.color = GREEN
        self.fontObj = pygame.font.Font('freesansbold.ttf', kwargs["fontsize"])
        self.obj = None
        self.x = kwargs['x']
        self.y = kwargs['y']
        self.width = kwargs['width']
        self.height = kwargs['height']
        BaseButton.DISPLAYSURF = kwargs['surf']

    def update(self):
        self.obj = pygame.draw.rect(BaseButton.DISPLAYSURF, self.color, (self.x, self.y, self.width, self.height))
        self.obj.topleft = (self.x, self.y)
        #textSurfaceObj = self.fontObj.render(str(self.text), True, BLACK, self.color)
        #textRectObj = textSurfaceObj.get_rect()
        #textRectObj.center = self.obj.center
        #BaseButton.DISPLAYSURF.blit(textSurfaceObj, textRectObj)

    def onclick(self):
        pass
