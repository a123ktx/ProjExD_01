import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    # scr = pg.display.get_surface()
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    #こうかとんの情報
    kk_img1 = pg.image.load("ex01/fig/3.png")
    kk_img1 = pg.transform.flip(kk_img1, True, False)
    kk_img2 = pg.transform.rotozoom(kk_img1, 10, 1.0)
    kk_imgs = [kk_img1, kk_img2]

    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        tmr += 1
        screen.blit(bg_img, [0, 0])
        #こうかとんを貼り付ける
        #タイムステップに応じて交互に表示させる
        if tmr % 2 == 0:
            screen.blit(kk_imgs[0], [300,200])
        elif tmr % 2 == 1:
            screen.blit(kk_imgs[1],[300,200])

        pg.display.update()
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()