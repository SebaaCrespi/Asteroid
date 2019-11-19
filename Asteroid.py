import pygame,sys,time

from pygame.locals import *
from random import randint

from modelo.Bala import *
from modelo.Nave import * 
from modelo.Meteorito import *

width = 1024
height = 600

# BOTON
class Boton(pygame.sprite.Sprite):
    def __init__(self,img1,img2,posx,posy):
        self.imgunselect = img1
        self.imgselect = img2
        self.currentimg = self.imgunselect
        self.rect = self.currentimg.get_rect() 
        self.rect.left,self.rect.top = (posx,posy)

    def update(self,display,cursor):
        if cursor.colliderect(self.rect):
            self.currentimg = self.imgselect
        else:
            self.currentimg = self.imgunselect

        display.blit(self.currentimg,self.rect)

# CURSOR
class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1 )
    
    def update(self):
        self.left,self.top = pygame.mouse.get_pos()

# *-. FUNCIONES .-*
def disparos(self,lstMeteorito,superficie,seg):
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

def controlmeteoritos(window,lstMeteorito,time,self,seg,width,height):
    if len(lstMeteorito) > 0:
            for m in lstMeteorito:
                if m.out == False: 
                    m.movimiento(time,height)
                    m.dibujar(window)
                else:
                    self.hearts -= 1
                    lstMeteorito.remove(m)
                    agregarMeteoritos(lstMeteorito,1,width)

                if (m.timeboom + 1) <= seg:
                    lstMeteorito.remove(m)
                    agregarMeteoritos(lstMeteorito,1,width)

                if m.rect.colliderect(self.rect):
                    lstMeteorito.remove(m)
                    self.damage(seg)
                    agregarMeteoritos(lstMeteorito,1,width)
                    

    if len(lstMeteorito) == 0:
        agregarMeteoritos(lstMeteorito,5,width)

def agregarMeteoritos(lstMeteorito,cant,width):
    i=0
    while(i < cant):
        m = Meteorito(width)
        lstMeteorito.append(m)
        i += 1

def comenzarJuego(window,cursor):
    # MUSICA DE FONDO
    fondoSound = pygame.mixer.Sound("sounds/fondofin.wav")

    # IMAGENES DEL JUEGO
    windowbg = pygame.image.load("img/fondo_galaxy.png")
    tablebg = pygame.image.load("img/bg-table.png")
    heart = pygame.image.load("img/nave/heart.png")
    finbg = pygame.image.load("img/fin/fondo-fin.png")
    volver = pygame.image.load("img/fin/volver.png")
    volverselect = pygame.image.load("img/fin/volver-select.png")

    # SE CREAN OBJETOS PRINCIPALES PARA COMENZARs
    nave = Nave()
    volverbtn = Boton(volver,volverselect,(width/2)-111,(height/2) + 90)
    lstMeteorito = []
    # FUENTES
    fontText = pygame.font.Font('fonts/Pixeled.ttf', 8)
    fontEndp = pygame.font.Font('fonts/Pixeled.ttf', 18)

    # COLORES
    gris  = pygame.Color(125,125,125)
    blanco  = pygame.Color(255,255,255)
    
    # RELOJ 
    reloj = pygame.time.Clock()

    # BANDERA PARA FINALIZAR EL JUEGO
    perdiste = 1
    enJuego = True
    volverMenu = False

    while not volverMenu:
        time = reloj.tick(60) 
        timer = pygame.time.get_ticks()
        seg = (timer/1000)
        keys = pygame.key.get_pressed()
        cursor.update()
           

        if enJuego == True:   
            # CAPTURAR EVENTOS      
            for evento in pygame.event.get():
                if evento.type == QUIT:
                    sys.exit(0)
                #if evento.type == pygame.KEYDOWN:
                    
            if keys[K_SPACE]:
                nave.disparar((timer/1000)) 
            if keys[K_a] or keys[K_LEFT]:
                nave.moverIZQ(time)
            if keys[K_d] or keys[K_RIGHT]:
                nave.moverDER(time)

            # MOSTRAR
            window.blit(windowbg,(0,0))
            controlmeteoritos(window,lstMeteorito,time,nave,seg,width,height)
            nave.luces(seg)
            nave.dibujar(window)
            disparos(nave,lstMeteorito,window,seg)
            window.blit(tablebg,(0,0))
            scoretxt = pygame.font.Font.render(fontText,"SCORE: "+str(nave.score), 1, blanco)
            window.blit(scoretxt,(10,0))
            lifestxt = pygame.font.Font.render(fontText,"LIFES: ", 1, blanco)
            window.blit(lifestxt,(10,25))

            if nave.hearts >= 1:
                window.blit(heart,(55,30))
            if nave.hearts >= 2:
                window.blit(heart,(75,30))
            if nave.hearts >= 3:
                window.blit(heart,(95,30))
            if nave.hearts <= 0:
                nave.vida = False
                enJuego = False
                    
        else: #SI enJuego NO es True: (El juego terminó)
            if perdiste == 1:
                pygame.mixer.music.stop()
                fondoSound.play()
                fondoSound.set_volume(1.0)
                perdiste += 1

            
            window.blit(finbg,(0,0))
            scoretxt = pygame.font.Font.render(fontEndp,str(nave.score), 1, blanco)
            window.blit(scoretxt,((width/2)+45 ,(height/2) - 40))
            volverbtn.update(window,cursor)
        
            for evento in pygame.event.get():
                if evento.type == QUIT:
                    sys.exit(0)
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if volverbtn.currentimg == volverbtn.imgselect:
                        volverMenu = True
                        
        pygame.display.flip()

    fondoSound.stop()
    

