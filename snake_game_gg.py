import pygame , random, sys
pygame.mixer.init()
modded = ['Easy','Medium','Hard']
CELL_SIZE = 20
LEN_CELLS = 50
WID_CELLS = 25
doing=10
screen = 0
tame=0
x,y = 1,0
lame=0
score=0
hoe=True
mod=0
sound1=0
singisbling=0
agin1=(255,255,255)
agin2=(255,255,255)
agin3=(255,255,255)
sounding=['ON','OFF']
play_button = pygame.Surface((80,40))
settings = pygame.Surface((120,40))
scoring = pygame.Surface((120,40))
difficulty_surface=pygame.Surface((200,40))
sound=pygame.Surface((200,40))
back=pygame.Surface((200,40))
tame=pygame.time.Clock()
print("\nHINT:- ABSOLUTE PATH LIKE C:\\Users\\Lenovo\\OneDrive\\Desktop\\Game\n")
froster=input("Enter Absolute Path of Resources Folder: ")
def blake():
    pygame.mixer.music.load(f'{froster}/bonus.mp3')
    pygame.mixer.music.play()
    return
class fruit:
    def __init__(self):
        fruit.randomizing(self)
    def draw(self):
        global froster
        while (self.loc>LEN_CELLS*CELL_SIZE-140 and self.loc2<CELL_SIZE):
            fruit.randomizing(self)
        apple = pygame.image.load(f'{froster}/apple.png')
        goa = pygame.Rect(self.loc*CELL_SIZE,self.loc2*CELL_SIZE,CELL_SIZE,CELL_SIZE)
        screen.blit(apple,goa)
    def randomizing(self):
        self.loc = random.randint(2,LEN_CELLS-2)
        self.loc2 = random.randint(2,WID_CELLS-2)
        self.final = [self.loc,self.loc2]

class Snake:
    def __init__(self):
        self.length = 3
        self.blocks = [[5,5],[4,5],[3,5]]
    def draw_snake(self):
        for i in range(self.length):
            if i==0:
                if x==1:
                    head=goal9
                elif x==-1:
                    head=goal8
                elif y==1:
                    head=goal7
                elif y==-1:
                    head=goal10
                screen.blit(head,[self.blocks[i][0]*CELL_SIZE,self.blocks[i][1]*CELL_SIZE])
            elif i==self.length-1:
                if self.blocks[i][0]==self.blocks[i-1][0]:
                    if self.blocks[i][1]>self.blocks[i-1][1]:
                        tail=goal11
                    else:
                        tail=goal14
                elif self.blocks[i][1]==self.blocks[i-1][1]:
                    if self.blocks[i][0]<self.blocks[i-1][0]:
                        tail=goal12
                    else:
                        tail=goal13
                screen.blit(tail,[self.blocks[i][0]*CELL_SIZE,self.blocks[i][1]*CELL_SIZE])
            elif self.blocks[i][0]==self.blocks[i+1][0] and self.blocks[i][0]==self.blocks[i-1][0]:
                mid=goal6
                screen.blit(mid,[self.blocks[i][0]*CELL_SIZE,self.blocks[i][1]*CELL_SIZE])
            elif self.blocks[i][1]==self.blocks[i+1][1] and self.blocks[i][1]==self.blocks[i-1][1]:
                mid=goal3
                screen.blit(mid,[self.blocks[i][0]*CELL_SIZE,self.blocks[i][1]*CELL_SIZE])
            else:
                if (self.blocks[i][1]<self.blocks[i-1][1] and self.blocks[i][1]==self.blocks[i+1][1] and self.blocks[i][0]>self.blocks[i+1][0]) or (self.blocks[i][0]==self.blocks[i+1][0] and self.blocks[i][0]>self.blocks[i-1][0] and self.blocks[i][1]<self.blocks[i+1][1]):
                    gogo=goal1
                elif (self.blocks[i][1]>self.blocks[i-1][1] and self.blocks[i][1]==self.blocks[i+1][1] and self.blocks[i][0]>self.blocks[i+1][0]) or (self.blocks[i][0]==self.blocks[i+1][0] and self.blocks[i][0]>self.blocks[i-1][0] and self.blocks[i][1]>self.blocks[i+1][1]):
                    gogo=goal4
                elif (self.blocks[i][1]<self.blocks[i-1][1] and self.blocks[i][1]==self.blocks[i+1][1] and self.blocks[i][0]<self.blocks[i+1][0]) or (self.blocks[i][0]==self.blocks[i+1][0] and self.blocks[i][0]<self.blocks[i-1][0] and self.blocks[i][1]<self.blocks[i+1][1]):
                    gogo=goal2
                elif (self.blocks[i][1]>self.blocks[i-1][1] and self.blocks[i][1]==self.blocks[i+1][1] and self.blocks[i][0]>self.blocks[i+1][0]) or (self.blocks[i][0]==self.blocks[i+1][0] and self.blocks[i][0]<self.blocks[i-1][0] and self.blocks[i][1]>self.blocks[i+1][1]):
                    gogo=goal5
                else:
                    gogo=goal5
                screen.blit(gogo,[self.blocks[i][0]*CELL_SIZE,self.blocks[i][1]*CELL_SIZE])

    def move(self):
        self.blocks.insert(0,[snake.blocks[0][0]+x,snake.blocks[0][1]+y])
        if len(self.blocks)>self.length:
            self.blocks.pop()
    def check(self,bobby=0):
        global sound1,froster,lame
        for i in self.blocks:
            if self.blocks.count(i)>1 or i[0]==0 or i[1]==0 or i[0]==LEN_CELLS-1 or i[1]==WID_CELLS-1 or bobby==1:
                if bobby!=1 and sound1==0:
                    pygame.mixer.music.load(f'{froster}/lose.wav')
                    pygame.mixer.music.play()
                initialize()
                if bobby!=1:
                    display_score(sing=1)
                reset()
                if bobby!=1:
                    menu(one=1)
                    lame = 0
                else:
                    menu(one=0)
