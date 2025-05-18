import pygame
import math
# Kayo Xavier Nascimento Cavalcante Leite - 21.2.4095
# Inicialização do Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Composição 2D: Rotação + Escala")

# Definições do quadrado
initial_square_size = 100
square_color =(255, 255, 255)
square_center = (WIDTH // 2, HEIGHT // 2)
angle = 0
scale = 1.0
scale_direction = 1  # 1 para aumentar, -1 para diminuir

# Loop principal
running = True
clock = pygame.time.Clock()
frame_count = 0

while running:
    screen.fill((0, 0, 0))
    
    # Captura eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Atualiza o ângulo de rotação e o fator de escala
    angle += 2
    scale += 0.01 * scale_direction
    if scale >= 2.0:
        scale_direction = -1
    elif scale <= 0.5:
        scale_direction = 1

    # Calcula o novo tamanho do quadrado baseado na escala
    square_size = int(initial_square_size * scale)
    
    # Criação do quadrado com a escala aplicada
    square_surface = pygame.Surface((square_size, square_size), pygame.SRCALPHA)
    pygame.draw.rect(square_surface, square_color, (0, 0, square_size, square_size))
    
    # Aplica a rotação ao quadrado escalado
    rotated_square = pygame.transform.rotate(square_surface, angle)
    rect = rotated_square.get_rect(center=square_center)
    
    # Desenha na tela
    screen.blit(rotated_square, rect.topleft)
    
    pygame.display.flip()
    clock.tick(75)

pygame.quit()
