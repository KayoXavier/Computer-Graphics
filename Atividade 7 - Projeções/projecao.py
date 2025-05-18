import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
# Kayo Xavier Nascimento Cavalcante Leite - 21.2.4095
# Variáveis globais de controle
isPerspective = 1  # 1 para perspectiva, 0 para ortogonal
scale = 1.0
growing = True

# Configurações da janela
WIDTH, HEIGHT = 800, 600

def setProjection(projection_type):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if projection_type == 1:
        # Projeção perspectiva: (ângulo de visão, aspecto, plano próximo, plano distante)
        gluPerspective(45.0, float(WIDTH) / float(HEIGHT), 0.1, 100.0)
        print("Projeção configurada: Perspectiva")
    else:
        # Projeção ortogonal: (left, right, bottom, top, near, far)
        glOrtho(-5, 5, -5, 5, -10, 10)
        print("Projeção configurada: Ortogonal")
    glMatrixMode(GL_MODELVIEW)

def init():
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Fundo preto
    setProjection(isPerspective)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    # Configuração da câmera: posição, alvo e vetor up
    gluLookAt(3.0, 3.0, 5.0,  # Posição da câmera
              0.0, 0.0, 0.0,  # Para onde a câmera olha
              0.0, 1.0, 0.0)  # Vetor "up"

    # Aplica a escala do cubo (animação)
    glPushMatrix()
    glScalef(scale, scale, scale)
    glColor3f(1.0, 1.0, 1.0)  # Cubo branco
    glutWireCube(2.0)        # Cubo wireframe com aresta 2.0
    glPopMatrix()

    glutSwapBuffers()

def keyboard(key, x, y):
    global isPerspective
    # key é do tipo bytes; convertemos para str para comparação
    key = key.decode('utf-8')
    if key.lower() == 'p':
        isPerspective = 1
        print("Tecla 'p' pressionada: Alternando para projeção perspectiva")
    elif key.lower() == 'o':
        isPerspective = 0
        print("Tecla 'o' pressionada: Alternando para projeção ortogonal")
    setProjection(isPerspective)
    glutPostRedisplay()

def timer(value):
    global scale, growing
    # Atualiza o fator de escala
    if growing:
        scale += 0.05
    else:
        scale -= 0.05

    if scale >= 2.0:
        growing = False
       
    if scale <= 0.5:
        growing = True
        

    glutPostRedisplay()
    glutTimerFunc(16, timer, 0)  # Aproximadamente 60 FPS

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutInitWindowPosition(100, 100)
    # A função glutCreateWindow espera um bytes string
    glutCreateWindow(b"Cubo Animado")
    
    init()
    
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutTimerFunc(0, timer, 0)
    glutMainLoop()

if __name__ == '__main__':
    main()
