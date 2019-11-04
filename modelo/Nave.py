import pygame
from modelo.Bala import *

class Nave(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/nave/ovni-min.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = 512
        self.rect.centery = 560
        self.speed = 0.3
        self.listaDisparo = []
        self.vida = True
        self.hearts = 3
        self.soundShot = pygame.mixer.Sound('sounds/disparo2.wav')

    def moverIZQ(self,time):
        if self.vida == True:
            if self.rect.left >= 0:
                self.rect.centerx -= self.speed * time

    def moverDER(self,time):
        if self.vida == True:
            if self.rect.right <= 1024:
                self.rect.centerx += self.speed * time

    def luces(self,timer,time):
        if int(timer/1000) == self.timeChange :
            self.timeChange += 1
            self.posimg += 1

            if self.posimg > len(self.lstimg) -1:
                self.posimg = 0
    def disparar(self):
        bala = Bala(self.rect.centerx,self.rect.top)
        self.listaDisparo.append(bala)
        self.soundShot.play()

    def dibujar(self,superficie):
        superficie.blit(self.image,self.rect)
