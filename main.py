import pygame as pg
import random
from boundary import Boundary
from ray import Ray
from particle import Particle

pg.init()

size = width, height = 640, 480
speed = [2, 2]
black = 0, 0, 0

screen = pg.display.set_mode(size)

print(screen.get_rect().center)

'''
walls = [Boundary((50, 50), (500, 50)),
         Boundary((500, 50), (500, 400)),
         Boundary((50, 400), (500, 400)),
         Boundary((50, 50), (50, 400)),
         Boundary((200, 200), (100, 300))]
'''

walls = []
for i in range(5):
    x1 = random.randint(0, width)
    y1 = random.randint(0, height)

    x2 = random.randint(0, width)
    y2 = random.randint(0, height)

    walls.append(Boundary((x1, y1), (x2, y2)))


velocity = 20

particle = Particle(150, 150)

isClosed = False

deltaTime = 1 / 60

while not isClosed:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isClosed = True
    
    key=pg.key.get_pressed()  #checking pressed keys
    if key[pg.K_a]: particle.pos[0] -= velocity * deltaTime
    if key[pg.K_d]: particle.pos[0] += velocity * deltaTime
    if key[pg.K_w]: particle.pos[1] -= velocity * deltaTime
    if key[pg.K_s]: particle.pos[1] += velocity * deltaTime


    particle.update(pg.mouse.get_pos())
    
    screen.fill(black)

    particle.show(screen, walls)
    particle.look(screen, walls)

    [b.show(screen) for b in walls]

    pg.display.update()

pg.quit()