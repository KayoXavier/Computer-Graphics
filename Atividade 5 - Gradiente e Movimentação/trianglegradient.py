import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
# Kayo Xavier Nascimento Cavalcante Leite - 21.2.4095
# Inicialização do Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
pygame.display.set_mode((WIDTH, HEIGHT), pygame.OPENGL | pygame.DOUBLEBUF)
pygame.display.set_caption("Triângulo Colorido com Gradiente")

def init_gl():
    # Define a cor de fundo
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Fundo branco
    # Define o viewport
    glViewport(0, 0, WIDTH, HEIGHT)
    # Configura a projeção para 2D com uma projeção ortográfica
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, WIDTH, 0, HEIGHT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    print("OpenGL inicializado com projeção ortográfica para 2D.")

def draw_gradient_triangle():
    glBegin(GL_TRIANGLES)
    # Vértice 1: Vermelho
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(WIDTH / 2, HEIGHT * 0.8)
    # Vértice 2: Verde
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(WIDTH * 0.2, HEIGHT * 0.2)
    # Vértice 3: Azul
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(WIDTH * 0.8, HEIGHT * 0.2)
    glEnd()

def main():
    init_gl()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        glClear(GL_COLOR_BUFFER_BIT)
        draw_gradient_triangle()
        pygame.display.flip()
   
    
    pygame.quit()
    print("Programa finalizado.")

if __name__ == '__main__':
    main()
