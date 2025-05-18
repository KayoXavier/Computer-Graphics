import pygame
import sys

# Kayo Xavier Nascimento Cavalcante Leite - 21.2.4095

# Inicialização do Pygame
pygame.init()

# Definições da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo do quadrado")

# Definições de cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#Definições do quadrado
object_x, object_y = 400, 300  # Initial position
object_size = 50
speed = 5

# Main game loop
running = True
while running:

    # Limpa a tela
    screen.fill(WHITE)

    # Captura Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

     # Movimentação da bolinha
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        object_x -= speed
    if keys[pygame.K_RIGHT]:
        object_x += speed
    if keys[pygame.K_UP]:
        object_y -= speed
    if keys[pygame.K_DOWN]:
        object_y += speed

    # Verifica colisões com as bordas
    object_x = max(0, min(object_x, WIDTH - object_size))
    object_y = max(0, min(object_y, HEIGHT - object_size))

    # Desenha quadrado:
    pygame.draw.rect(screen, BLACK, (object_x, object_y, object_size, object_size))

    # Atualiza o display
    pygame.display.flip()
    pygame.time.Clock().tick(60)  # Cap at 60 FPS

pygame.quit()
sys.exit()