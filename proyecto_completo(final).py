#http://programarcadegames.com/python_examples/f.php?file=timer.py&lang=es
#http://programarcadegames.com/python_examples/show_file.php?lang=es&file=maze_runner.py
#http://www.chelintutorials.blogspot.com.co/p/descargas.html
#http://www.loserjuegos.com.ar/referencia/articulos/menu
import pygame
from pygame.locals import *
import random
# Colores
NEGRO = (0, 0, 0) 
BLANCO = (255, 255, 255) 
VERDE = (153,204,50)
ROJO_LADRILLO = (158, 40, 28)
 
pygame.init()
class escalera(pygame.sprite.Sprite):
    def __init__(self,imagen):
        pygame.sprite.Sprite.__init__(self)
        self.imagen=imagen
        self.rect=self.imagen.get_rect()
    def dibujar(self,superficie):
        superficie.blit(self.imagen,self.rect)
    def posicion(self,x,y):
        self.rect.left,self.rect.top=(x,y)
class malo(pygame.sprite.Sprite):
    
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.x=x
        self.y=y
        self.im1=pygame.image.load("mico3.png")
        self.im2=pygame.image.load("mico2.png")
        self.im1=pygame.transform.scale(self.im1,(60,60))
        self.im2=pygame.transform.scale(self.im2,(60,60))
        self.timetarget=20
        self.timenum=0
        self.currentimage=0
       
    def update(self):
        self.timenum+=1
        if(self.timenum==self.timetarget):
            if (self.currentimage==0):
                self.currentimage=1
            else:
                self.currentimage=0
            self.timenum=0
        self.render(pantalla)
        
    def render(self,pantalla):
        if (self.currentimage==0):
            pantalla.blit(self.im1,(self.x,self.y))
        else:
            pantalla.blit(self.im2,(self.x,self.y))
