import pygame, os
from funcs import Muscle, MQuestion, read_xl_data, get_rand_list_member
from pygame_funcs import blit_img, blit_text, blit_muscle_info, Button
from games import picture_game_loop, sorulu_game_loop, name_game_loop

data = read_xl_data("muscles.xlsx")
muscle_attributes = data.pop(0)
muscle_attributes = muscle_attributes[1:]
muscles = []
for i in range(len(data)):
    muscles.append(Muscle(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5]))
locations = []
for row in data:
    if row[1] not in locations:
        locations.append(row[1])
locations.pop(0)

pygame.init()
white = (255,255,255)
black = (0,0,0)
gray = (150,150,150)
agray = (120,120,120)
red = (200, 150,150)
dogruduzgunred = (255,0,0)
ared = (170, 120, 120)
green = (150,200,150)
agreen = (120, 170, 120)
blue = (150,150,200)

screen = pygame.display.set_mode((1000,500))
pygame.mixer.music.load("selcuk_gulus.mp3")

font = pygame.font.SysFont('Times New Roman', 20, False, False)
insultfont = pygame.font.SysFont("Comic Sans MS", 35, True, False)

choices = []
shownchoices = []
activechoices = []

for loc in locations:
    choice = Button(loc)
    choices.append(choice)

resimlibutton = Button("Image Mode")
isimlibutton = Button("Name Mode")
sorulubutton = Button("Question Mode")
allbutton = Button("Select All")
addwrongsbutton = Button("Yanlışları havuza ekle")
nextchoicesbutton = Button(" > ")
previouschoicesbutton = Button(" < ")
def draw_choices(pageno):
    shownchoices.clear()
    for i in range(pageno*15, (pageno+1)*15):
        if i < len(choices):
            shownchoices.append(choices[i])
    x = 30
    y = 50
    allbutton.draw(screen, white, black, font, 30, 20)
    for c in shownchoices:
        c.draw(screen, white, black, font, x, y)
        y += 30
def choice_screen(pageno):
    screen.fill(white)
    nextchoicesbutton.draw(screen, white, black, font, 630, 400)
    previouschoicesbutton.draw(screen, white, black, font, 600, 400)
    draw_choices(pageno)
    resimlibutton.draw(screen, green, black, font, 800, 440)
    isimlibutton.draw(screen, red, black, font, 800, 390)
    sorulubutton.draw(screen, blue, black, font, 800, 340)
    addwrongsbutton.draw(screen, blue, black, font, 500, 200)



def intro():
    running = True
    pageno = 0
    choice_screen(pageno)
    addwrongs = False
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                activechoices = [c for c in choices if c.active]
                if allbutton.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    allbutton.draw(screen, gray, black, font, allbutton.left, allbutton.top)
                    for c in choices:
                        c.activate()
                        c.draw(screen, c.activecolor, black, font, c.x, c.y)
                for c in shownchoices:
                    if c.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                        c.activate()
                        c.draw(screen, c.activecolor, black, font, c.x, c.y)
                if resimlibutton.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    picture_game_loop(screen, activechoices, addwrongs, muscles, font)
                if isimlibutton.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    name_game_loop(screen, activechoices, addwrongs, muscles, font)
                if sorulubutton.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    sorulu_game_loop(screen, activechoices, addwrongs, muscles, font)
                    for c in activechoices:
                        print(c.text)
                if addwrongsbutton.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    addwrongs = True
                    addwrongsbutton.draw(screen, gray, black, font, addwrongsbutton.left, addwrongsbutton.top)
                if previouschoicesbutton.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    if pageno > 0:
                        pageno -= 1
                        choice_screen(pageno)
                if nextchoicesbutton.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    pageno += 1
                    choice_screen(pageno)

                
        pygame.display.update()



intro()

#to do: diğer satıra geçsin yazılar, geri butonu. resimli ve isimli modda havuza soru ekleme opsiyonu olsun. 
#random insult wronga bastığında "mediyi de geçemediysen...."
#şıklı yap
#bu insertiona sahip olan mm? vs
#bi game class ı yap oyunları da onun subclass i yap.