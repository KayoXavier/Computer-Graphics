import sys
import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
# Kayo Xavier Nascimento Cavalcante Leite - 21.2.4095
# Variáveis globais para os ângulos de órbita
earth_angle = 0.0
moon_angle = 0.0

# Configurações da janela
WIDTH, HEIGHT = 800, 600

def init():
    """Inicializa o OpenGL e configura a perspectiva."""
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Fundo preto
    glEnable(GL_DEPTH_TEST)           # Habilita o teste de profundidade
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(WIDTH) / float(HEIGHT), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    print("OpenGL inicializado e perspectiva definida.")

def display():
    """Callback de exibição para desenhar o sistema solar."""
    global earth_angle, moon_angle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    # Configuração da câmera: posição do observador, alvo e vetor up
    gluLookAt(0.0, 5.0, 20.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    
    # Desenha o Sol (fixo no centro)
    glPushMatrix()
    glColor3f(1.0, 1.0, 0.0)  # Amarelo
    glutSolidSphere(1.0, 50, 50)
    glPopMatrix()
    
    # Desenha a Terra orbitando o Sol
    glPushMatrix()
    glRotatef(earth_angle, 0.0, 1.0, 0.0)  # Rotaciona para posicionar a Terra na órbita
    glTranslatef(8.0, 0.0, 0.0)              # Raio da órbita da Terra
    glColor3f(0.0, 0.0, 1.0)                 # Azul para a Terra
    glutSolidSphere(0.5, 50, 50)
    
    # Desenha a Lua orbitando a Terra
    glPushMatrix()
    glRotatef(moon_angle, 0.0, 1.0, 0.0)      # Rotaciona para posicionar a Lua na órbita da Terra
    glTranslatef(1.5, 0.0, 0.0)              # Raio da órbita da Lua
    glColor3f(0.5, 0.5, 0.5)                 # Cinza para a Lua
    glutSolidSphere(0.2, 50, 50)
    glPopMatrix()  # Fim da Lua
    
    glPopMatrix()  # Fim da Terra
    
    glutSwapBuffers()

def timer(value):
    """Callback de temporizador para atualizar os ângulos das órbitas."""
    global earth_angle, moon_angle
    earth_angle += 0.5    # Incrementa a órbita da Terra
    if earth_angle > 360:
        earth_angle -= 360

    moon_angle += 2.0     # Incrementa a órbita da Lua
    if moon_angle > 360:
        moon_angle -= 360
    
    glutPostRedisplay()  # Solicita a atualização da tela
    glutTimerFunc(16, timer, 0)  # Chama novamente o timer após 16ms (~60 FPS)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Sistema Solar Simples")
    init()
    glutDisplayFunc(display)
    glutTimerFunc(0, timer, 0)
    glutMainLoop()

if __name__ == '__main__':
    main()
