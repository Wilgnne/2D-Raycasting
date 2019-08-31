import pygame as pg

class Boundary:

    def __init__ (self, a, b):
        self.a = a
        self.b = b

    def show (self, screen, color = (255, 255, 255), strok = 1):
        pg.draw.line(screen, color, self.a, self.b, strok)