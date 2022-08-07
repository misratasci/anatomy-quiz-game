import pygame
import os

pygame.init()
white = (255,255,255)
green = (0,153,0)
red = (153,0,0)
grey = (166,166,166)
running = True

screen = pygame.display.set_mode((500,500))
screen.fill(white)

path = "imgs/Carotid canal.jpg"
print(os.path.splitext(os.path.basename(path))[0])
img = pygame.image.load(path)
img = pygame.transform.scale(img, (int(img.get_rect().size[0]/2), int(img.get_rect().size[1]/2)))
screen.blit(img, (screen.get_size()[0]/2-img.get_rect().size[0]/2,0))

pygame.draw.rect(screen, green, (50, 500, 100, 25))


while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()