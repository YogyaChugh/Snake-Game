import random
import sys

import pygame as pg

pg.mixer.init() # The audio one
modded = ["Easy", "Medium", "Hard"]
CELL_SIZE = 20
LEN_CELLS = 50
WID_CELLS = 25
doing = 10
screen = 0
tame = 0
x, y = 1, 0
lame = 0
score = 0
hoe = True
mod = 0
sound1 = 0
singisbling = 0
agin1 = (255, 255, 255)
agin2 = (255, 255, 255)
agin3 = (255, 255, 255)
sounding = ["ON", "OFF"]
play_button = pg.Surface((80, 40))
settings = pg.Surface((120, 40))
scoring = pg.Surface((120, 40))
difficulty_surface = pg.Surface((200, 40))
sound = pg.Surface((200, 40))
back = pg.Surface((200, 40))
tame = pg.time.Clock()


def blake():
    pg.mixer.music.load("audio/bonus.wav")
    pg.mixer.music.play()
    return


class fruit:
    def __init__(self):
        fruit.randomizing(self)

    def draw(self):
        c = CELL_SIZE
        while self.loc > LEN_CELLS * c - 140 and self.loc2 < c:
            fruit.randomizing(self)
        apple = pg.image.load("assets/fruit.png")
        apple = pg.transform.scale(apple, (22, 22))
        goa = pg.Rect(self.loc * c, self.loc2 * c, c, c)
        screen.blit(apple, goa)

    def randomizing(self):
        self.loc = random.randint(2, LEN_CELLS - 2)
        self.loc2 = random.randint(2, WID_CELLS - 2)
        self.final = [self.loc, self.loc2]


class Snake:
    def __init__(self):
        self.length = 3
        self.blocks = [[5, 5], [4, 5], [3, 5]]

    def draw_snake(self):
        cs = CELL_SIZE
        for i in range(self.length):
            if i == 0:
                if x == 1:
                    head = goal9
                elif x == -1:
                    head = goal8
                elif y == 1:
                    head = goal7
                elif y == -1:
                    head = goal10
                cur = self.blocks[i]
                screen.blit(head, [cur[0] * cs, cur[1] * cs])
            elif i == self.length - 1:
                if self.blocks[i][0] == self.blocks[i - 1][0]:
                    if self.blocks[i][1] > self.blocks[i - 1][1]:
                        tail = goal11
                    else:
                        tail = goal14
                elif self.blocks[i][1] == self.blocks[i - 1][1]:
                    if self.blocks[i][0] < self.blocks[i - 1][0]:
                        tail = goal12
                    else:
                        tail = goal13
                cur = self.blocks[i]
                screen.blit(tail, [cur[0] * cs, cur[1] * cs])
            elif (
                self.blocks[i][0] == self.blocks[i + 1][0]
                and self.blocks[i][0] == self.blocks[i - 1][0]
            ):
                mid = goal6
                cur = self.blocks[i]
                screen.blit(mid, [cur[0] * cs, cur[1] * cs])
            elif (
                self.blocks[i][1] == self.blocks[i + 1][1]
                and self.blocks[i][1] == self.blocks[i - 1][1]
            ):
                mid = goal3
                cur = self.blocks[i]
                screen.blit(mid, [cur[0] * cs, cur[1] * cs])
            else:
                if (
                    self.blocks[i][1] < self.blocks[i - 1][1]
                    and self.blocks[i][1] == self.blocks[i + 1][1]
                    and self.blocks[i][0] > self.blocks[i + 1][0]
                ) or (
                    self.blocks[i][0] == self.blocks[i + 1][0]
                    and self.blocks[i][0] > self.blocks[i - 1][0]
                    and self.blocks[i][1] < self.blocks[i + 1][1]
                ):
                    gogo = goal1
                elif (
                    self.blocks[i][1] > self.blocks[i - 1][1]
                    and self.blocks[i][1] == self.blocks[i + 1][1]
                    and self.blocks[i][0] > self.blocks[i + 1][0]
                ) or (
                    self.blocks[i][0] == self.blocks[i + 1][0]
                    and self.blocks[i][0] > self.blocks[i - 1][0]
                    and self.blocks[i][1] > self.blocks[i + 1][1]
                ):
                    gogo = goal4
                elif (
                    self.blocks[i][1] < self.blocks[i - 1][1]
                    and self.blocks[i][1] == self.blocks[i + 1][1]
                    and self.blocks[i][0] < self.blocks[i + 1][0]
                ) or (
                    self.blocks[i][0] == self.blocks[i + 1][0]
                    and self.blocks[i][0] < self.blocks[i - 1][0]
                    and self.blocks[i][1] < self.blocks[i + 1][1]
                ):
                    gogo = goal2
                elif (
                    self.blocks[i][1] > self.blocks[i - 1][1]
                    and self.blocks[i][1] == self.blocks[i + 1][1]
                    and self.blocks[i][0] > self.blocks[i + 1][0]
                ) or (
                    self.blocks[i][0] == self.blocks[i + 1][0]
                    and self.blocks[i][0] < self.blocks[i - 1][0]
                    and self.blocks[i][1] > self.blocks[i + 1][1]
                ):
                    gogo = goal5
                else:
                    gogo = goal5
                cur = self.blocks[i]
                screen.blit(gogo, [cur[0] * cs, cur[1] * cs])

    def move(self):
        self.blocks.insert(0, [snake.blocks[0][0] + x, snake.blocks[0][1] + y])
        if len(self.blocks) > self.length:
            self.blocks.pop()

    def check(self, bobby=0):
        global lame
        for i in self.blocks:
            if (
                self.blocks.count(i) > 1
                or i[0] == 0
                or i[1] == 0
                or i[0] == LEN_CELLS - 1
                or i[1] == WID_CELLS - 1
                or bobby == 1
            ):
                if bobby != 1 and sound1 == 0:
                    pg.mixer.music.load("audio/lose.wav")
                    pg.mixer.music.play()
                initialize()
                if bobby != 1:
                    display_score(sing=1)
                reset()
                if bobby != 1:
                    menu(one=1)
                    lame = 0
                else:
                    menu(one=0)