class bola_de_fuego(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.imagen=pygame.image.load("exploboulette2.png")
        self.rect=self.imagen.get_rect()
        self.rect.x=x
        self.rect.y=y
    def crear(self,pantalla):
        pantalla.blit(self.imagen, (self.rect.x,self.rect.y))
    def update (self,pantalla):
        self.crear(pantalla)
class princesa(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.im1=pygame.image.load("princesa.png")
        self.im1=pygame.transform.scale(self.im1,(30,38))
        self.rect=self.im1.get_rect()
        self.rect.x=x
        self.rect.y=y
    def render(self,pantalla):
        pantalla.blit(self.im1,(self.rect.x,self.rect.y))
    def update(self,pantalla):
        self.render(pantalla)
class Protagonista(pygame.sprite.Sprite): 
    mx = 0
    my = 0 
    nivel = None
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.image.load("negro1.png")
        self.mira="none"     
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top=(400,680)
    def update(self): 
        self.crear()
        self.gravedad(0.4)
         
        self.rect.x += self.mx
         
        lista_impactos_bloques = pygame.sprite.spritecollide(self, self.nivel.listade_plataformas, False)
        for bloque in lista_impactos_bloques:
            if self.mx > 0:
                self.rect.right = bloque.rect.left
            elif self.mx < 0:
                self.rect.left = bloque.rect.right
 
        self.rect.y += self.my
         
        lista_impactos_bloques = pygame.sprite.spritecollide(self, self.nivel.listade_plataformas, False) 
        for bloque in lista_impactos_bloques:
 
            if self.my > 0:
                self.rect.bottom = bloque.rect.top 
            elif self.my < 0:
                self.rect.top = bloque.rect.bottom
 
            self.my = 0
    def gravedad(self,gravedad):
        
        if self.my == 0:
            self.my = 1
        else:
            self.my += gravedad
    def crear(self):
        if self.rect.y >= 700 - self.rect.height and self.my >= 0:
            self.my = 0
            self.rect.y = 700 - self.rect.height
        
    def saltar(self):

        self.rect.y += 2
        lista_impactos_plataforma = pygame.sprite.spritecollide(self, self.nivel.listade_plataformas, False)
        self.rect.y -= 2
         
        if len(lista_impactos_plataforma) > 0 or self.rect.bottom >= 700:
            self.my = -10

    def ir_izquierda(self):
        self.mx = -4
    def ir_derecha(self):
        self.mx = 4
    def quieto(self):
        self.mx = 0
class Plataforma(pygame.sprite.Sprite):
 
    def __init__(self, largo, alto ):
        pygame.sprite.Sprite.__init__(self)
         
        self.image = pygame.Surface([largo, alto])
        self.image.fill(ROJO_LADRILLO)    
                 
        self.rect = self.image.get_rect()
class Nivel(object):    
    def __init__(self, protagonista,barril):
        self.listade_plataformas = pygame.sprite.Group()
        self.listade_enemigos = pygame.sprite.Group()
        self.protagonista = protagonista
        self.barril=barril  
    def update(self):
        self.listade_plataformas.update()
        self.listade_enemigos.update() 
    def draw(self, pantalla):
         
        pantalla.fill(NEGRO)
                   
        self.listade_plataformas.draw(pantalla)
        self.listade_enemigos.draw(pantalla)      
class Nivel_1(Nivel):
    def __init__(self, protagonista,barril):
        """ Creamos el nivel 1. """
         
        Nivel.__init__(self, protagonista,barril)
         
        nivel = [ #[800,15,0,685],
                  [650, 20, 80, 604],[25,20,776,604],
                  [100,20,0,502],[80,20,80,502],[55,20,206,502],[100,20,240,502],[100,20,320,502],[100,20,400,502],[100,20,480,502],[100,20,560,502],[100,20,640,502],
                  [100,20,720,394],[100,20,640,394],[100,20,560,394],[30,20,480,394],[41,20,556,394],[100,20,400,394],[100,20,320,394],[100,20,240,394],[100,20,160,394],[100,20,80,394],
                  [100,20,0,284],[100,20,80,284],[100,20,160,284],[20,20,240,284],[51,20,306,284],[100,20,320,284],[100,20,400,284], [100,20,480,284],[100,20,560,284],[100,20,640,284],
                  [100,20,720,170],[20,20,640,170],[51,20,706,170],[100,20,560,170],[100,20,480,170],[100,20,400,170],[100,20,320,170],[100,20,240,170],[100,20,160,170],[100,20,80,170],
                  [95,20,0,90],[288,20,133,90],[150,20,466,90]
                  ]
 
        for plataforma in nivel:
            bloque = Plataforma(plataforma[0], plataforma[1])
            bloque.rect.x = plataforma[2]
            bloque.rect.y = plataforma[3]
            bloque.protagonista = self.protagonista
            bloque.barril=self.barril
            self.listade_plataformas.add(bloque)
class Nivel_2(Nivel):
 
    def __init__(self, protagonista,barril):
        """ Creamos el nivel 2. """
         
        Nivel.__init__(self, protagonista,barril)
         
        nivel = [ #[800,15,0,685],
                  [628, 20, 100, 604],[55,20,0,604],
                  [170,20,198,535],[100,20,400,520],[100,20,480,520],[100,20,560,520],
                  [100,20,720,420],[100,20,640,420],[100,20,560,420],[30,20,480,420],[33,20,548,420],[100,20,400,420],[160,20,240,420],[100,20,160,420],
                  [100,20,160,310],[20,20,240,310],[100,20,298,310],[162,20,400,294], [100,20,560,294],[150,20,640,294],
                  [100,20,720,170],[20,20,640,170],[43,20,698,170],[100,20,560,170],[200,20,400,170],[100,20,320,170],
                  [419,20,0,90],[336,20,466,90]
                  ]
 
        for plataforma in nivel:
            bloque = Plataforma(plataforma[0], plataforma[1])
            bloque.rect.x = plataforma[2]
            bloque.rect.y = plataforma[3]
            bloque.protagonista = self.protagonista
            bloque.barril=self.barril
            self.listade_plataformas.add(bloque)

pantalla = pygame.display.set_mode((40,40))
class Menu:
    
    def __init__(self, opciones):
        self.opciones = opciones
        self.font = pygame.font.Font('BREAK IT.ttf', 28)
        self.seleccionado = 0
        self.total = len(self.opciones)
        self.mantiene_pulsado = False

    def actualizar(self):

        k = pygame.key.get_pressed()

        if not self.mantiene_pulsado:
            if k[K_UP]:
                self.seleccionado -= 1
            elif k[K_DOWN]:
                self.seleccionado += 1
            elif k[K_RETURN]:

                # Invoca a la función asociada a la opción.
                titulo, funcion = self.opciones[self.seleccionado]
                #print "Selecciona la opción '%s'." %(titulo)
                funcion()

        # procura que el cursor esté entre las opciones permitidas
        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1

        # indica si el usuario mantiene pulsada alguna tecla.
        self.mantiene_pulsado = k[K_UP] or k[K_DOWN] or k[K_RETURN]


    def imprimir(self, screen):
        """Imprime sobre 'screen' el texto de cada opción del menú."""

        total = self.total
        indice = 0
        altura_de_opcion = 30
        x = 155
        y = 185
        
        for (titulo, funcion) in self.opciones:
            if indice == self.seleccionado:
                color = (200, 0, 0)
            else:
                color = (0, 0, 0)

            imagen = self.font.render(titulo, 1, color)
            posicion = (x, y + altura_de_opcion * indice)
            indice += 1
            screen.blit(imagen, posicion)


def comenzar_nivel_1():
    def main():
        """ Programa Principal """
            
        # Definimos el alto y largo de la pantalla 
        dimensiones = [800, 700] 
        pantalla = pygame.display.set_mode(dimensiones) 
           
        pygame.display.set_caption("DON KING KONG") 
        tipodeletra1=pygame.font.SysFont("BREAK IT.ttf",100)
        tipodeletra2=pygame.font.SysFont("BREAK IT.ttf",28)

        #variables del cronometro
        
        def mensaje1(txt,color,x,y):
                texinpantalla = tipodeletra1.render(txt,True,color)
                pantalla.blit(texinpantalla,(x,y))
        def mensaje2(txt,color,x,y):
                texinpantalla = tipodeletra2.render(txt,True,color)
                pantalla.blit(texinpantalla,(x,y))
        def vida(vida):
            text1= tipodeletra2.render("Vidas: "+str(vida), True, BLANCO)
            pantalla.blit(text1,(0,0)) 
        def puntaje(puntaje):
            text2= tipodeletra2.render("Puntaje: "+str(puntaje), True, VERDE)
            pantalla.blit(text2,(200,0)) 
        class Proyectil(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load("exploboulette2.png")
                self.rect = pygame.Rect(protagonista.rect.left, protagonista.rect.top+11, 10, 4)
                self.velocidad = 10
                if protagonista.mira == "izq":
                    self.velocidad*=-1
            def update(self,pantalla):
                self.rect.x+=self.velocidad
                pantalla.blit(self.image, (self.rect.left, self.rect.top))
        class Barriles(pygame.sprite.Sprite):
            #x=400
            #y=100
            direc="der"
            mx=0
            my=0
            nivel=None
            def __init__(self, posicionx, posiciony,direc1):
                    
                pygame.sprite.Sprite.__init__(self)
                self.image=pygame.image.load("barril.png")
                self.image=pygame.transform.scale(self.image,(18,18))
                self.rect=self.image.get_rect()
                self.rect.x=posicionx
                self.rect.top=posiciony
                direc=direc1="izq"
                pygame.sprite.Sprite.__init__(self)
                rand=random.randint(0,5)
            def update(self):
                self.mover()
                self.gravedad(0.4)
                self.rect.x += self.mx
                lista_impactos_bloques1 = pygame.sprite.spritecollide(self,nivel.listade_plataformas, False)
                for bloque in lista_impactos_bloques1:
                    if self.mx > 0:
                        self.rect.right = bloque.rect.left
                    elif self.mx < 0:
                        self.rect.left = bloque.rect.right

                self.rect.y += self.my
                     
                lista_impactos_bloques1 = pygame.sprite.spritecollide(self, nivel.listade_plataformas, False) 
                for bloque in lista_impactos_bloques1:
                    if self.my > 0:
                        self.rect.bottom = bloque.rect.top 
                    elif self.my < 0:
                        self.rect.top = bloque.rect.bottom

                    self.my = 0
                        
                self.crear(pantalla)
            def gravedad(self,gravedad):
                if self.my == 0:
                    self.my = 1
                else:
                    self.my += gravedad

                
            def crear(self,pantalla):
                pantalla.blit(self.image,(self.rect.centerx,self.rect.top))
                if self.rect.y >= 700 - self.rect.height and self.my >= 0:
                    self.my = 0
                    self.rect.y = 700 - self.rect.height
            def mover(self):
                if 0<self.rect.top<90:
                    self.rect.centerx+=2
                if 110<self.rect.top<170:
                    self.rect.centerx+=2
                if 190<self.rect.top<284:
                    self.rect.centerx+=-2
                if 304<self.rect.top<394:
                    self.rect.centerx+=2
                if 414<self.rect.top<502:
                    self.rect.centerx+=-2
                if 532<self.rect.top<604:
                    self.rect.centerx+=2
                if 624<self.rect.top<700:
                    self.rect.centerx+=-2

        # Creamos al protagonista......................
        protagonista = Protagonista()
        mico=malo(240,30)
        barril=Barriles(100,100,"none")
        bola=bola_de_fuego(600,570)
        princess=princesa(580,50)
        nivel=Nivel_1(protagonista,barril)

        #tiempo cronometro............................
        numFPS = 0
        FPS = 60
        start  =150
        font =pygame.font.SysFont("BREAK IT.ttf",28) 
        #grupos de sprites.............................
        barriles_lista=pygame.sprite.Group() 
        lista_de_todos_los_sprites=pygame.sprite.Group()  
        lista_de_proyectiles=pygame.sprite.Group()
        lista_de_escaleras=pygame.sprite.Group()
        bola_lista=pygame.sprite.Group()
        grupo_princesa=pygame.sprite.Group()
        lista_sprites_activos = pygame.sprite.Group()

        # Creamos todos los niveles.........................
        listade_niveles = []
        listade_niveles.append(Nivel_1(protagonista,barril))
         
        # Establecemos el nivel actual....................
        nivel_actual_no = 0
        nivel_actual = listade_niveles[nivel_actual_no]
         
        #..................................................
        protagonista.nivel = nivel_actual
        protagonista.rect.x = 340
        protagonista.rect.y = 700 - protagonista.rect.height
        lista_sprites_activos.add(protagonista)
        hecho = False
        

        #escaleras..............................................
        cy=pygame.image.load("escaleras3.png").convert_alpha()
        cy=pygame.transform.scale(cy,(45,95))
        ce=pygame.image.load("escaleras.png").convert_alpha()
        ce=pygame.transform.scale(ce,(45,103))
        ci=pygame.image.load("escaleras2.png").convert_alpha()
        ci=pygame.transform.scale(ci,(45,108))
        ca=pygame.image.load("escaleras2.png").convert_alpha()
        ca=pygame.transform.scale(ca,(45,110))
        cu=pygame.image.load("escaleras4.png").convert_alpha()
        cu=pygame.transform.scale(cu,(45,114))
        co=pygame.image.load("escaleras5.png").convert_alpha()
        co=pygame.transform.scale(co,(45,80))
        cp=pygame.image.load("escaleras6.png").convert_alpha()
        cp=pygame.transform.scale(cp,(45,79))

        #lis=[(("escaleras3.png"),(45,95)),(("escaleras.png"),(45,103)),(("escaleras2.png"),(45,108)),
         #   (("escaleras2.png"),(45,110)),(("escaleras4.png"),(45,114)),(("escaleras5.png"),(45,80)),
          #  (("escaleras6.png"),(45,79))]
        
        #se agrega a la clase de escalera.............................
        escal1=escalera(cy)
        escal2=escalera(ce)
        escal3=escalera(ci)
        escal4=escalera(ca)
        escal5=escalera(cu)
        escal6=escalera(co)
        escal7=escalera(cp)
        
           
        # Lo usamos para gestionar cuan rápido se actualiza la pantalla.
        reloj = pygame.time.Clock()

       
        #agregar cosas a lista..............................................
        lista_de_todos_los_sprites.add(protagonista)
        bola_lista.add(bola)
        grupo_princesa.add(princess)
        lista_de_escaleras.add(escal1,escal2,escal3,escal4,escal5,escal6,escal7)
        #variable para acabar el juego.......................................
        hecho = False
        #variable de vida....................................................
        vidas=1
        #variable para los puntajes..........................................
        puntajes=0
        #tiempo para que salgan los barriles...................................
        tiempo=0
        #variable para matar el jugador......................................
        gameover=False
        #variable para poner el proyectil a funcionar.........................
        haybala=False
        #variable para pasar el nivel 2........................................
        raro=False
        # -------- Bucle Principal del nivel 1 ----------- 
        while not hecho: 
            for evento in pygame.event.get(): # El usuario realizó alguna acción 
                if evento.type == pygame.QUIT: # Si el usuario hizo click en salir
                    hecho = True # Marcamos como hecho y salimos de este bucle
                # presiona una tecla....................................
                if evento.type == pygame.KEYDOWN:
                    #presiona  la tecla se mueve a la izquierda..................
                    if evento.key == pygame.K_LEFT:
                        protagonista.ir_izquierda()
                        protagonista.image = pygame.image.load("negrovolteado4.png")
                        protagonista.mira="izq"
                    #presiona  la tecla se mueve a la derecha..................
                    if evento.key == pygame.K_RIGHT:
                        protagonista.ir_derecha()
                        protagonista.image = pygame.image.load("negro4.png")
                        protagonista.mira="der"
                    #presiona  la tecla y salta..................
                    if evento.key == pygame.K_UP:
                        protagonista.saltar()
                        if protagonista.mira=="der":
                            protagonista.image= pygame.image.load("negro5.png")
                        else:
                            protagonista.image=pygame.image.load("negrovolteado5.png")
                    #si la variable es verdad se pueden disparar proyectiles
                    if haybala==True:
                        if evento.key == pygame.K_SPACE:
                        #Agregarle condicionante para cuando toca la pistola
                            tiro=Proyectil()
                            lista_de_proyectiles.add(tiro)
                            lista_de_todos_los_sprites.add(tiro)
                            if protagonista.mira=="izq":
                                protagonista.image=pygame.image.load("negrokamehavolteado.png")
                            else:
                                protagonista.image=pygame.image.load("negrokameha.png") 
                #si suelta la tecla                  
                if evento.type == pygame.KEYUP:
                    if evento.key == pygame.K_LEFT and protagonista.mx < 0: 
                        protagonista.quieto()
                        protagonista.image = pygame.image.load("negrovolteado1.png")

                    if evento.key == pygame.K_RIGHT and protagonista.mx > 0:
                        protagonista.quieto()
                        protagonista.image = pygame.image.load("negro1.png")
            # colision con la imagen de la bola. 
            if pygame.sprite.spritecollide(protagonista,bola_lista,True):
                    #se elimina esa imagen
                    bola_lista.remove(bola)
                    #permite que se use K_space para dispare
                    haybala=True

            

            #actualiza 2 grupos de sprites...........................
            lista_sprites_activos.update()
            nivel_actual.update()
            # Si el protagonista se acerca al lado derecho, se desplaza a la izquierda (-x)
            if protagonista.rect.right > 800:
                protagonista.rect.right = 800
         
            # Si el protagonista se acerca al lado izquierdo, se desplaza a la derecha (+x)
            if protagonista.rect.left < 0:
                protagonista.rect.left = 0
            

            #dibuja todo menos las escaleras..............
            nivel_actual.draw(pantalla)
            mico.update()
            grupo_princesa.update(pantalla)
            bola_lista.update(pantalla)


            #se da la posicion de las escaleras.................
            escal1.posicion(730,604)
            escal2.posicion(160,502)
            escal3.posicion(510,394)
            escal4.posicion(260,284)
            escal5.posicion(660,170)
            escal6.posicion(95,90)
            escal7.posicion(420,90)



            #se dibujan las escaleras.............................
            escal1.dibujar(pantalla)
            escal2.dibujar(pantalla)
            escal3.dibujar(pantalla)
            escal4.dibujar(pantalla)
            escal5.dibujar(pantalla)
            escal6.dibujar(pantalla)
            escal7.dibujar(pantalla)
            #se dibujan los grupos de sprites....................
            lista_sprites_activos.draw(pantalla)
            lista_de_todos_los_sprites.draw(pantalla)
            # se limita a 60 fps......................................... 
            reloj.tick(60) 
            #produccion de barriles......................................      
            if tiempo==120:
                barril=Barriles(240,65,"none")
                barriles_lista.add(barril)
                tiempo=0
            tiempo+=1
            barriles_lista.update()
            #genero el tiro..............................................
            for tiro in lista_de_proyectiles:
                tiro.update(pantalla)
                # Eliminamos el proyectil si sale de la   de la pantalla............
                if tiro.rect.x < -10:
                    lista_de_proyectiles.remove(tiro)
                    lista_de_todos_los_sprites.remove(tiro)
                elif tiro.rect.x  > 800:
                    lista_de_proyectiles.remove(tiro)
                    lista_de_todos_los_sprites.remove(tiro)
                #colision entre barriles y proyectil, se eliminan ambos y se suma al puntaje.........
                if pygame.sprite.spritecollide(tiro,barriles_lista, True):
                    barriles_lista.remove(barril)
                    lista_de_proyectiles.remove(tiro)
                    lista_de_todos_los_sprites.remove(tiro)
                    puntajes+=100
                    if puntaje==2500:
                        gameover=True

            #colision entre barriles y protagonista, se acaba el juego...................
            if pygame.sprite.spritecollide(protagonista,barriles_lista,True):
                vidas-=1
                if vidas==0:
                    gameover=True
            #colision entre princesa y protagonista,se pasa al nivel 2......................
            if pygame.sprite.spritecollide(protagonista,grupo_princesa,True):
                raro=True
            
             
            #imprimimos la vida y el puntaje.............................................
            vida(vidas)
            puntaje(puntajes)

            #cronometro del juego(el tiempo restante)...................................
            totseg  = start - (numFPS // FPS)
            if totseg < 0:
                totseg = 0
            minutos = totseg // 60
            segundos = totseg % 60
            texto12 = "Tiempo restante:{0:02}:{1:00}".format(minutos,segundos)
            text = font.render(texto12, False, VERDE)
            pantalla.blit(text, (400, 0))


            numFPS +=1
            # se actualiza la pantalla con todo lo que sea dibujado...................... 
            pygame.display.update()
            #es el loop para cuando pierde el protagonista...................................
            while gameover == True:
                pantalla.fill(NEGRO)
                mensaje1(("GAME OVER"),BLANCO,220,150)
                mensaje2(("(q) para salir del juego"),VERDE,250,300)
                mensaje2(("(r) para reiniciar del juego"),VERDE,250,340)

                

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            hecho = True
                            gameover = False
                        if event.key == pygame.K_r:
                            main()
                        else:
                            pass 

               
                pygame.display.update()
            #es el loop para cuando el protagonista llega hasta la princesa........................
            while raro == True:
                pantalla.fill(NEGRO)
                mensaje1(("GANASTE"),BLANCO,220,150)

                mensaje2(("(s) para pasar al nivel 2 del juego"),VERDE,250,340)

                

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        
                        if event.key == pygame.K_s:
                            comenzar_nivel_2() 
                        else:
                            pass 

               
                pygame.display.update()
        pygame.quit()
     
    if __name__ == "__main__":
        main()
    
def comenzar_nivel_2():
    def main():
        """ Programa Principal """
            
        # Definimos el alto y largo de la pantalla 
        dimensiones = [800, 700] 
        pantalla = pygame.display.set_mode(dimensiones) 
           
        pygame.display.set_caption("DON KING KONG") 
        tipodeletra1=pygame.font.SysFont("BREAK IT.ttf",100)
        tipodeletra2=pygame.font.SysFont("BREAK IT.ttf",28)

        #variables del cronometro
        numero_de_fotogramas = 0
        tasa_fotogramas = 60
        instante_de_partida = 150
        fuente = pygame.font.Font(None, 25)
        def mensaje1(txt,color,x,y):
                texinpantalla = tipodeletra1.render(txt,True,color)
                pantalla.blit(texinpantalla,(x,y))
        def mensaje2(txt,color,x,y):
                texinpantalla = tipodeletra2.render(txt,True,color)
                pantalla.blit(texinpantalla,(x,y))
        def vida(vida):
            text1= tipodeletra2.render("Vidas: "+str(vida), True, BLANCO)
            pantalla.blit(text1,(0,0))
        def puntaje(puntaje):
            text2= tipodeletra2.render("Puntaje: "+str(puntaje), True, VERDE)
            pantalla.blit(text2,(200,0))  
        class Proyectil(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load("exploboulette2.png")
                self.rect = pygame.Rect(protagonista.rect.left, protagonista.rect.top+11, 10, 4)
                self.velocidad = 10
                if protagonista.mira == "izq":
                    self.velocidad*=-1
            def update(self,pantalla):
                self.rect.x+=self.velocidad
                pantalla.blit(self.image, (self.rect.left, self.rect.top))
        class Barriles(pygame.sprite.Sprite):
            #x=400
            #y=100
            direc="der"
            mx=0
            my=0
            nivel=None
            def __init__(self, posicionx, posiciony,direc1):
                    
                pygame.sprite.Sprite.__init__(self)
                self.image=pygame.image.load("barril.png")
                self.image=pygame.transform.scale(self.image,(18,18))
                self.rect=self.image.get_rect()
                self.rect.x=posicionx=35
                self.rect.top=posiciony=100
                direc=direc1="izq"
                pygame.sprite.Sprite.__init__(self)
                rand=random.randint(0,5)
                self.velcaida=0
            def update(self):
                self.mover()
                self.calc_grav(0.4)
                self.rect.x += self.mx
                lista_impactos_bloques1 = pygame.sprite.spritecollide(self,nivel.listade_plataformas, False)
                for bloque in lista_impactos_bloques1:
                    if self.mx > 0:
                        self.rect.right = bloque.rect.left
                    elif self.mx < 0:
                        self.rect.left = bloque.rect.right

                self.rect.y += self.my
                     
                lista_impactos_bloques1 = pygame.sprite.spritecollide(self, nivel.listade_plataformas, False) 
                for bloque in lista_impactos_bloques1:
                    if self.my > 0:
                        self.rect.bottom = bloque.rect.top 
                    elif self.my < 0:
                        self.rect.top = bloque.rect.bottom

                    self.my = 0
                        
                self.crear(pantalla)
            def calc_grav(self,gravedad):
                if self.my == 0:
                    self.my = 1
                else:
                    self.my += gravedad

                
            def crear(self,pantalla):
                pantalla.blit(self.image,(self.rect.centerx,self.rect.top))
                if self.rect.y >= 700 - self.rect.height and self.my >= 0:
                    self.my = 0
                    self.rect.y = 700 - self.rect.height
            def mover(self):
                if 0<self.rect.top<90:
                    self.rect.centerx+=2
                if 110<self.rect.top<170:
                    self.rect.centerx+=2
                if 190<self.rect.top<310:
                    self.rect.centerx+=-2
                if 330<self.rect.top<420:
                    self.rect.centerx+=2
                if 440<self.rect.top<535:
                    self.rect.centerx+=-2
                if 555<self.rect.top<604:
                    self.rect.centerx+=2
                if 624<self.rect.top<700:
                    self.rect.centerx+=-2
        
        # Creamos al protagonista
        protagonista = Protagonista()
        mico=malo(35,30)
        barril=Barriles(35,100,"none")
        bola=bola_de_fuego(480,248)
        princess=princesa(700,50)
        nivel=Nivel_2(protagonista,barril)


        #cronometro variables.......................................................
        numFPS = 0
        FPS = 60
        start  =150
        font =pygame.font.SysFont("BREAK IT.ttf",28)
        #grupos de sprites...............................................
        barriles_lista=pygame.sprite.Group() 
        lista_de_todos_los_sprites=pygame.sprite.Group()  
        lista_de_proyectiles=pygame.sprite.Group()
        lista_de_escaleras=pygame.sprite.Group()
        bola_lista=pygame.sprite.Group()
        grupo_princesa=pygame.sprite.Group()
        lista_sprites_activos = pygame.sprite.Group()

        # se crea el nivel................................................
        listade_niveles = []
        listade_niveles.append(Nivel_2(protagonista,barril))
          
        # Establecemos el nivel actual.....................................
        nivel_actual_no = 0
        nivel_actual = listade_niveles[nivel_actual_no]
        protagonista.nivel = nivel_actual
         
        protagonista.rect.x = 340
        protagonista.rect.y = 700 - protagonista.rect.height
        #se agrega el protagonista al grupo de sprites principal..............
        lista_sprites_activos.add(protagonista)
        

        #escaleras................................................
        cy=pygame.image.load("escaleras3.png").convert_alpha()
        cy=pygame.transform.scale(cy,(45,95))
        ci=pygame.image.load("escaleras2.png").convert_alpha()
        ci=pygame.transform.scale(ci,(45,101))
        ca=pygame.image.load("escaleras2.png").convert_alpha()
        ca=pygame.transform.scale(ca,(45,111))
        cu=pygame.image.load("escaleras4.png").convert_alpha()
        cu=pygame.transform.scale(cu,(45,123))
        cp=pygame.image.load("escaleras6.png").convert_alpha()
        cp=pygame.transform.scale(cp,(45,80))
        #se agrega a la clase de escaleras........................
        escal1=escalera(cy)
        escal3=escalera(ci)
        escal4=escalera(ca)
        escal5=escalera(cu)
        escal7=escalera(cp)
        
        #gestiona las actualizaciones de la pantalla...................
        reloj = pygame.time.Clock()
        #agrego variables a grupos de sprites.............................
        lista_de_todos_los_sprites.add(protagonista)
        bola_lista.add(bola)
        grupo_princesa.add(princess)
        lista_de_escaleras.add(escal1,escal3,escal4,escal5,escal7)
        
        #variable de tiempo para que salgan los barriles...................
        tiempo=0
        #variable del loop......................................
        hecho = False
        #variable de vidas............................
        vidas=1
        #variable de puntajes...............
        puntajes=0
        #variable para matar al jugador.............
        gameover=False
        #variable para cuando es posible disparar los proyectiles.........
        haybala=False
        #variable para terminar el juego...........................
        raro=False
        # -------- Bucle Principal del Programa ----------- 
        while not hecho: 
            for evento in pygame.event.get(): # El usuario realizó alguna acción 
                if evento.type == pygame.QUIT: # Si el usuario hizo click en salir
                    hecho = True # Marcamos como hecho y salimos de este bucle
            
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_LEFT:
                        protagonista.ir_izquierda()
                        protagonista.image = pygame.image.load("negrovolteado4.png")
                        protagonista.mira="izq"

                    if evento.key == pygame.K_RIGHT:
                        protagonista.ir_derecha()
                        protagonista.image = pygame.image.load("negro4.png")
                        protagonista.mira="der"
                    if evento.key == pygame.K_UP:
                        protagonista.saltar()
                        if protagonista.mira=="der":
                            protagonista.image= pygame.image.load("negro5.png")
                        else:
                            protagonista.image=pygame.image.load("negrovolteado5.png")
                    if haybala==True:
                        if evento.key == pygame.K_SPACE:
                            tiro=Proyectil()
                            lista_de_proyectiles.add(tiro)
                            lista_de_todos_los_sprites.add(tiro)
                            if protagonista.mira=="izq":
                                protagonista.image=pygame.image.load("negrokamehavolteado.png")
                            else:
                                protagonista.image=pygame.image.load("negrokameha.png")                   
                if evento.type == pygame.KEYUP:
                    if evento.key == pygame.K_LEFT and protagonista.mx < 0: 
                        protagonista.quieto()
                        protagonista.image = pygame.image.load("negrovolteado1.png")

                    if evento.key == pygame.K_RIGHT and protagonista.mx > 0:
                        protagonista.quieto()
                        protagonista.image = pygame.image.load("negro1.png")

            if pygame.sprite.spritecollide(protagonista,bola_lista,True):
                    bola_lista.remove(bola)
                    haybala=True


            lista_sprites_activos.update()
            nivel_actual.update()
            # Si el protagonista se acerca al lado derecho, se desplaza a la izquierda (-x)
            if protagonista.rect.right > 800:
                protagonista.rect.right = 800
         
            # Si el protagonista se acerca al lado izquierdo, se desplaza a la derecha (+x)
            if protagonista.rect.left < 0:
                protagonista.rect.left = 0
            #dibuja todo menos las escaleras................................
            nivel_actual.draw(pantalla)
            mico.update()
            grupo_princesa.update(pantalla)
            bola_lista.update(pantalla)
            #se da la posicion de las escaleras................................
            escal1.posicion(55,604)
            escal3.posicion(510,420)
            escal4.posicion(260,310)
            escal5.posicion(660,170)
            escal7.posicion(420,90)
             #se dibujan las escaleras..............................................
            escal1.dibujar(pantalla)
            escal3.dibujar(pantalla)
            escal4.dibujar(pantalla)
            escal5.dibujar(pantalla)
            escal7.dibujar(pantalla)
            lista_sprites_activos.draw(pantalla)
            lista_de_todos_los_sprites.draw(pantalla)
            protagonista.colision_escalera(lista_de_escaleras)
            # Limitamos a 60 fps................................................... 
            reloj.tick(60) 
            #produccion de barriles.................................................      
            if tiempo==120:
                barril=Barriles(240,65,"none")
                barriles_lista.add(barril)
                tiempo=0
            tiempo+=1
            barriles_lista.update()
            #genero el tiro..........................................................
            for tiro in lista_de_proyectiles:
                tiro.update(pantalla)
                # Eliminamos el proyectil si vuela fuera de la pantalla
                if tiro.rect.x < -10:
                    lista_de_proyectiles.remove(tiro)
                    lista_de_todos_los_sprites.remove(tiro)
                elif tiro.rect.x  > 800:
                    lista_de_proyectiles.remove(tiro)
                    lista_de_todos_los_sprites.remove(tiro)
                #colision entre barriles y proyectiles, se eliman ambos....................
                if pygame.sprite.spritecollide(tiro,barriles_lista, True):
                    barriles_lista.remove(barril)
                    lista_de_proyectiles.remove(tiro)
                    lista_de_todos_los_sprites.remove(tiro)
                    puntajes+=100
                    if puntajes==2500:
                        gameover=True
            #colision con personaje y barril..............................................
            if pygame.sprite.spritecollide(protagonista,barriles_lista,True):
                vidas-=1
                if vidas==0:
                    gameover=True
            #colision con princesa y protagonista y gana el juego.........................
            if pygame.sprite.spritecollide(protagonista,grupo_princesa,True):
                raro=True            
             

            vida(vidas)
            puntaje(puntajes)
            #genera el cronometro...............................................
            totseg  = start - (numFPS // FPS)
            if totseg < 0:
                totseg = 0

            minutes = totseg // 60
            seconds = totseg % 60
            outtext = "Tiempo restante:{0:02}:{1:00}".format(minutes,seconds)
            text = font.render(outtext, False, VERDE)
            
            pantalla.blit(text, (400, 0))



            numFPS +=1

            # se actualiza la pantalla con todo lo que sea dibujado. 
            pygame.display.update()

            while gameover == True:
                pantalla.fill(NEGRO)
                mensaje1(("GAME OVER"),BLANCO,220,150)
                mensaje2(("(q) para salir del juego"),VERDE,250,300)
                mensaje2(("(r) para reiniciar del juego"),VERDE,250,340)

                

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            hecho = True
                            gameover = False
                        if event.key == pygame.K_r:
                            main()
                        else:
                            pass 
            while raro == True:
                pantalla.fill(NEGRO)
                mensaje1(("GANASTE"),BLANCO,220,150)
                mensaje2(("(q) para salir del juego"),VERDE,250,300)

                

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            hecho = True
                            gameover = False
                       
                        else:
                            pass 


               
                pygame.display.update()
            
        pygame.quit()
     
    if __name__ == "__main__":
        main()

def mostrar_opciones():
    print("Como jugar:\n(K_)es para saltar\n(K_LEFT) es para ir a la izquierda\n(K_RIGHT) es para ir a la derecha\n(K_SPACE)es para disparar los proyectiles\nCuando es alcanzado por un barril aparecen:\n(K_q)para salir del juego\n(K_r) para reiniciar el nivel\nCuando se llega hasta la princesa:\n(K_s) para pasar al nivel 2(solo si se esta en el nivel 1)")

def salir_del_programa():
    import sys
    sys.exit(0)


if __name__ == '__main__':
    
    salir = False
    opciones = [
        ("Jugar nivel 1", comenzar_nivel_1),
        ("Jugar nivel 2", comenzar_nivel_2),
        ("Instrucciones", mostrar_opciones),
        ("Salir", salir_del_programa)
        ]

    pygame.font.init()
    screen = pygame.display.set_mode((500, 400))
    fondo = pygame.image.load("FONDO_MENU2.png").convert()
    menu = Menu(opciones)

    while not salir:

        for e in pygame.event.get():
            if e.type == QUIT:
                salir = True

        screen.blit(fondo, (0, 0))
        menu.actualizar()
        menu.imprimir(screen)

        pygame.display.flip()
        pygame.time.delay(10)
