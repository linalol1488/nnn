import pygame as pg
from random import *
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
            game_over == True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                direction = "left"
            if event.key == pg.K_RIGHT:
                direction = "right"
            if event.key == pg.K_UP:
                direction = "up"
            if event.key == pg.K_DOWN:
                direction = "down"

    if direction == "left":
        x -= 40
    if direction == "right":
        x += 40
    if direction == "up":
        y -= 40
    if direction == "down":
        y += 40
    for i in range(len(sn) - 1):
        sn[i] = sn[i+1]
        pg.display.update()
    sn[-1] = [x, y]
    if apx == x and apy == y:
        sn = sn[0]+sn
        sc += 1
        while [apx, apy] in sn:
            apx = randint(1, 19)*40
            apy = randint(1, 11)*40
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
pg.quit()
quit()
