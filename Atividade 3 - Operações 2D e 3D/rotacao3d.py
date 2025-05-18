import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
# Kayo Xavier Nascimento Cavalcante Leite - 21.2.4095
# Inicialização do Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
pygame.display.set_mode((WIDTH, HEIGHT), pygame.OPENGL | pygame.DOUBLEBUF)
pygame.display.set_caption("Rotação 3D do Cubo")

def init_gl():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Fundo preto
    glEnable(GL_DEPTH_TEST)           # Habilita o teste de profundidade
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (WIDTH / HEIGHT), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -5)        # Afasta a cena para visualizar o cubo
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
        (0,1), (1,2), (2,3), (3,0),
        (4,5), (5,6), (6,7), (7,4),
        (0,4), (1,5), (2,6), (3,7)
    )
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    init_gl()
    clock = pygame.time.Clock()
    rotation_angle = 0
    frame_count = 0

    print("Iniciando rotação 3D do cubo...")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Atualiza o ângulo de rotação
        rotation_angle += 1

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5)
        # Rotaciona o cubo ao redor dos eixos x, y e z
        glRotatef(rotation_angle, 1, 1, 1)

        draw_cube()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    print("Programa finalizado.")

if __name__ == '__main__':
    main()
