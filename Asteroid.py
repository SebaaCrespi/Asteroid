import pygame,sys,time

from pygame.locals import *
from random import randint

from modelo.Bala import *
from modelo.Nave import * 
from modelo.Meteorito import *


lstMeteorito = []
cantmet = 0

# FUNCIONES
def disparos(self,superficie):
    if len(self.listaDisparo) > 0:
        for bala in self.listaDisparo:
            bala.dibujar(superficie) 
            bala.trayectoria()
            if bala.rect.top <= 0:
                self.listaDisparo.remove(bala)
            else:
                for m in lstMeteorito:
                   if bala.rect.colliderect(m.rect):
                       lstMeteorito.remove(m)
                       self.listaDisparo.remove(bala)

def controlmeteoritos(window,time,self):
    if len(lstMeteorito) > 0:
            for m in lstMeteorito:
                if m.out == False: 
                    m.movimiento(time)
                    m.dibujar(window)
                else:
                    new = Meteorito()
                    lstMeteorito.remove(m)
                    lstMeteorito.append(new)
                if m.rect.colliderect(self.rect):
                    pass
    if len(lstMeteorito) == 0:
        agregarMeteoritos(5)

def agregarMeteoritos(cant):
    i=0
    while(i < cant):
        m = Meteorito()
        lstMeteorito.append(m)
        i += 1

#--------------------------------------------------
def asteroid():
    window = pygame.display.set_mode((1024,600))
    windowbg = pygame.image.load("img/fondo_galaxy.png")
    pygame.display.set_caption("Asteroid")
    nave = Nave()
    fuente = pygame.font.Font('fonts/DroidSans.ttf', 25)
    agregarMeteoritos(5)
    gris  = pygame.Color(125,125,125)
    reloj = pygame.time.Clock()
    enJuego = True
    while True:
        time = reloj.tick(60) 
        timer = pygame.time.get_ticks()
        keys = pygame.key.get_pressed()

        for evento in pygame.event.get():
            if evento.type == QUIT:
                sys.exit(0)
            if enJuego == True:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == K_SPACE:
                        nave.disparar()
        if keys[K_a] or keys[K_LEFT]:
            nave.moverIZQ(time)
        if keys[K_d] or keys[K_RIGHT]:
            nave.moverDER(time)

        window.blit(windowbg,(0,0))
        controlmeteoritos(window,time,nave)
        nave.dibujar(window)
        disparos(nave,window)
        tiempo = pygame.font.Font.render(fuente,"Tiempo: "+str(timer/1000), 1, gris)
        window.blit(tiempo,(10,10))

        pygame.display.flip()
    return 0

if __name__ == '__main__':
    pygame.init()
    asteroid()