gg = fruit()
snake = Snake()


def open_settings():
    global mod, sound1, agin1, agin2, agin3
    while True:
        for event in pg.event.get():
            mouse = pg.mouse.get_pos()
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse = pg.mouse.get_pos()
                if mouse[0] >= 420 and mouse[0] <= 620:
                    if mouse[1] >= 160 and mouse[1] <= 200:
                        mod += 1
                        mod %= 3
                    elif mouse[1] >= 240 and mouse[1] <= 280:
                        sound1 += 1
                        sound1 %= 2
                    elif mouse[1] >= 320 and mouse[1] <= 360:
                        snake.check(bobby=1)
            if mouse[0] >= 420 and mouse[0] <= 620:
                if mouse[1] >= 160 and mouse[1] <= 200:
                    difficulty_surface.fill((239, 0, 65))
                    agin1 = (239, 0, 65)
                elif mouse[1] >= 240 and mouse[1] <= 280:
                    sound.fill((239, 0, 65))
                    agin2 = (239, 0, 65)
                elif mouse[1] >= 320 and mouse[1] <= 360:
                    back.fill((239, 0, 65))
                    agin3 = (239, 0, 65)
                else:
                    difficulty_surface.fill((255, 255, 255))
                    sound.fill((255, 255, 255))
                    back.fill((255, 255, 255))
                    agin1 = (255, 255, 255)
                    agin2 = (255, 255, 255)
                    agin3 = (255, 255, 255)
        font = pg.font.Font(None, 28)
        text = font.render(f"Difficulty: {modded[mod]}", 1, (0, 0, 0), agin1)
        text_rect = text.get_rect(
            center=(
                difficulty_surface.get_width() / 2,
                difficulty_surface.get_height() / 2,
            )
        )
        difficulty_surface.blit(text, text_rect)
        screen.blit(difficulty_surface, (21 * 20, 8 * 20))
        text3 = font.render(f"Sound: {sounding[sound1]}", 1, (0, 0, 0), agin2)
        text_rect3 = text3.get_rect(
            center=(sound.get_width() / 2, sound.get_height() / 2)
        )
        sound.blit(text3, text_rect3)
        screen.blit(sound, (21 * 20, 12 * 20))
        font = pg.font.Font(None, 28)
        text = font.render("<-- Back", True, (0, 0, 0), agin3)
        w = back.get_width()
        h = back.get_height()
        text_rect = text.get_rect(center=(w / 2, h / 2))
        back.blit(text, text_rect)
        screen.blit(back, (21 * 20, 16 * 20))
        pg.display.update()


