import pygame

from ..mesper import Event


class RectangleCollision(Event):

    def __init__(self, ent1: int, rect1: pygame.Rect, ent2: int, rect2: pygame.Rect):
        self.ent1 = ent1
        self.rect1 = rect1
        self.ent2 = ent2
        self.rect2 = rect2
