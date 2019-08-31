import pygame as pg

def distance (a, b):
    x1 = a[0]
    y1 = a[1]

    x2 = b[0]
    y2 = b[1]

    dx = (x2 - x1) ** 2
    dy = (y2 - y1) ** 2

    return ( dx + dy ) ** 0.5

def translate (surface:pg.surface, pos:tuple):
    temp_surf = surface.copy()
    surface.fill((0, 0, 0))

    rect = temp_surf.get_rect()

    surface.blit(temp_surf, pos)

    return pos
