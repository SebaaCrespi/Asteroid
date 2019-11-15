import pygame,sys,time

from pygame.locals import *
from random import randint

from modelo.Bala import *
from modelo.Nave import * 
from modelo.Meteorito import *


width = 1024
height = 600

lstMeteorito = []

# *-. FUNCIONES .-*
def disparos(self,superficie,seg):
    if len(self.listaDisparo) > 0:
        for bala in self.listaDisparo:
            bala.dibujar(superficie) 
            bala.trayectoria()
            if bala.rect.top <= 0:
                self.listaDisparo.remove(bala)
            else:
                for m in lstMeteorito:
                   if bala.rect.colliderect(m.rect):
                        self.listaDisparo.remove(bala)
                        m.explosion(seg)
                        self.score += 1                    

def controlmeteoritos(window,time,self,seg,width,height):
    if len(lstMeteorito) > 0:
            for m in lstMeteorito:
                if m.out == False: 
                    m.movimiento(time,height)
                    m.dibujar(window)
                else:
                    self.hearts -= 1
                    lstMeteorito.remove(m)
                    agregarMeteoritos(1,width)

                if (m.timeboom + 1) <= seg:
                    lstMeteorito.remove(m)
                    agregarMeteoritos(1,width)

                if m.rect.colliderect(self.rect):
                    lstMeteorito.remove(m)
                    self.damage(seg)
                    agregarMeteoritos(1,width)
                    

    if len(lstMeteorito) == 0:
        agregarMeteoritos(5)

def agregarMeteoritos(cant,width):
    i=0
    while(i < cant):
        m = Meteorito(width)
        lstMeteorito.append(m)
        i += 1

#--------------------------------------------------
def asteroid():
    # IMAGENES DEL JUEGO
    window = pygame.display.set_mode((width,height))
    windowbg = pygame.image.load("img/fondo_galaxy.png")
    tablebg = pygame.image.load("img/bg-table.png")
    heart = pygame.image.load("img/nave/heart.png")

    # TITULO 
    pygame.display.set_caption("Asteroid")

    # SE CREAN OBJETOS PRINCIPALES PARA COMENZAR
    nave = Nave()
    agregarMeteoritos(5,width)
    
    # FUENTES
    fontText = pygame.font.Font('fonts/Pixeled.ttf', 8)
    fontEnd = pygame.font.Font('fonts/DroidSans.ttf', 40)

    # COLORES
    gris  = pygame.Color(125,125,125)
    blanco  = pygame.Color(255,255,255)

    # RELOJ 
    reloj = pygame.time.Clock()

    # BANDERA PARA FINALIZAR EL JUEGO
    enJuego = True

    while True:
        time = reloj.tick(60) 
        timer = pygame.time.get_ticks()
        seg = (timer/1000)
        keys = pygame.key.get_pressed()

        # CAPTURAR EVENTOS
        for evento in pygame.event.get():
            if evento.type == QUIT:
                sys.exit(0)
            if enJuego == True:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == K_SPACE:
                        nave.disparar((timer/1000))
        if enJuego == True:              
            if keys[K_a] or keys[K_LEFT]:
                nave.moverIZQ(time)
            if keys[K_d] or keys[K_RIGHT]:
                nave.moverDER(time)

            # MOSTRAR
            window.blit(windowbg,(0,0))
            controlmeteoritos(window,time,nave,seg,width,height)
            nave.luces(seg)
            nave.dibujar(window)
            disparos(nave,window,seg)
            window.blit(tablebg,(0,0))
            timetxt = pygame.font.Font.render(fontText,"TIME: "+str(seg), 1, blanco)
            window.blit(timetxt,(10,5))
            scoretxt = pygame.font.Font.render(fontText,"SCORE: "+str(nave.score), 1, blanco)
            window.blit(scoretxt,(10,25))
            lifestxt = pygame.font.Font.render(fontText,"LIFES: ", 1, blanco)
            window.blit(lifestxt,(10,45))

            if nave.hearts >= 1:
                window.blit(heart,(55,50))
            if nave.hearts >= 2:
                window.blit(heart,(75,50))
            if nave.hearts >= 3:
                window.blit(heart,(95,50))
            if nave.hearts <= 0:
                nave.vida = False
                enJuego = False
                    

        else:
            window.blit(windowbg,(0,0))
            msgend= pygame.font.Font.render(fontEnd,"Fin del juego", 10, gris)
            window.blit(msgend,((width/2)-120,(height/2) -50))


        pygame.display.flip()
    return 0

if __name__ == '__main__':
    pygame.init()
    asteroid()


