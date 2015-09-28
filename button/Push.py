from button.BaseButton import BaseButton


class Push(BaseButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    '''
    def button(text, color, x, y, hight, width, FONTSIZE = 20):
        fontObj = pygame.font.Font('freesansbold.ttf', FONTSIZE)
        button = pygame.draw.rect(DISPLAYSURF, color, (x, y, width, hight))
        button.topleft = (x, y)
        textSurfaceObj = fontObj.render(str(text), True, BLACK, color)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = button.center
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        return button'''
