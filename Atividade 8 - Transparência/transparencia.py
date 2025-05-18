from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

# Cores e transparências (RGBA) iniciais
cube_color = [1.0, 0.0, 0.0, 0.5]    # Vermelho com 50% de opacidade
sphere_color = [0.0, 0.0, 1.0, 0.5]   # Azul com 50% de opacidade

def init():
    glClearColor(0.2, 0.2, 0.2, 1.0)  # Fundo cinza escuro
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_COLOR_MATERIAL)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    # Configura a câmera
    gluLookAt(0.0, 3.0, 10.0,  0.0, 0.0, 0.0,  0.0, 1.0, 0.0)
    
    # Desenha o cubo (à esquerda)
    glPushMatrix()
    glTranslatef(-2.0, 0.0, 0.0)
    glColor4fv(cube_color)
    glutSolidCube(3.0)
    glPopMatrix()
    
    # Desenha a esfera (à direita)
    glPushMatrix()
    glTranslatef(2.0, 0.0, 0.0)
    glColor4fv(sphere_color)
    glutSolidSphere(1.5, 50, 50)
    glPopMatrix()
    
    glutSwapBuffers()

def reshape(width, height):
    if height == 0:
        height = 1
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def keyboard(key, x, y):
    global cube_color, sphere_color
    key = key.decode('utf-8')
    if key == 'q':      # Diminui alpha do cubo (mais transparente)
        cube_color[3] = max(0.0, cube_color[3] - 0.1)
    elif key == 'a':    # Aumenta alpha do cubo (menos transparente)
        cube_color[3] = min(1.0, cube_color[3] + 0.1)
    elif key == 'w':    # Diminui alpha da esfera (mais transparente)
        sphere_color[3] = max(0.0, sphere_color[3] - 0.1)
    elif key == 's':    # Aumenta alpha da esfera (menos transparente)
        sphere_color[3] = min(1.0, sphere_color[3] + 0.1)
    elif key == 'r':    # Reseta para os valores iniciais
        cube_color[:] = [1.0, 0.0, 0.0, 0.5]
        sphere_color[:] = [0.0, 0.0, 1.0, 0.5]
    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Cena com Objetos Transparente")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

if __name__ == '__main__':
    main()
