import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    img3 = pg.image.load("ex01/fig/3.png")
    img3 = pg.transform.flip(img3,True,False)
    img4 = pg.transform.rotate(img3,10)
    imglst = [img3,img4]
    tmr = 0
    x = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = -tmr
        screen.blit(bg_img, [x, 0])
        screen.blit(imglst[tmr%2],[300,200])
        pg.display.update()
        tmr += 1
        clock.tick(100)
        


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()