#--------------------------------------------------
def asteroid():
    # SE CREA LA PANTALLA CON UN ANCHO Y ALTO
    window = pygame.display.set_mode((width,height))

    # TITULO 
    pygame.display.set_caption("Asteroid")
    
    # MUSICA DEL JUEGO
    pygame.mixer.music.load("sounds/musicaJuego.mp3")

    # IMAGENES DEL MENU
    menubg = pygame.image.load('img/menu/fondo_menu.jpg')
    comenzar = pygame.image.load("img/menu/comenzar.png")
    comenzarSelect = pygame.image.load("img/menu/comenzar-select.png")
    records = pygame.image.load("img/menu/records.png")
    recordsSelect = pygame.image.load("img/menu/records-select.png")
    salir = pygame.image.load("img/menu/salir.png")
    salirSelect = pygame.image.load("img/menu/salir-select.png")

    # BOTONES DEL MENÚ
    comenzarBtn = Boton(comenzar,comenzarSelect,396,328)
    recordsBtn = Boton(records,recordsSelect,386,378)
    salirBtn = Boton(salir,salirSelect,356,428)
    
    # CURSOR PARA EL MENÚ
    cursor = Cursor()

    #INICIA EL MENÚ
    menu = True
    musica = 1
    while menu == True:
        if musica == 1:
            pygame.mixer.music.play(-1,1.7)
            pygame.mixer.music.set_volume(0.1)
            musica += 1
        
        window.blit(menubg,(0,0))
        comenzarBtn.update(window,cursor)
        recordsBtn.update(window,cursor)
        salirBtn.update(window,cursor)
        cursor.update()
        
        for evento in pygame.event.get():
            if evento.type == QUIT:
                sys.exit(0)
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if comenzarBtn.currentimg == comenzarBtn.imgselect:
                    comenzarJuego(window,cursor)
                if recordsBtn.currentimg == recordsBtn.imgselect:
                    pass
                if salirBtn.currentimg == salirBtn.imgselect:
                    sys.exit(0)
        
        pygame.display.flip()

    
    return 0

if __name__ == '__main__':
    pygame.init()
    asteroid()


