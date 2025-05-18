import pygame
# Kayo Xavier Nascimento Cavalcante Leite - 21.2.4095
pygame.init()

# Configurações da tela: largura 256 (para representar de 0 a 255) e altura 100
WIDTH, HEIGHT = 256, 256
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gradiente RGB: R varia de 0 a 255")

# Valores constantes para G e B
G = 128
B = 128

running = True
clock = pygame.time.Clock()

print("Iniciando gradiente RGB...")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Para cada coluna, desenha uma linha com a cor correspondente
    for x in range(WIDTH):
        R = x  # R varia de 0 a 255 conforme a posição x
        color = (R, G, B)
        pygame.draw.line(screen, color, (x, 0), (x, HEIGHT))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
print("Programa de gradiente RGB finalizado.")
