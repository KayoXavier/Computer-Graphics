import pygame

# Kayo Xavier Nascimento Cavalcante Leite - 21.2.4095

# Inicialização do Pygame
pygame.init()

# Definições da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo da Bolinha")

# Definições da bolinha
ball_radius = 20
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
speed = 5

# Definições de cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Loop principal
runnig = True
clock = pygame.time.Clock()
while runnig:

    screen.fill(WHITE)  # Limpa a tela
    
    # Captura eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnig = False
    
    # Movimentação da bolinha
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ball_x -= speed
    if keys[pygame.K_RIGHT]:
        ball_x += speed
    if keys[pygame.K_UP]:
        ball_y -= speed
    if keys[pygame.K_DOWN]:
        ball_y += speed
    
    # Verifica colisões com as bordas
    if ball_x - ball_radius < 0 or ball_x + ball_radius > WIDTH:
        speed = -speed
    if ball_y - ball_radius < 0 or ball_y + ball_radius > HEIGHT:
        speed = -speed
    
    # Desenha a bolinha
    pygame.draw.circle(screen, BLACK, (ball_x, ball_y), ball_radius)
    
    pygame.display.flip()
    pygame.time.Clock().tick(60)  # Cap at 60 FPS

pygame.quit()
