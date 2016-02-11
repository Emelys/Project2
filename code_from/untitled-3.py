import sys, pygame
from pygame.locals import * 

pygame.init()

size = width, height = 500, 500
black = 0, 0, 0

screen = pygame.display.set_mode((width, height + 50))


ball = pygame.image.load("tex2.png").convert()
window = pygame.image.load("tex1.png").convert()
hero = pygame.image.load("hero.png").convert()
bush = pygame.image.load("tex3.png").convert()
bush2 = pygame.image.load("tex4.png").convert()
finish = pygame.image.load("tex5.png").convert()
hero.set_colorkey((0,0,0))
#hero = pygame.transform.rotate(hero, 50)
#ball = pygame.transform.rotate(ball, 50)
#window = pygame.transform.rotate(window, 50)
x, y = 0, 0
texture_size = 50
matrix = [[0, 0, 2, 0, 0, 0, 0, 0, 0, 3],
          [1, 0, 1, 0, 1, 0, 2, 2, 0, 3],
          [1, 0, 0, 0, 0, 0, 2, 2, 0, 3],
          [0, 1, 1, 0, 1, 0, 0, 0, 0, 3],
          [0, 0, 0, 0, 1, 1, 1, 1, 0, 3],
          [0, 0, 0, 0, 0, 0, 0, 1, 0, 3],
          [0, 0, 0, 0, 0, 1, 1, 1, 0, 3],
          [0, 2, 0, 2, 0, 0, 0, 0, 0, 3],
          [0, 3, 0, 2, 2, 2, 0, 0, 0, 3],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 3]]



def create_field(texture_size):
    screen.fill(black)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 0:
                screen.blit(ball, (i * texture_size, j * texture_size))
            elif matrix[i][j] == 1:
                screen.blit(window, (i * texture_size, j * texture_size))
            elif matrix[i][j] == 2:
                screen.blit(bush, (i * texture_size, j * texture_size))
            elif matrix[i][j] == 3:
                screen.blit(bush2, (i * texture_size, j * texture_size)) 
            elif matrix[i][j] == 4:
                screen.blit(finish, (i * texture_size, j * texture_size))             
    

def moving(x1, y1, texture_size):
    for event in pygame.event.get():
        #print(matrix[x1 // texture_size][(y1 - texture_size) // texture_size], 
              #matrix[x1 // texture_size][(y1 + texture_size) // texture_size],
              #matrix[(x1 + texture_size) // texture_size][y1 // texture_size],
              #matrix[(x1 - texture_size) // texture_size][y1 // texture_size])
        print(x1 + texture_size,  (x1 + texture_size) < width)
        if event.type == KEYDOWN:
            if event.key == K_UP and matrix[x1 // texture_size][(y1 - texture_size) // texture_size] == 0:
                y1 -= texture_size
            if event.key == K_DOWN and matrix[x1 // texture_size][(y1 + texture_size) // texture_size] == 0 :
                y1 += texture_size
            if event.key == K_RIGHT and matrix[(x1 + texture_size) // texture_size][y1 // texture_size] == 0 and (x1 + texture_size) < width:
                x1 += texture_size
            if event.key == K_LEFT and matrix[(x1 - texture_size) // texture_size][y1 // texture_size] == 0:
                x1 -= texture_size        
    return x1, y1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit() 
    
    create_field(50)
    x, y = moving(x, y, 50)
    screen.blit(hero, moving(x, y, 50))
    pygame.display.flip()
    