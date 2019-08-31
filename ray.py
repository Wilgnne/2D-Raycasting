import pygame as pg
import pgUtils
from boundary import Boundary

class Ray:

    def __init__ (self, pos, direction):
        self.pos = pos
        self.dir = direction
    
    def setDirection (self, direction):
        x = direction[0] - self.pos[0]
        y = direction[1] - self.pos[1]

        distance = pgUtils.distance(self.pos, direction)

        self.dir = (x / distance, y / distance)
    
    def show (self, screen, color = (255, 255, 255), strok = 1):

        #center = pgUtils.translate(screen, self.pos)
        #pg.draw.line(screen, color, center, (center[0] + self.dir[0] * 10, center[1] + self.dir[1] * 10), strok)
        pos = list(map(int, self.pos))
        pg.draw.line(screen, color, self.pos, (pos[0] + self.dir[0] * 10, pos[1] + self.dir[1] * 10), strok)
    
    def cast (self, wall: Boundary):
        x1 = wall.a[0]
        y1 = wall.a[1]

        x2 = wall.b[0]
        y2 = wall.b[1]

        x3 = self.pos[0]
        y3 = self.pos[1]

        x4 = self.pos[0] + self.dir[0]
        y4 = self.pos[1] + self.dir[1]

        det = ((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4))

        if det == 0:
            return False
        
        t = ((x1 - x3) * (y3 - y4)) - ((y1 - y3) * (x3 - x4))
        t /= det

        u = ((x1 - x2) * (y1 - y3)) - ((y1 - y2) * (x1 - x3))
        u /= -det

        if (0 < t < 1) and u > 0:
            x = x1 + t * (x2 - x1)
            y = y1 + t * (y2 - y1)
            return [int(x), int(y)]
        
        return False
