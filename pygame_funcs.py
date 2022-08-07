import pygame
from funcs import Muscle

def load_img(path):
    img = pygame.image.load(path)
    img_aspect_ratio = img.get_rect().size[0]/img.get_rect().size[1]
    if int(img_aspect_ratio*500) < 500:
        img = pygame.transform.scale(img, (int(img_aspect_ratio*500), 500))
    else:
        img = pygame.transform.scale(img, (500, int(500/img_aspect_ratio)))
    return img

def blit_img(screen, muscle):
    screen.blit(load_img(muscle.imgpath), (25,0))

def blit_text(screen, textlist, font, color, pos):
    i = 0
    for text in textlist:
        txt = font.render(text, False, color)
        screen.blit(txt, (pos[0], pos[1] + i))
        i += 30

def blit_muscle_info(screen, muscle, font, color):
    blit_img(screen, muscle)
    textpos = (load_img(muscle.imgpath).get_rect().size[0] + 50, 100)
    blit_text(screen, muscle.get_info_text(), font, color, textpos)


gray = (150,150,150)
white = (255,255,255)
class Button(pygame.Rect):
    def __init__(self, text):
        self.text = text
        self.width = 14*len(self.text)
        self.height = 30
        self.active = False
        self.color = white
        self.activecolor = gray
    def draw(self, screen, color, textcolor, font, x, y):
        self.x = x
        self.y = y
        self.color = color
        if self.active:
            self.color = self.activecolor
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        text = font.render(self.text, False, textcolor)
        screen.blit(text, (self.x+10, self.y+5))
    def activate(self):
        self.active = True
        