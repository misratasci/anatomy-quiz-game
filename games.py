import pygame, random
from pygame_funcs import Button, blit_muscle_info, blit_img, load_img, blit_text
from funcs import get_rand_list_member, MQuestion

nextbutton = Button("Next")
showbutton = Button("Show")
rightbutton = Button("Right")
wrongbutton = Button("Wrong")

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

insults = ["salak", "mal", "gerizekalı", "aptal", "medi'yi de geçemediysen...", 
"guys, 5 years...", "sen ikinci grupsun galiba", 
"bunları nutide de görcen, if you manage to go there...", 
"siz bir de circ'ü görün", "I told you guys, medi was easy...", "nuti is coming"]
def insult(screen, font):
    insult = get_rand_list_member(insults)
    screen.blit(font.render(insult, False, dogruduzgunred), (500 - 10*len(insult), 200))

def renew_q_screen(screen, qno, font):
    screen.fill(white)
    rightbutton.draw(screen, green, black, font, 770, 390)
    wrongbutton.draw(screen, red, black, font, 880, 390)
    nextbutton.draw(screen, gray, black, font, 880, 440)
    showbutton.draw(screen, gray, black, font, 770, 440)
    text = font.render(f"Questions left: {qno}", False, black)
    screen.blit(text, (800, 30))

def get_img_question(screen, list):
    muscle = get_rand_list_member(list)
    blit_img(screen, muscle)
    return muscle

"""
class Game():
    def __init__(self, screen, questions, addwrongs, font):
        self.questions = questions
        self.current_question = None
        self.screen = screen
        self.font = font
        self.addwrongs = addwrongs
        self.wrongs = []
        self.buttons = {"Next": Button("Next"), "Show": Button("Show"), "Right": Button("Right"), "Wrong": Button("Wrong")}
        running = True
        self.renew_q_screen()
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.buttons["Next"].collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                        self.renew_q_screen()
                    if self.buttons["Show"].collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                        blit_muscle_info(screen, q, font, black)
                    if self.buttons["Right"].collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                        qlist.remove(q)
                        renew_q_screen(screen, len(qlist), font)
                        q = get_img_question(screen, qlist)
                    if self.buttons["Wrong"].collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                        if addwrongs:
                            qlist.append(q)
                        renew_q_screen(screen, len(qlist), font)
                        q = get_img_question(screen, qlist)
            pygame.display.update()
    
    def draw_buttons(self):
        self.buttons["Right"].draw(self.screen, green, black, self.font, 770, 390)
        self.buttons["Wrong"].draw(self.screen, red, black, self.font, 880, 390)
        self.buttons["Next"].draw(self.screen, gray, black, self.font, 880, 440)
        self.buttons["Show"].draw(self.screen, gray, black, self.font, 770, 440)
    
    def renew_q_screen(self):
        screen.fill(white)
        self.draw_buttons()
        text = self.font.render(f"Questions left: {len(self.questions)}", False, black)
        screen.blit(text, (800, 30))
        self.blit_question()

    def get_question(self):
        self.current_question = get_rand_list_member(self.questions)
    
    def blit_question(self):
        blit_text(self.screen, [self.current_question.text], self.font, black, (100,100))


class Picture_Game(Game):

    def blit_question(self):
        q = self.get_question()
        blit_img(self.screen, q)
"""


def picture_game_loop(screen, activechoices, addwrongs, muscles, font):
    qlist = []
    for a in activechoices:
        for m in muscles:
            if a.text == m.location:
                qlist.append(m)
    running = True
    renew_q_screen(screen, len(qlist), font)
    q = get_img_question(screen, qlist)
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if nextbutton.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    renew_q_screen(screen, len(qlist), font)
                    q = get_img_question(screen, qlist)
                if showbutton.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    blit_muscle_info(screen, q, font, black)
                if rightbutton.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    qlist.remove(q)
                    renew_q_screen(screen, len(qlist), font)
                    q = get_img_question(screen, qlist)
                if wrongbutton.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    if addwrongs:
                        qlist.append(q)
                    renew_q_screen(screen, len(qlist), font)
                    q = get_img_question(screen, qlist)
        pygame.display.update()

def get_name_question(screen, list, font):
    muscle = get_rand_list_member(list)
    screen.blit(font.render(f"{muscle.name}?", False, black), (load_img(muscle.imgpath).get_rect().size[0]+50, 100))
    return muscle

