import pygame, random
from pygame.locals import *

def caixas(caixax, caixay, caixaw, caixah):
    caixa = (caixax, caixay)
    caixa_skin = pygame.Surface((caixaw, caixah))
    caixa_skin.fill((255, 0, 0))
    screen.blit(caixa_skin, caixa)

def click(caixax, caixay, caixaw, caixah):
    mouse = pygame.mouse.get_pos()
    if caixax < mouse[0] < caixax + caixaw and caixay < mouse[1] < caixay + caixah:
        print("Clique dentro da caixa")
        status = STOP
        #Aumentar uma pontuação
        #Fazer a caixa sumir
        #Fazer o alvo reiniciar caixax = -60 ou caixax = 610
        #Aparecer um texto na tela.
        
    else:
        print("Clique fora da caixa")
        status = MOVE
    return caixax, status

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Alvos')

clock = pygame.time.Clock()

RIGHT = 1
LEFT = 0
MOVE = 1
STOP = 0

my_direction = RIGHT
status = MOVE
caixax = 0
caixay = random.randint(0, 550)
caixaw, caixah = 50, 50
caixas(caixax, caixay, caixaw, caixah)

while True:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == MOUSEBUTTONDOWN:
            caixax, status = click(caixax, caixay, caixaw, caixah)

    if my_direction == RIGHT and status == MOVE:
        caixax = caixax + 10
    if my_direction == LEFT and status == MOVE:
        caixax = caixax - 10

    if caixax < -80 or caixax > 620:
        my_direction = random.randint(0, 2)
        if my_direction == 0:
            my_direction = LEFT
            caixax = 610
        if my_direction == 1:
            my_direction = RIGHT
            caixax = -60
        caixay = random.randint(0, 550)


    screen.fill((0, 0, 0))

    caixas(caixax, caixay, caixaw, caixah)

    pygame.display.update()
