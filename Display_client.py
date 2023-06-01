import pygame
import datetime
from pygame.locals import *
import Client

myClient = Client.Client()
data_list = []

pygame.init()
screen = pygame.display.set_mode((900,550 ))
pygame.display.set_caption('Client')

#color
Red = (255,0,0)
Black = (0,0,0)
Yellow = (249,211,113)
Brown = (84,72,61)

#font
font  = pygame.font.SysFont('Calibri', 25)
font2 = pygame.font.SysFont('Calibri', 15)

#Text
user_text1 = ''
user_text2 = ''
text1 = font.render('LOG IN',True , Yellow)
text2 = font2.render('REGISTER',True, Brown)
text3 = font2.render('Username',True, Brown)
text4 = font2.render('PassWord',True, Brown)
text5 = font2.render('Invalid username or password',True, Red)
text6 = font2.render('IP',True, Brown)
text_wrong_ip = font2.render('Invalid ip address',True, Red)

#Ruing
COLOR_INACTIVE = Brown
COLOR_ACTIVE = Black

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = font2.render(text, True, self.color)
        self.active = False

    def handle_event(self, event, op = True):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
                self.text=''
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE or self.txt_surface.get_width()+30 > self.rect.w:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

            if op:
                self.txt_surface = font2.render(self.text, True, self.color)
            else:
                self.txt_surface = font2.render('*'*len(self.text), True, self.color)
                
    def update(self, x = 300):
        width = max(x, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+10, self.rect.y+10))
        pygame.draw.rect(screen, self.color, self.rect, 1)

def LogIn():
    clock = pygame.time.Clock()
    isConn = None

    input_box1 = InputBox(300, 250, 300, 35, 'username')
    input_box2 = InputBox(300, 295, 300, 35, 'password')
    input_box3 = InputBox(355, 450, 100, 30)

    input_boxes = [input_box1, input_box2, input_box3]

    Log_In = pygame.Rect(300, 350, 300, 40)
    createAcc = pygame.Rect(300, 400, 300, 30)

    while True:
        screen.fill(Yellow)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                myClient.disconnect()
                return -1

            input_box1.handle_event(event)
            input_box2.handle_event(event, False)
            input_box3.handle_event(event)

            input_box1.update()
            input_box2.update()
            input_box3.update(245)

            screen.fill(Yellow)

            for box in input_boxes:
                box.draw(screen)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if Log_In.collidepoint(event.pos):
                    user_name = input_box1.text
                    password = input_box2.text
                    ipaddr = input_box3.text

                    if not myClient.ON:
                        myClient.connect(ipaddr)
                    else:
                        if ipaddr != myClient.ADDR:
                            myClient.disconnect()
                            myClient.connect(input_box3.text)

                    if (myClient.ON):
                        if myClient.login(user_name, password):
                            return 2
                        else :
                            screen.blit(text5,(355,230))

            if not myClient.ON:
                screen.blit(text_wrong_ip,(487, 459))

            if event.type == pygame.MOUSEBUTTONDOWN:
                if createAcc.collidepoint(event.pos):
                    return 1

            # Log In
            pygame.draw.rect(screen, Brown, (300, 350, 300, 40))
            pygame.draw.line(screen, Brown,(300,350),(600,350),1)
            pygame.draw.line(screen, Brown,(300,350),(300,390),1)
            pygame.draw.line(screen, Brown,(300,390),(600,390),1)
            pygame.draw.line(screen, Brown,(600,350),(600,390),1)
            screen.blit(text1,(415,358))

            #New account
            pygame.draw.line(screen, Brown,(300,400),(600,400),1)
            pygame.draw.line(screen, Brown,(300,430),(600,430),1)
            pygame.draw.line(screen, Brown,(300,400),(300,430),1)
            pygame.draw.line(screen, Brown,(600,400),(600,430),1)
            screen.blit(text2,(421,408))

            #IP
            pygame.draw.line(screen, Brown,(300,450),(350,450),1)
            pygame.draw.line(screen, Brown,(300,480),(350,480),1)
            pygame.draw.line(screen, Brown,(350,450),(350,480),1)
            pygame.draw.line(screen,Brown,(300,450),(300,480),1)
            screen.blit(text6,(320,458))

            #frontpager
            frontpager = pygame.image.load('gold prices_1.png')
            screen.blit(frontpager,(155,50))
            frontpager = pygame.image.load('flower1.png')
            screen.blit(frontpager,(0,365))
            frontpager = pygame.image.load('flower2.png')
            screen.blit(frontpager,(700,365))

            #update screen
            pygame.display.flip()
            clock.tick(30)