gg = fruit()
snake = Snake()
def open_settings():
    global mod,sound1,agin1,agin2,agin3,froster
    while True:
        for event in pygame.event.get():
            mouse=pygame.mouse.get_pos()
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                mouse=pygame.mouse.get_pos()
                if mouse[0]>=420 and mouse[0]<=620:
                    if mouse[1]>=160 and mouse[1]<=200:
                        mod+=1
                        mod%=3
                    elif mouse[1]>=240 and mouse[1]<=280:
                        sound1+=1
                        sound1%=2
                    elif mouse[1]>=320 and mouse[1]<=360:
                        snake.check(bobby=1)
            if mouse[0]>=420 and mouse[0]<=620:
                if mouse[1]>=160 and mouse[1]<=200:
                    difficulty_surface.fill((239,0,65))
                    agin1=(239,0,65)
                elif mouse[1]>=240 and mouse[1]<=280:
                    sound.fill((239,0,65))
                    agin2=(239,0,65)
                elif mouse[1]>=320 and mouse[1]<=360:
                    back.fill((239,0,65))
                    agin3=(239,0,65)
                else:
                    difficulty_surface.fill((255,255,255))
                    sound.fill((255,255,255))
                    back.fill((255,255,255))
                    agin1=(255,255,255)
                    agin2=(255,255,255)
                    agin3=(255,255,255)
        font = pygame.font.Font(None,28)
        text=font.render(f'Difficulty: {modded[mod]}',True,(0,0,0),agin1)
        text_rect=text.get_rect(center=(difficulty_surface.get_width()/2,difficulty_surface.get_height()/2))
        difficulty_surface.blit(text,text_rect)
        screen.blit(difficulty_surface,(21*20,8*20))
        font3 = pygame.font.Font(None,28)
        text3=font.render(f'Sound: {sounding[sound1]}',True,(0,0,0),agin2)
        text_rect3=text3.get_rect(center=(sound.get_width()/2,sound.get_height()/2))
        sound.blit(text3,text_rect3)
        screen.blit(sound,(21*20,12*20))
        font=pygame.font.Font(None,28)
        text=font.render('<-- Back',True,(0,0,0),agin3)
        text_rect=text.get_rect(center=(back.get_width()/2,back.get_height()/2))
        back.blit(text,text_rect)
        screen.blit(back,(21*20,16*20))
        pygame.display.update()
def initialize():
    global LEN_CELLS,CELL_SIZE,WID_CELLSA,screen,tame
    pygame.init()
    screen = pygame.display.set_mode((LEN_CELLS * CELL_SIZE , WID_CELLS * CELL_SIZE))
    pygame.display.set_caption("Snake Game")
    tame = pygame.time.Clock()
initialize()
goal1 = pygame.image.load(f"{froster}/body_bottomleft.png")
goal2 = pygame.image.load(f"{froster}/body_bottomright.png")
goal3 = pygame.image.load(f"{froster}/body_horizontal.png")
goal4 = pygame.image.load(f"{froster}/body_topleft.png")
goal5 = pygame.image.load(f"{froster}/body_topright.png")
goal6 = pygame.image.load(f"{froster}/body_vertical.png")
goal7 = pygame.image.load(f"{froster}/head_down.png")
goal8 = pygame.image.load(f"{froster}/head_left.png")
goal9 = pygame.image.load(f"{froster}/head_right.png")
goal10 = pygame.image.load(f"{froster}/head_up.png")
goal11 = pygame.image.load(f"{froster}/tail_down.png")
goal12 = pygame.image.load(f"{froster}/tail_left.png")
goal13 = pygame.image.load(f"{froster}/tail_right.png")
goal14 = pygame.image.load(f"{froster}/tail_up.png")


def mummy():
    screen.fill((175,215,70))
    for singer in range(LEN_CELLS):
        for singer2 in range(WID_CELLS):
            if singer%2 ==0:
                if singer2%2==0:
                    pygame.draw.rect(screen,(167,209,61),(singer*CELL_SIZE,singer2*CELL_SIZE,CELL_SIZE,CELL_SIZE))
            else:
                if singer2%2!=0:
                    pygame.draw.rect(screen,(167,209,61),(singer*CELL_SIZE,singer2*CELL_SIZE,CELL_SIZE,CELL_SIZE))
            if singer==0 or singer2==0 or singer==LEN_CELLS-1 or singer2==WID_CELLS-1:
                pygame.draw.rect(screen,(0,0,0),(singer*CELL_SIZE,singer2*CELL_SIZE,CELL_SIZE,CELL_SIZE))
