import pygame

from modelo.Bala import *

class Nave(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #-- img sin luces self.image = pygame.image.load('img/nave/ovni-min.png')
        self.imgluz1 = pygame.image.load('img/nave/ovni-min-luces1.png')
        self.imgluz2 = pygame.image.load('img/nave/ovni-min-luces2.png')
        self.imgdmg = pygame.image.load('img/nave/ovni-min-dmg.png')
        self.lstimgnave = [self.imgluz1,self.imgluz2,self.imgdmg] 
        self.posimg = 0
        self.imgnave = self.lstimgnave[self.posimg]
        self.rect = self.imgnave.get_rect()
        self.rect.centerx = 512
        self.rect.centery = 560
        self.speed = 0.3
        self.listaDisparo = []
        self.vida = True
        self.hearts = 3
        self.timeChange = 0.05 #AGREGAR UNA IMAGEN DEL OVNI CON LUCES Y HACER BIEN LA FUCION LUCES
        self.dmgrecived = False
        self.timedmg = 99999
        self.soundDmg = pygame.mixer.Sound('sounds/dmgc.wav')
        self.lastshot = 1
        self.score = 0
        self.soundShot = pygame.mixer.Sound('sounds/disparo2.wav')


    def moverIZQ(self,time):
        if self.vida == True:
            if self.rect.left >= 0:
                self.rect.centerx -= self.speed * time

    def moverDER(self,time):
        if self.vida == True:
            if self.rect.right <= 1024:
                self.rect.centerx += self.speed * time

    def luces(self,seg):
        if (self.timedmg + 0.25) <= seg or self.dmgrecived == False: 
            if seg - self.timeChange >= 0 :
                self.dmgrecived == False
                self.timeChange += 1
                self.posimg += 1

                if self.posimg > len(self.lstimgnave) - 2:
                        self.posimg = 0
                    

    def damage(self,seg):
        self.posimg = 2
        self.timedmg = seg
        self.hearts -= 1
        self.dmgrecived = True
        self.soundDmg.play()

    def disparar(self,timeshot):
        if timeshot - self.lastshot > 0.5 : #LIMITO LOS DISPAROS A 1 POR 0.5
            self.lastshot = timeshot
            bala = Bala(self.rect.centerx,self.rect.top)
            self.listaDisparo.append(bala)
            self.soundShot.play()

    def dibujar(self,superficie):
        self.imgnave = self.lstimgnave[self.posimg]
        superficie.blit(self.imgnave,self.rect)
