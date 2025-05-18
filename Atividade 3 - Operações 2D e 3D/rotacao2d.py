import pygame
import math
# Kayo Xavier Nascimento Cavalcante Leite - 21.2.4095
# Inicialização do Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Transformação 2D - Rotação")

# Definições do quadrado
square_size = 100
square_color = (255, 255, 255)
square_center = (WIDTH // 2, HEIGHT // 2)
angle = 0

# Loop principal
going = True
clock = pygame.time.Clock()
while going:
    screen.fill((0, 0, 0))  # Limpa a tela
    
    # Captura eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            going = False
    
    # Atualiza o ângulo de rotação
    angle += 2
    
    # Criação do quadrado rotacionado
    square_surface = pygame.Surface((square_size, square_size), pygame.SRCALPHA)
    pygame.draw.rect(square_surface, square_color, (0, 0, square_size, square_size))
    rotated_square = pygame.transform.rotate(square_surface, angle)
    
    # Ajusta a posição para manter o centro
    rect = rotated_square.get_rect(center=square_center)
    
    # Desenha na tela
    screen.blit(rotated_square, rect.topleft)
    
    pygame.display.flip()
    clock.tick(75)  # 30 FPS

pygame.quit()
