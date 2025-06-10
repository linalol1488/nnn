import pygame as pg
from random import *
from time import *
pg.init()
disp = pg.display.set_mode((800, 480))
pg.display.set_caption("Змейка")
pg.display.update()

gr = (0, 255, 0)
bl = (0, 0, 0)
re = (255, 0, 0)
direction = "right"
x = 200
y = 320
apx = 400
apy = 120
sc = 0
sn = [[x, y]]
WHITE = (255, 255, 255)
clock = pg.time.Clock()
game_over = False
font = pg.font.Font(None, 40)
while not game_over:
    clock.tick(4)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            mes = font.render("игра окончена", True, WHITE)
            disp.blit(mes, [0, 0])
            game_over = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT and direction != "right":
                direction = "left"
            if event.key == pg.K_RIGHT and direction != "left":
                direction = "right"
            if event.key == pg.K_UP and direction != "down":
                direction = "up"
            if event.key == pg.K_DOWN and direction != "up":
                direction = "down"

    if direction == "left":
        x -= 40
    if direction == "right":
        x += 40
    if direction == "up":
        y -= 40
    if direction == "down":
        y += 40
    if direction == "pp":
        y += 0
        x += 0
    for i in range(len(sn) - 1):
        sn[i] = sn[i + 1]
        pg.display.update()
    sn[-1] = [x, y]
    if apx == x and apy == y:
        sn = [sn[0]] + sn
        sc += 1
        while [apx, apy] in sn:
            apx = randint(1, 19)*40
            apy = randint(1, 11)*40
    pg.draw.rect(disp, re, [apx, apy, 40, 40])
    pg.display.update()
    disp.fill(bl)
    for i in range(len(sn)):
        pg.draw.rect(disp, gr, [sn[i][0], sn[i][1], 40, 40])
    pg.draw.rect(disp, re, [apx, apy, 40, 40])
    pg.display.update()
    mes = font.render("счет:" + str(sc), True, WHITE)
    disp.blit(mes, [0, 0])
    pg.draw.rect(disp, re, [apx, apy, 40, 40])
    pg.display.update()
    for i in range(480):
        if sn[-1] ==  [800,i]:
            direction = "pp"
            mes = font.render("игра окончена", True, WHITE)
            disp.blit(mes, [300, 100])
            pg.display.update()
            pg.time.delay(2000)
            game_over = True
        elif sn[-1] == [0,i]:
            direction = "pp"
            mes = font.render("игра окончена", True, WHITE)
            disp.blit(mes, [300, 100])
            pg.display.update()
            pg.time.delay(2000)
            game_over = True
    for i in range(800):
        if sn[-1] == [i, 480]:
            direction = "pp"
            mes2 = font.render("игра окончена", True, WHITE)
            disp.blit(mes2, [300, 100])
            pg.display.update()
            sleep(2.0)
            game_over = True
        elif sn[-1] == [i, 0]:
            direction = "pp"
            mes2 = font.render("игра окончена", True, WHITE)
            disp.blit(mes2, [300, 100])
            pg.display.update()
            sleep(2.0)
            game_over = True
    if sn[-1] in sn[:-1] and len(sn) > 4:
        mes2 = font.render("игра окончена", True, WHITE)
        disp.blit(mes2, [300, 100])
        pg.display.update()
        sleep(2.0)
        game_over = True
pg.quit()
quit()