def CreateAcc():
    clock = pygame.time.Clock()

    SingUP = pygame.Rect(300, 390, 300, 40)
    Back = pygame.Rect(800, 10, 80, 30)

    text7 = font2.render('Account',True, Brown)
    text8 = font2.render('Password',True, Brown)
    text9 = font2.render('Confirm password',True, Brown)
    text10= font.render('REGISTER',True, Yellow)
    text11= font.render('BACK',True, Yellow)
    text12= font2.render('Wrong password',True, Red)
    text_wrong_acc = font2.render('Account is already in use', True, Red)

    input_box1 = InputBox(300, 195, 300, 35, 'username')
    input_box2 = InputBox(300, 255, 300, 35, 'password')
    input_box3 = InputBox(300, 315, 300, 35, 'password')#confirm pass
    input_box4 = InputBox(355, 450, 100, 30)

    input_boxes = [input_box1, input_box2, input_box3, input_box4]

    while True:
        screen.fill(Yellow)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                myClient.disconnect()
                return -1

            input_box1.handle_event(event)
            input_box2.handle_event(event, False)
            input_box3.handle_event(event, False)
            input_box4.handle_event(event)

            input_box1.update()
            input_box2.update()
            input_box3.update()
            input_box4.update(245)

            screen.fill(Yellow)

            for box in input_boxes:
                box.draw(screen)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if SingUP.collidepoint(event.pos):
                    user_name = input_box1.text
                    password = input_box2.text
                    confirm = input_box3.text
                    ipaddr = input_box4.text

                    if not myClient.ON:
                        myClient.connect(ipaddr)
                    else:
                        if ipaddr != myClient.ADDR:
                            myClient.disconnect()
                            myClient.connect(ipaddr)

                    if password == confirm:
                        if (myClient.ON):
                            if myClient.signup(user_name, password):
                                myClient.disconnect()
                                return 0
                            else:
                                screen.blit(text_wrong_acc, (452, 180))
                    else:
                        screen.blit(text12,(496,300))

            if not myClient.ON:
                screen.blit(text_wrong_ip,(487, 459))

            if event.type == pygame.MOUSEBUTTONDOWN:
                if Back.collidepoint(event.pos):
                    myClient.disconnect()
                    return 0

            screen.blit(text7,(300,180))
            screen.blit(text8,(300,240))
            screen.blit(text9,(300,300))

            frontpager = pygame.image.load('creAcc.png')
            screen.blit(frontpager,(200,70))

            #Register
            pygame.draw.rect(screen, Brown, (300, 390, 300, 40))
            pygame.draw.line(screen, Brown,(300,390),(600,390),1)
            pygame.draw.line(screen, Brown,(300,390),(300,430),1)
            pygame.draw.line(screen, Brown,(300,430),(600,430),1)
            pygame.draw.line(screen, Brown,(600,390),(600,430),1)
            screen.blit(text10,(402,400))

            #Back
            pygame.draw.rect(screen, Brown, (800, 10, 80, 30))
            pygame.draw.line(screen, Brown,(800,10),(880,10),1)
            pygame.draw.line(screen, Brown,(800,10),(800,40),1)
            pygame.draw.line(screen, Brown,(800,40),(880,40),1)
            pygame.draw.line(screen, Brown,(880,10),(880,40),1)
            screen.blit(text11,(815,15))

            #IP
            pygame.draw.line(screen, Brown,(300,450),(350,450),1)
            pygame.draw.line(screen, Brown,(300,480),(350,480),1)
            pygame.draw.line(screen, Brown,(350,450),(350,480),1)
            pygame.draw.line(screen, Brown,(300,450),(300,480),1)
            screen.blit(text6,(320,458))

            #update screen
            pygame.display.flip()

