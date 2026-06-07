import pygame
import random
from pygame.math import Vector2

class FRUIT:
    def __init__(self):
        #position/coordonee du fruit (x)
        self.randomize()
    def draw_fruit(self):
        #creer un rectangle
        fruit_rect=pygame.Rect(self.x*taille_bloc,self.y*taille_bloc,taille_bloc,taille_bloc)
        #dessiner le rectangle
        pygame.draw.rect (screen,(126,166,114),fruit_rect)
    def randomize(self):
        self.x=random.randint(0, nombre_bloc-1)
        self.y = random.randint(0, nombre_bloc - 1)
        self.pos = Vector2(self.x, self.y)

class SNAKE:
    def __init__(self):
        self.body= [Vector2(5,10),Vector2(4,10),Vector2(3,10)] #position de depart
        self.direction=Vector2(1,0) #ON VA A DROITE
        self.new_bloc=False
    def draw_snake(self):
        for bloc in self.body: #la liste
            #creer un rectangle
            snake_rect = pygame.Rect(int(bloc.x * taille_bloc),int(bloc.y * taille_bloc),taille_bloc, taille_bloc)
            #dessiner ce rectangle
            pygame.draw.rect(screen, (156, 190, 250), snake_rect)
    def move_snake (self):
        if self.new_bloc == True :
            body_copy=self.body[:]
            self.new_bloc = False
        else:
            body_copy = self.body[:-1]
        body_copy=[body_copy[0]+self.direction]+body_copy
        self.body=body_copy[:] #mettre a jour self body sinon aucune action
    def add_bloc(self):
        self.new_bloc=True


class MAIN:
    def __init__(self):
        self.fruit=FRUIT ()
        self.snake=SNAKE()
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
    def draw_elements (self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
    def check_collision (self):
        #si le snake et le fruits sont sur le meme bloc
        if self.snake.body[0]==self.fruit.pos:
            #repositionner ke fruit
            self.fruit.randomize()
            #ajoiuter un autre bloc au snake
            self.snake.add_bloc()
    def check_fail (self):
        #verifier si le snake est en dehors du screen
        if not (0<self.snake.body[0].x<nombre_bloc and 0<self.snake.body[0].y<nombre_bloc):
            pygame.quit()

        #verifier si le snake se mange
        for bloc in self.snake.body[1:]:
            if self.snake.body[0] == bloc:
                pygame.quit()

pygame.init()
taille_bloc=20
nombre_bloc=30
screen=pygame.display.set_mode((taille_bloc*nombre_bloc,taille_bloc*nombre_bloc))
clock=pygame.time.Clock()
main_game=MAIN()
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

#BOUCLE DU JEU
while True:
    screen.fill((50,200,110))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==SCREEN_UPDATE:
            main_game.update()
        if event.type== pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)
            if event.key==pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)