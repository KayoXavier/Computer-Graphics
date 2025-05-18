import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
# Kayo Xavier Nascimento Cavalcante Leite - 21.2.4095
# Inicialização do Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
pygame.display.set_mode((WIDTH, HEIGHT), pygame.OPENGL | pygame.DOUBLEBUF)
pygame.display.set_caption("Composição 3D: Rotação + Translação do Cubo")

def init_gl():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Fundo preto
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (WIDTH / HEIGHT), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    print("OpenGL inicializado e perspectiva definida.")

def draw_cube():
    # Define os vértices do cubo
    vertices = [
        [1, 1, -1],
        [1, -1, -1],
        [-1, -1, -1],
        [-1, 1, -1],
        [1, 1, 1],
        [1, -1, 1],
        [-1, -1, 1],
        [-1, 1, 1]
    ]
    # Define as arestas que conectam os vértices
    edges = (
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
    )
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    init_gl()
    clock = pygame.time.Clock()
    rotation_angle = 0.0
    translation = 0.0
    translation_direction = 1
    frame_count = 0

    print("Iniciando composição 3D: Rotação + Translação do Cubo...")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Atualiza os valores de rotação e translação
        rotation_angle += 1.0  # Incrementa o ângulo de rotação
        translation += translation_direction * 0.02  # Atualiza a translação

        # Inverte a direção da translação ao atingir os limites
        if translation > 2.0 or translation < -2.0:
            translation_direction *= -1

        # Renderização
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        # Composição: primeiro translada, depois rotaciona
        glTranslatef(translation, 0.0, -5.0)
        glRotatef(rotation_angle, 1, 1, 1)

        draw_cube()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    print("Programa finalizado.")

if __name__ == '__main__':
    main()