def initialize():
    global screen, tame
    pg.init()
    c = CELL_SIZE
    screen = pg.display.set_mode((LEN_CELLS * c, WID_CELLS * c))
    pg.display.set_caption("Snake Game")
    tame = pg.time.Clock()


initialize()
goal1 = pg.image.load("assets/body_bottomleft.png")
goal1 = pg.transform.scale(goal1, (22, 22))
goal2 = pg.image.load("assets/body_bottomright.png")
goal2 = pg.transform.scale(goal2, (22, 22))
goal3 = pg.image.load("assets/body_horizontal.png")
goal3 = pg.transform.scale(goal3, (22, 22))
goal4 = pg.image.load("assets/body_topleft.png")
goal4 = pg.transform.scale(goal4, (22, 22))
goal5 = pg.image.load("assets/body_topright.png")
goal5 = pg.transform.scale(goal5, (22, 22))
goal6 = pg.image.load("assets/body_vertical.png")
goal6 = pg.transform.scale(goal6, (22, 22))
goal7 = pg.image.load("assets/head_down.png")
goal7 = pg.transform.scale(goal7, (22, 22))
goal8 = pg.image.load("assets/head_left.png")
goal8 = pg.transform.scale(goal8, (22, 22))
goal9 = pg.image.load("assets/head_right.png")
goal9 = pg.transform.scale(goal9, (22, 22))
goal10 = pg.image.load("assets/head_up.png")
goal10 = pg.transform.scale(goal10, (22, 22))
goal11 = pg.image.load("assets/tail_down.png")
goal11 = pg.transform.scale(goal11, (22, 22))
goal12 = pg.image.load("assets/tail_left.png")
goal12 = pg.transform.scale(goal12, (22, 22))
goal13 = pg.image.load("assets/tail_right.png")
goal13 = pg.transform.scale(goal13, (22, 22))
goal14 = pg.image.load("assets/tail_up.png")
goal14 = pg.transform.scale(goal14, (22, 22))


def mummy():
    c = CELL_SIZE
    screen.fill((175, 215, 70))
    for singer in range(LEN_CELLS):
        for singer2 in range(WID_CELLS):
            if singer % 2 == 0:
                if singer2 % 2 == 0:
                    pg.draw.rect(
                        screen,
                        (167, 209, 61),
                        (singer * CELL_SIZE, singer2 * c, c, c),
                    )
            else:
                if singer2 % 2 != 0:
                    pg.draw.rect(
                        screen,
                        (167, 209, 61),
                        (singer * c, singer2 * c, c, c),
                    )
            if (
                singer == 0
                or singer2 == 0
                or singer == LEN_CELLS - 1
                or singer2 == WID_CELLS - 1
            ):
                s = singer
                pg.draw.rect(screen, (0, 0, 0), (s * c, singer2 * c, c, c))


def display_score(
    x=(LEN_CELLS * CELL_SIZE - 140), y=(1 * CELL_SIZE), sing=1, blink=False
):
    global hoe
    font = pg.font.Font(None, 28)
    if blink is True:
        if lame > 5:
            hoe = False
        if (sing % 10) % 2 == 0:
            flex = (239, 0, 65)
        else:
            flex = (255, 255, 255)
    else:
        flex = (255, 255, 255)
    text = font.render(f"SCORE : {score}", True, (0, 0, 0), (255, 255, 255))
    w = scoring.get_width()
    h = scoring.get_height()
    a = text.get_rect(center=(w / 2, h / 2))
    scoring.fill((255, 255, 255))
    pg.draw.rect(scoring, flex, (0, 0, 5, 40))
    pg.draw.rect(scoring, flex, (0, 0, 120, 5))
    pg.draw.rect(scoring, flex, (120 - 5, 0, 5, 40))
    pg.draw.rect(scoring, flex, (0, 40 - 5, 120, 5))
    if blink is False:
        scoring.fill((255, 255, 255))
    scoring.blit(text, a)
    screen.blit(scoring, (x, y))


