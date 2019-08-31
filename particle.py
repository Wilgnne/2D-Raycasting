import math, pgUtils
import pygame as pg
from ray import Ray

class Particle:

    def __init__ (self, x, y):
        self.pos = [x, y]
        self.rays = []
        
        for angle in range(0, 360, 1):
            radians = math.radians(angle)
            self.rays.append(Ray(self.pos, (math.cos(radians), math.sin(radians))))
    
    def update (self, newPos):
        self.pos[0] = newPos[0]
        self.pos[1] = newPos[1]
    
    def look (self, screen, walls):
        for ray in self.rays:
            closest = None
            record = math.inf
            for wall in walls:
                pt = ray.cast(wall)
                if pt:
                    d = pgUtils.distance(self.pos, pt)
                    if d < record:
                        record = d
                        closest = pt
            if closest:
                pg.draw.line(screen, (255, 255, 255), self.pos, closest, 1)
    
    def show (self, screen, walls):
        pg.draw.circle(screen, (255, 255, 255), list(map(int, self.pos)), 5)

        for ray in self.rays:
            ray.show(screen)