def name_game_loop(screen, activechoices, addwrongs, muscles, font):
    qlist = []
    for a in activechoices:
        for m in muscles:
            if a.text == m.location:
                qlist.append(m)
    running = True
    renew_q_screen(screen, len(qlist), font)
    q = get_name_question(screen, qlist, font)
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if nextbutton.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    renew_q_screen(screen, len(qlist), font)
                    q = get_name_question(screen, qlist, font)
                if showbutton.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    blit_muscle_info(screen, q, font, black)
                if rightbutton.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    qlist.remove(q)
                    renew_q_screen(screen, len(qlist), font)
                    q = get_name_question(screen, qlist, font)
                if wrongbutton.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    if addwrongs:
                        qlist.append(q)
                    renew_q_screen(screen, len(qlist), font)
                    q = get_name_question(screen, qlist, font)
        pygame.display.update()

def get_soru_question(screen, list, font):
    if len(list) == 0:
        return None
    q = get_rand_list_member(list)
    screen.blit(font.render(f"{q.muscle.name} {q.ozellik}?", False, black), (load_img(q.muscle.imgpath).get_rect().size[0]+50,100))
    return q

def sorulu_game_loop(screen, activechoices, addwrongs, muscles, font):
    musclelist = []
    for a in activechoices:
        for m in muscles:
            if a.text == m.location:
                musclelist.append(m)
    qlist = []
    for m in musclelist:
        qlist.append(MQuestion(m, "location"))
        qlist.append(MQuestion(m, "origin"))
        qlist.append(MQuestion(m, "insertion"))
        qlist.append(MQuestion(m, "nerve"))
        qlist.append(MQuestion(m, "function"))
    running = True
    renew_q_screen(screen, len(qlist), font)
    q = get_soru_question(screen, qlist, font)
    wronglist = []
    while running:

        for event in pygame.event.get():
            if len(qlist) == 0:
                ending(screen, wronglist, font)
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if nextbutton.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    renew_q_screen(screen, len(qlist), font)
                    q = get_soru_question(screen, qlist, font)
                if showbutton.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    screen.blit(font.render(f"{q.answer}", False, black), (load_img(q.muscle.imgpath).get_rect().size[0]+50, 150))
                    blit_img(screen, q.muscle)
                if rightbutton.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    pygame.mixer.music.play(0)
                    qlist.remove(q)
                    renew_q_screen(screen, len(qlist), font)
                    q = get_soru_question(screen, qlist, font)
                if wrongbutton.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    insult(screen, font)
                    if addwrongs:
                        qlist.append(q)
                    wronglist.append(q)
        
        pygame.display.update()
"""
def blit_options(screen, question, muscles, pos):
    all_options = []
    for m in muscles:
        q = MQuestion(m, question.ozellik)
        all_options.append(q.answer)
    options = random.sample(all_options, k = 5)
    option_buttons = []
    for op in options:
        option_buttons.append = Button(op)
    y = 0
    for but in option_buttons:
        but.draw(screen, gray, black, font, pos[0], pos[1]+y)
        y += 30
    
def optioned_game_loop(screen, activechoices, addwrongs, muscles, font):
    musclelist = []
    for a in activechoices:
        for m in muscles:
            if a.text == m.location:
                musclelist.append(m)
    qlist = []
    for m in musclelist:
        qlist.append(MQuestion(m, "location"))
        qlist.append(MQuestion(m, "origin"))
        qlist.append(MQuestion(m, "insertion"))
        qlist.append(MQuestion(m, "nerve"))
        qlist.append(MQuestion(m, "function"))
    running = True
    renew_q_screen(screen, len(qlist), font)
    q = get_soru_question(screen, qlist, font)
    wronglist = []
    while running:

        for event in pygame.event.get():
            if len(qlist) == 0:
                ending(screen, wronglist, font)
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if nextbutton.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    renew_q_screen(screen, len(qlist), font)
                    q = get_soru_question(screen, qlist, font)
                if showbutton.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    screen.blit(font.render(f"{q.answer}", False, black), (load_img(q.muscle.imgpath).get_rect().size[0]+50, 150))
                    blit_img(screen, q.muscle)
                if rightbutton.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    pygame.mixer.music.play(0)
                    qlist.remove(q)
                    renew_q_screen(screen, len(qlist), font)
                    q = get_soru_question(screen, qlist, font)
                if wrongbutton.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    insult(screen, font)
                    if addwrongs:
                        qlist.append(q)
                    wronglist.append(q)
        
        pygame.display.update()
"""

def ending(screen, wronglist, font):
    screen.fill(green)
    running = True
    blit_text(screen, ["Wrongs:"], font, black, (100, 100))
    y = 150
    for w in wronglist:
        blit_text(screen, [f"{w.muscle.name} {w.ozellik}: {w.answer}"], font, black, (100, y))
        y += 50

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()