def display_score(x=(LEN_CELLS*CELL_SIZE-140),y=(1*CELL_SIZE),sing=1,blink=False):
    global lame,hoe
    font = pygame.font.Font(None,28)
    if blink==True:
        if lame>5:
            hoe=False
        if (sing%10)%2==0:
            flex=(239,0,65)
        else:
            flex=(255,255,255)
    else:
        flex=(255,255,255)
    text = font.render(f'SCORE : {score}',True,(0,0,0),(255,255,255))
    a = text.get_rect(center=(scoring.get_width()/2,scoring.get_height()/2))
    scoring.fill((255,255,255))
    pygame.draw.rect(scoring,flex,(0,0,5,40))
    pygame.draw.rect(scoring,flex,(0,0,120,5))
    pygame.draw.rect(scoring,flex,(120-5,0,5,40))
    pygame.draw.rect(scoring,flex,(0,40-5,120,5))
    if blink==False:
        scoring.fill((255,255,255))
    scoring.blit(text,a)
    screen.blit(scoring,(x,y))
def reset():
    global gg,snake,x,y
    gg=fruit()
    snake=Snake()
    x,y = 1,0
def main():
    global x,y,score,sound1,singisbling,froster
    score = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LEFT or event.key ==pygame.K_a) and x!=1:
                    x,y = -1,0
                elif (event.key == pygame.K_RIGHT or event.key==pygame.K_d) and x!=-1:
                    x,y = 1,0
                elif (event.key == pygame.K_UP or event.key==pygame.K_w) and y!=1:
                    x,y = 0,-1
                elif (event.key == pygame.K_DOWN or event.key==pygame.K_s) and y!=-1:
                    x,y = 0,1
                else:
                    pass
                if event.key==pygame.K_ESCAPE:
                    initialize()
                    display_score(singisbling)
                    reset()
                    menu(one=1)
        singisbling+=1
        singisbling%=100
        mummy()
        gg.draw()
        snake.move()
        snake.draw_snake()
        snake.check()
        if snake.blocks[0]==gg.final:
            snake.length +=1
            score+=10
            gg.randomizing()
            if sound1!=1:
                blake()
        display_score(sing=singisbling)
        pygame.display.update()
        if mod==0:
            doing=10
        elif mod==1:
            doing=13
        else:
            doing=16
        tame.tick(doing)
def menu(one=0):
    global mod,agin1,agin2,singisbling,doing,froster,lame
    while True:
        for event in pygame.event.get():
            mouse=pygame.mouse.get_pos()
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                mouse=pygame.mouse.get_pos()
                if mouse[0] <= 560 and mouse[0]>=480:
                    if mouse[1] <=280 and mouse[1]>=240:
                        main()
                if mouse[0] <=580 and mouse[0]>=460:
                    if mouse[1]<=360 and mouse[1]>=320:
                        initialize()
                        mummy()
                        agin1=(255,255,255)
                        agin2=(255,255,255)
                        open_settings()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    main()
            if mouse[0]>=480 and mouse[0]<=560:
                if mouse[1]>=240 and mouse[1]<=280:
                    play_button.fill((239,0,65))
                    agin1=(239,0,65)
                else:
                    play_button.fill((255,255,255))
                    settings.fill((255,255,255))
                    agin1=(255,255,255)
                    agin2=(255,255,255)
            else:
                play_button.fill((255,255,255))
                settings.fill((255,255,255))
                agin1=(255,255,255)
                agin2=(255,255,255)
            if mouse[0]>=460 and mouse[0]<=580:
                if mouse[1]>=320 and mouse[1]<=360:
                    settings.fill((239,0,65))
                    agin2=(239,0,65)
            else:
                play_button.fill((255,255,255))
                settings.fill((255,255,255))
                agin1=(255,255,255)
                agin2=(255,255,255)
        mummy()
        singisbling+=1
        singisbling%=100
        logo=pygame.image.load(f'{froster}/logo-removebg-preview.png')
        screen.blit(logo,(18*20,2*20))
        font=pygame.font.Font(None,32)
        text=font.render('Play',True,(0,0,0),agin1)
        text_rect=text.get_rect(center=(play_button.get_width()/2,play_button.get_height()/2))
        play_button.blit(text,text_rect)
        font2=pygame.font.Font(None,32)
        text2=font2.render('Settings',True,(0,0,0),agin2)
        text_rect2=text2.get_rect(center=(settings.get_width()/2,settings.get_height()/2))
        settings.blit(text2,text_rect2)
        screen.blit(play_button,(24*20,12*20))
        screen.blit(settings,(23*20,16*20))
        if one==1 and hoe==True:
            display_score(690,180,singisbling,blink=True)
            lame +=1
        if one==1 and hoe==False:
            display_score(690,180,singisbling)
        pygame.display.update()
        tame.tick(doing)
menu()
pygame.quit()
