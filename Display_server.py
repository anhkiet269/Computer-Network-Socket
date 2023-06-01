import pygame
import datetime
from Get import GET
from Account import account
from pygame.locals import *

data_list = GET.load_data()

pygame.init()
screen = pygame.display.set_mode((900,550))
pygame.display.set_caption('Server')

#color
Red = (255,0,0)
Black =(0,0,0)
Yellow = (249,211,113)
Brown = (84,72,61)

#font
font  = pygame.font.SysFont('Calibri', 25)
font2 = pygame.font.SysFont('Calibri', 15)
text1 = font.render('DATA', True , Brown)
text2 = font.render('LOGGED IN ACCOUNT',True , Brown)

def menu ():
    View_Data = pygame.Rect(250, 295, 400, 50)
    View_Logged_In_Accounts= pygame.Rect(250, 370, 400, 50)
    clock = pygame.time.Clock()
    done = False
    while True:
        screen.fill(Brown)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 return -1

            if event.type == pygame.MOUSEBUTTONDOWN:
                if View_Data.collidepoint(event.pos):
                    done = True
                    return 1

            if event.type == pygame.MOUSEBUTTONDOWN:
                if View_Logged_In_Accounts.collidepoint(event.pos):
                    return 2
        frontpager = pygame.image.load('server.png')
        screen.blit(frontpager,(200,50))

        pygame.draw.rect(screen, Yellow, (250, 295, 400, 50))
        pygame.draw.rect(screen, Yellow, (250, 370, 400, 50))

        screen.blit(text1,(420,310))
        screen.blit(text2,(340,385))

        pygame.display.flip()

def ViewData (data_list):
    clock = pygame.time.Clock()

    Back = pygame.Rect(70, 460, 80, 30)

    text11= font2.render('BACK',True, Brown)
    text13= font2.render('Name',True, Brown)
    text14=  font2.render('Buy',True, Brown)
    text15=  font2.render('Sell',True, Brown)

    texts = []
    buy_texts = []
    sell_texts = []

    if len(data_list) != 0:
        check_color = True
        for i in range(20):
            color = ()
            if check_color == True:
                color = Yellow
            else:
                color = Brown
            texts.append(font2.render(data_list[i]['name'],True, color))
            buy_texts.append(font2.render(str(data_list[i]['buy']),True, color))
            sell_texts.append(font2.render(str(data_list[i]['sell']),True, color))
            check_color = not check_color

    else:
        for i in range(20):
            texts.append(font2.render('Empty',True, Black))
            buy_texts.append(font2.render('Empty',True, Black))
            sell_texts.append(font2.render('Empty',True, Black))

    while True:
        screen.fill(Brown)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 return -1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Back.collidepoint(event.pos):
                    return 0

        # Capture
        frontpager = pygame.image.load('gold prices.png')
        screen.blit(frontpager,(280,10))    
            
        # Back
        pygame.draw.rect(screen, Yellow, (70, 460, 80, 30))
        screen.blit(text11,(94,468))

        # Talbe 1
        pygame.draw.rect(screen, Yellow,(70, 110, 350, 30))
        pygame.draw.rect(screen, Yellow,(70, 170, 350, 30))
        pygame.draw.rect(screen, Yellow,(70, 230, 350, 30))
        pygame.draw.rect(screen, Yellow,(70, 290, 350, 30))
        pygame.draw.rect(screen, Yellow,(70, 350, 350, 30))
        pygame.draw.rect(screen, Yellow,(70, 410, 350, 30))

        screen.blit(text13,(80,117))
        screen.blit(text14,(255,117))
        screen.blit(text15,(355,117))

        # Table 2
        pygame.draw.rect(screen, Yellow, (475, 110, 350, 30))
        pygame.draw.rect(screen, Yellow,(475, 170, 350, 30))
        pygame.draw.rect(screen, Yellow,(475, 230, 350, 30))
        pygame.draw.rect(screen, Yellow,(475, 290, 350, 30))
        pygame.draw.rect(screen, Yellow,(475, 350, 350, 30))
        pygame.draw.rect(screen, Yellow,(475, 410, 350, 30))

        screen.blit(text13,(485,117))
        screen.blit(text14,(655,117))
        screen.blit(text15,(755,117))

        y = 148
        for i in range(10):
            screen.blit(texts[i], (80, y))
            screen.blit(buy_texts[i], (248, y))
            screen.blit(sell_texts[i], (347, y))
            y += 30

        y = 148
        for i in range(10, 20):
            screen.blit(texts[i], (485, y))
            screen.blit(buy_texts[i], (651, y))
            screen.blit(sell_texts[i], (750, y))
            y += 30

        now = datetime.datetime.now()
        nowes= now.strftime("%Y-%m-%d %H:%M:%S")
        texx = font2.render(nowes,True, Yellow)
        screen.blit(texx,(690,460))

        pygame.display.flip()

def View_Account():
    Back = pygame.Rect(100, 460, 80, 30)

    acc = account.Account()

    text3= font2.render('BACK',True, Brown)
    text4= font2.render('No',True, Yellow)
    text5= font2.render('Login Account',True, Yellow)
    text6= font2.render('Status',True, Yellow)

    while True:
        screen.fill(Brown)

        user_list = acc.load_login_user()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 return - 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Back.collidepoint(event.pos):
                    return 0


        # Back
        pygame.draw.rect(screen, Yellow, (100, 460, 80, 30))
        screen.blit(text3,(124, 468))

        # Capture
        frontpager = pygame.image.load('logged in account.png')
        screen.blit(frontpager,(60,0))
    
        # Table
        pygame.draw.rect(screen, Yellow, (100, 180, 700, 50))
        pygame.draw.rect(screen, Yellow, (100, 230, 700, 50))
        pygame.draw.rect(screen, Yellow, (100, 280, 700, 50))
        pygame.draw.rect(screen, Yellow, (100, 330, 700, 50))
        pygame.draw.rect(screen, Yellow, (100, 380, 700, 50))

        pygame.draw.line(screen, Brown,(100,180),(800,180),1)
        pygame.draw.line(screen, Brown,(100,230),(800,230),1)
        pygame.draw.line(screen, Brown,(100,280),(800,280),1)
        pygame.draw.line(screen, Brown,(100,330),(800,330),1)
        pygame.draw.line(screen, Brown,(100,380),(800,380),1)

        pygame.draw.line(screen, Brown,(150,150),(150,450),1)
        pygame.draw.line(screen, Brown,(500,150),(500,450),1)

        x = 117
        x1 = 250
        x2 = 632
        y = 195
        for i in range(5):
            if i < len(user_list):
                t = font.render(str(i + 1), True, Brown)
                screen.blit(t, (x, y))

                t1 = font.render(user_list[i], True, Brown)
                screen.blit(t1, (x1, y))
            
                t2 = font.render('ON', True, Brown)
                screen.blit(t2, (x2, y))

            else:
                break

            y += 50

        screen.blit(text4,(115,160))
        screen.blit(text5,(250,160))
        screen.blit(text6,(630,160))

        pygame.display.flip()
def main() :


    op = 0
    while op != -1:
        if op == 0:
            op = menu()
        elif op == 1:
            op = ViewData(data_list)
        elif op == 2:
            op = View_Account()

if __name__ == '__main__':
    main()
    pygame.quit()