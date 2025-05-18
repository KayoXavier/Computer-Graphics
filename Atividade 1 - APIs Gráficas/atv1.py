from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Kayo Xavier Nascimento Cavalcante Leite - 21.2.4095

def init():
    # Configura a cor de fundo (Branco)
    glClearColor(1.0, 1.0, 1.0, 1.0)

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    # Define a cor do quadrado (Preto)
    glColor3f(0.0, 0.0, 0.0)
    
    # Desenha o quadrado centralizado
    glBegin(GL_QUADS)
    glVertex2f(-0.5, -0.5)  # Canto inferior esquerdo
    glVertex2f( 0.5, -0.5)  # Canto inferior direito
    glVertex2f( 0.5,  0.5)  # Canto superior direito
    glVertex2f(-0.5,  0.5)  # Canto superior esquerdo
    glEnd()

    glutSwapBuffers()

def reshape(width, height):
    # Define a viewport para cobrir toda a janela
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    
    # Preserva a razão de aspecto ajustando os limites da projeção ortográfica
    if width <= height:
        aspect = float(height) / float(width)
        # Se a largura é o fator limitante, ajusta os limites verticais
        gluOrtho2D(-1.0, 1.0, -1.0 * aspect, 1.0 * aspect)
    else:
        aspect = float(width) / float(height)
        # Se a altura é o fator limitante, ajusta os limites horizontais
        gluOrtho2D(-1.0 * aspect, 1.0 * aspect, -1.0, 1.0)
    
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(400, 400) #define o tamanho inicial da janela
    glutCreateWindow(b"Quadrado Centralizado com Proporcoes Fixas") #cria a janela (a string representa o titulo da aba ao ser aberta)
    init()
    glutDisplayFunc(draw) #desenha o quadrado atraves da função draw 
    glutReshapeFunc(reshape) # atualiza o tamanho do quadrado de acordo com as proporções da janela
    glutMainLoop()

if __name__ == '__main__':
    main()
