import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    # scr = pg.display.get_surface()
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)

    tmr = 0
    angle = 0
    v = -1

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        angle += v
        if tmr % 10 == 0:
            v *= -1
        tmr += 1
        screen.blit(bg_img, [(-tmr)%3200-3200, 0])
        screen.blit(bg_img2,[-tmr%3200-1600,0])
        screen.blit(bg_img, [(-tmr)%3200, 0])
        #こうかとんを貼り付ける
        #なめらかに動かす
        kk_img = pg.image.load("ex01/fig/3.png")
        kk_img = pg.transform.flip(kk_img, True, False)
        kk_img = pg.transform.rotozoom(kk_img, angle, 1.0)
        screen.blit(kk_img, [300,200])

        pg.display.update()
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()