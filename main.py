import time

from pygame import*

window = display.set_mode((700, 500))
display.set_caption('Доганялки')
background = transform.scale(image.load('background.png'), (700,500))
clock = time.Clock()
FPS = 60
run = True
x1 = 100
y1 = 350
sprite1 = transform.scale(image.load('sprite1 (2).png'), (65,65))
x2 = 150
y2 = 420
sprite2 = transform.scale(image.load('sprite2.png'), (65,65))
while run:
    window.blit(background, (0,0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))
    for e in event.get():
        if e.type == QUIT:
            run = False
    keys_pressed = key.get_pressed()
    if keys_pressed[K_LEFT] and x1 > 3:
        x1 -= 10
    if keys_pressed[K_RIGHT] and x1 < 595:
        x1 += 10
    if keys_pressed[K_UP] and y1 > 5:
        y1 -= 10
    if keys_pressed[K_DOWN] and y1 < 395:
        y1 += 10

    if keys_pressed[K_d] and x2 > 3:
        x2 -= 10
    if keys_pressed[K_r] and x2 < 595:
        x2 += 10
    if keys_pressed[K_u] and y2 > 5:
        y2 -= 10
    if keys_pressed[K_n] and y2 < 395:
        y2 += 10
    display.update()
    clock.tick(FPS)
