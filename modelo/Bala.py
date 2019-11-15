import pygame

class Bala(pygame.sprite.Sprite):
    def __init__(self,posx,posy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/nave/bala.jpg')
        self.rect = self.image.get_rect()
        self.rect.centerx = posx
        self.rect.bottom = posy
        self.speed = 0.7

    def trayectoria(self):
        self.rect.top -= self.speed

    def dibujar(self,superficie):
        superficie.blit(self.image,self.rect)