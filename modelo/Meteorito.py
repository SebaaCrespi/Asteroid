import pygame
from random import randint

class Meteorito(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagea = pygame.image.load('img/meteorito/meteorito.png')
        self.imageb = pygame.image.load('img/meteorito/meteorito90deg.png')
        self.imagec = pygame.image.load('img/meteorito/meteorito180deg.png')
        self.imaged = pygame.image.load('img/meteorito/meteorito270deg.png')
        self.imgexplosion = pygame.image.load('img/meteorito/explosion.png')
        self.lstimg = [self.imagea,self.imageb,self.imagec,self.imaged,self.imgexplosion]
        self.posimg = randint(0,3)
        self.imgMeteorito = self.lstimg[self.posimg]
        self.rect = self.imgMeteorito.get_rect()
        self.rect.centery = randint(-500,-60)
        self.rect.centerx = randint(30,994)
        self.speed = 0.1
        self.out = False
        self.soundboom = pygame.mixer.Sound('sounds/explosionmarian.wav')
        self.timeboom = 9999999

    def movimiento(self,time):
        self.rect.centery += self.speed * time
        self.rect.centerx == self.rect.centerx
        if self.rect.centery >= 700:
            self.out = True

    def explosion(self,seg):
        self.posimg = 4
        self.speed = 0
        self.timeboom = seg
        self.soundboom.play()

    def dibujar(self,superficie): 
        self.imgMeteorito = self.lstimg[self.posimg]
        superficie.blit(self.imgMeteorito,self.rect)