def Exchange(): 
    clock = pygame.time.Clock()

    Logout = pygame.Rect(70, 470, 80, 30)
    seachPrice = pygame.Rect(200, 470, 70, 30)

    search = InputBox(275, 470, 10, 30)

    data_list = myClient.requestData()
    print(data_list)

    texts = []
    buy_texts = []
    sell_texts = []

    if len(data_list) != 0:
        check_color = True
        for i in range(20):
            color = ()
            if check_color == True:
                color = Brown
            else:
                color = Yellow
            texts.append(font2.render(data_list[i]['name'],True, color))
            buy_texts.append(font2.render(str(data_list[i]['buy']),True, color))
            sell_texts.append(font2.render(str(data_list[i]['sell']),True, color))
            check_color = not check_color

    else:
        for i in range(20):
            texts.append(font2.render('Empty',True, Black))
            buy_texts.append(font2.render('Empty',True, Black))
            sell_texts.append(font2.render('Empty',True, Black))

    money_obj = {}

    text11= font2.render('LOG OUT',True, Yellow)
    text13= font2.render('Name',True, Yellow)
    text14= font2.render('Buy',True, Yellow)
    text15= font2.render('Sell',True, Yellow)
    text16= font2.render('Buy',True, Brown)
    text17= font2.render('Sell',True, Brown)
    text36= font2.render('Search',True, Yellow)

    while True:
        screen.fill(Yellow)

        now = datetime.datetime.now()
        now_str = now.strftime("%Y-%m-%d %H:%M:%S")
        time_text = font2.render(now_str, True, Brown)

        search.update(150)
        search.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                myClient.disconnect()
                return -1
            
            search.handle_event(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if Logout.collidepoint(event.pos):
                    myClient.disconnect()
                    return 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                if seachPrice.collidepoint(event.pos):
                    money_obj = {}
                    money = search.text.upper()
                    
                    for i in data_list:
                        if i['name'] == money:
                            money_obj = i

        
        if money_obj != {}:
            buy_text = font2.render(str(money_obj['buy']), True, Brown)
            sell_text = font2.render(str(money_obj['sell']), True, Brown)

            screen.blit(buy_text, (438, 478))
            screen.blit(sell_text, (493, 478))
        else:
            buy_text = font2.render('Empty', True, Brown)
            sell_text = font2.render('Empty', True, Brown)

            screen.blit(buy_text, (436, 478))
            screen.blit(sell_text, (491, 478))

        screen.blit(time_text, (690,485))

        # Capture
        frontpager = pygame.image.load('gold prices_2.png')
        screen.blit(frontpager,(280,10))

        # Log out
        pygame.draw.rect(screen, Brown, (70, 470, 80, 30))
        screen.blit(text11,(80,478))

        # Talbe 1
        pygame.draw.rect(screen, Brown,(70, 110, 350, 30))
        pygame.draw.rect(screen, Brown,(70, 170, 350, 30))
        pygame.draw.rect(screen, Brown,(70, 230, 350, 30))
        pygame.draw.rect(screen, Brown,(70, 290, 350, 30))
        pygame.draw.rect(screen, Brown,(70, 350, 350, 30))
        pygame.draw.rect(screen, Brown,(70, 410, 350, 30))

        screen.blit(text13,(80,117))
        screen.blit(text14,(255,117))
        screen.blit(text15,(355,117))

        # Table 2
        pygame.draw.rect(screen, Brown, (475, 110, 350, 30))
        pygame.draw.rect(screen, Brown,(475, 170, 350, 30))
        pygame.draw.rect(screen, Brown,(475, 230, 350, 30))
        pygame.draw.rect(screen, Brown,(475, 290, 350, 30))
        pygame.draw.rect(screen, Brown,(475, 350, 350, 30))
        pygame.draw.rect(screen, Brown,(475, 410, 350, 30))

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
        
        pygame.draw.rect(screen, Brown, (200, 470, 70, 30))
        screen.blit(text36,(215, 478))
        
        pygame.draw.line(screen, Brown,(430,470),(480,470),1)
        pygame.draw.line(screen, Brown,(430,500),(480,500),1)
        pygame.draw.line(screen, Brown,(430,470),(430,500),1)
        pygame.draw.line(screen, Brown,(480,470),(480,500),1)
        screen.blit(text16,(433,455))

        pygame.draw.line(screen, Brown,(485,470),(535,470),1)
        pygame.draw.line(screen, Brown,(485,500),(535,500),1)
        pygame.draw.line(screen, Brown,(485,470),(485,500),1)
        pygame.draw.line(screen, Brown,(535,470),(535,500),1)
        screen.blit(text17,(488,455))

        pygame.display.flip()

def main():
    op = 0
    
    while op != -1:
        if op == 0:
            op = LogIn()
        elif op == 1:
            op = CreateAcc()
        elif op == 2:
            op = Exchange()

if __name__ == '__main__':
    main()
    pygame.quit()