def reset():
    global gg, snake, x, y
    gg = fruit()
    snake = Snake()
    x, y = 1, 0


def main():
    global x, y, score, singisbling
    score = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                key = event.key
                if (key == pg.K_LEFT or key == pg.K_a) and x != 1:
                    x, y = -1, 0
                elif (key == pg.K_RIGHT or key == pg.K_d) and x != -1:
                    x, y = 1, 0
                elif (key == pg.K_UP or key == pg.K_w) and y != 1:
                    x, y = 0, -1
                elif (key == pg.K_DOWN or key == pg.K_s) and y != -1:
                    x, y = 0, 1
                else:
                    pass
                if key == pg.K_ESCAPE:
                    initialize()
                    display_score(singisbling)
                    reset()
                    menu(one=1)
        singisbling += 1
        singisbling %= 100
        mummy()
        gg.draw()
        snake.move()
        snake.draw_snake()
        snake.check()
        if snake.blocks[0] == gg.final:
            snake.length += 1
            score += 10
            gg.randomizing()
            if sound1 != 1:
                blake()
        display_score(sing=singisbling)
        pg.display.update()
        if mod == 0:
            doing = 10
        elif mod == 1:
            doing = 13
        else:
            doing = 16
        tame.tick(doing)


def menu(one=0):
    global agin1, agin2, singisbling, lame
    while True:
        for event in pg.event.get():
            mouse = pg.mouse.get_pos()
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse = pg.mouse.get_pos()
                if mouse[0] <= 560 and mouse[0] >= 480:
                    if mouse[1] <= 280 and mouse[1] >= 240:
                        main()
                if mouse[0] <= 580 and mouse[0] >= 460:
                    if mouse[1] <= 360 and mouse[1] >= 320:
                        initialize()
                        mummy()
                        agin1 = (255, 255, 255)
                        agin2 = (255, 255, 255)
                        open_settings()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    main()
            if mouse[0] >= 480 and mouse[0] <= 560:
                if mouse[1] >= 240 and mouse[1] <= 280:
                    play_button.fill((239, 0, 65))
                    agin1 = (239, 0, 65)
                else:
                    play_button.fill((255, 255, 255))
                    settings.fill((255, 255, 255))
                    agin1 = (255, 255, 255)
                    agin2 = (255, 255, 255)
            else:
                play_button.fill((255, 255, 255))
                settings.fill((255, 255, 255))
                agin1 = (255, 255, 255)
                agin2 = (255, 255, 255)
            if mouse[0] >= 460 and mouse[0] <= 580:
                if mouse[1] >= 320 and mouse[1] <= 360:
                    settings.fill((239, 0, 65))
                    agin2 = (239, 0, 65)
            else:
                play_button.fill((255, 255, 255))
                settings.fill((255, 255, 255))
                agin1 = (255, 255, 255)
                agin2 = (255, 255, 255)
        mummy()
        singisbling += 1
        singisbling %= 100
        logo = pg.image.load("assets/logo-removebg-preview.png")
        screen.blit(logo, (18 * 20, 2 * 20))
        font = pg.font.Font(None, 32)
        text = font.render("Play", True, (0, 0, 0), agin1)
        text_rect = text.get_rect(
            center=(play_button.get_width() / 2, play_button.get_height() / 2)
        )
        play_button.blit(text, text_rect)
        font2 = pg.font.Font(None, 32)
        text2 = font2.render("Settings", True, (0, 0, 0), agin2)
        text_rect2 = text2.get_rect(
            center=(settings.get_width() / 2, settings.get_height() / 2)
        )
        settings.blit(text2, text_rect2)
        screen.blit(play_button, (24 * 20, 12 * 20))
        screen.blit(settings, (23 * 20, 16 * 20))
        if one == 1 and hoe is True:
            display_score(690, 180, singisbling, blink=True)
            lame += 1
        if one == 1 and hoe is False:
            display_score(690, 180, singisbling)
        pg.display.update()
        tame.tick(doing)


menu()
pg.quit()
