from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
from PIL import Image
# Kayo Xavier Nascimento Cavalcante Leite - 21.2.4095
# Variáveis globais
texture = None
angle = 0.0
tex_offset_x = 0.0  # Offset na coordenada s (x)
tex_offset_y = 0.0  # Offset na coordenada t (y)
tex_scale = 1.0     # Fator de escala aplicado às coordenadas de textura

def load_texture():
    global texture
    try:
        image = Image.open("texture.bmp")#atualizar caminho da textura para rodar em computador diferente
    except IOError:
        print("Erro ao abrir 'texture.bmp'. Verifique se o arquivo existe!")
        sys.exit(1)
    # Inverte a imagem verticalmente para adequar ao padrão do OpenGL
    image = image.transpose(Image.FLIP_TOP_BOTTOM)
    img_data = image.convert("RGB").tobytes()
    width, height = image.size

    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0,
                 GL_RGB, GL_UNSIGNED_BYTE, img_data)

def draw_textured_cube():
    glBindTexture(GL_TEXTURE_2D, texture)
    glBegin(GL_QUADS)
    # Face frontal
    glTexCoord2f((0.0 + tex_offset_x) * tex_scale, (0.0 + tex_offset_y) * tex_scale); glVertex3f(-1.0, -1.0,  1.0)
    glTexCoord2f((1.0 + tex_offset_x) * tex_scale, (0.0 + tex_offset_y) * tex_scale); glVertex3f( 1.0, -1.0,  1.0)
    glTexCoord2f((1.0 + tex_offset_x) * tex_scale, (1.0 + tex_offset_y) * tex_scale); glVertex3f( 1.0,  1.0,  1.0)
    glTexCoord2f((0.0 + tex_offset_x) * tex_scale, (1.0 + tex_offset_y) * tex_scale); glVertex3f(-1.0,  1.0,  1.0)

    # Face traseira
    glTexCoord2f((0.0 + tex_offset_x) * tex_scale, (0.0 + tex_offset_y) * tex_scale); glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f((1.0 + tex_offset_x) * tex_scale, (0.0 + tex_offset_y) * tex_scale); glVertex3f( 1.0, -1.0, -1.0)
    glTexCoord2f((1.0 + tex_offset_x) * tex_scale, (1.0 + tex_offset_y) * tex_scale); glVertex3f( 1.0,  1.0, -1.0)
    glTexCoord2f((0.0 + tex_offset_x) * tex_scale, (1.0 + tex_offset_y) * tex_scale); glVertex3f(-1.0,  1.0, -1.0)

    # Face esquerda
    glTexCoord2f((0.0 + tex_offset_x) * tex_scale, (0.0 + tex_offset_y) * tex_scale); glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f((1.0 + tex_offset_x) * tex_scale, (0.0 + tex_offset_y) * tex_scale); glVertex3f(-1.0, -1.0,  1.0)
    glTexCoord2f((1.0 + tex_offset_x) * tex_scale, (1.0 + tex_offset_y) * tex_scale); glVertex3f(-1.0,  1.0,  1.0)
    glTexCoord2f((0.0 + tex_offset_x) * tex_scale, (1.0 + tex_offset_y) * tex_scale); glVertex3f(-1.0,  1.0, -1.0)

    # Face direita
    glTexCoord2f((0.0 + tex_offset_x) * tex_scale, (0.0 + tex_offset_y) * tex_scale); glVertex3f(1.0, -1.0, -1.0)
    glTexCoord2f((1.0 + tex_offset_x) * tex_scale, (0.0 + tex_offset_y) * tex_scale); glVertex3f(1.0, -1.0,  1.0)
    glTexCoord2f((1.0 + tex_offset_x) * tex_scale, (1.0 + tex_offset_y) * tex_scale); glVertex3f(1.0,  1.0,  1.0)
    glTexCoord2f((0.0 + tex_offset_x) * tex_scale, (1.0 + tex_offset_y) * tex_scale); glVertex3f(1.0,  1.0, -1.0)

    # Face superior
    glTexCoord2f((0.0 + tex_offset_x) * tex_scale, (0.0 + tex_offset_y) * tex_scale); glVertex3f(-1.0,  1.0, -1.0)
    glTexCoord2f((1.0 + tex_offset_x) * tex_scale, (0.0 + tex_offset_y) * tex_scale); glVertex3f( 1.0,  1.0, -1.0)
    glTexCoord2f((1.0 + tex_offset_x) * tex_scale, (1.0 + tex_offset_y) * tex_scale); glVertex3f( 1.0,  1.0,  1.0)
    glTexCoord2f((0.0 + tex_offset_x) * tex_scale, (1.0 + tex_offset_y) * tex_scale); glVertex3f(-1.0,  1.0,  1.0)

    # Face inferior
    glTexCoord2f((0.0 + tex_offset_x) * tex_scale, (0.0 + tex_offset_y) * tex_scale); glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f((1.0 + tex_offset_x) * tex_scale, (0.0 + tex_offset_y) * tex_scale); glVertex3f( 1.0, -1.0, -1.0)
    glTexCoord2f((1.0 + tex_offset_x) * tex_scale, (1.0 + tex_offset_y) * tex_scale); glVertex3f( 1.0, -1.0,  1.0)
    glTexCoord2f((0.0 + tex_offset_x) * tex_scale, (1.0 + tex_offset_y) * tex_scale); glVertex3f(-1.0, -1.0,  1.0)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    # Configura a câmera
    gluLookAt(3.0, 3.0, 7.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    
    # Aplica uma rotação para visualização dinâmica
    glRotatef(angle, 1.0, 1.0, 0.0)
    draw_textured_cube()
    glutSwapBuffers()

def timer(value):
    global angle
    angle += 2.0
    if angle > 360.0:
        angle -= 360.0
    glutPostRedisplay()
    glutTimerFunc(16, timer, 0)

def keyboard(key, x, y):
    global tex_offset_x, tex_offset_y, tex_scale
    key = key.decode('utf-8')
    if key == 'q':      # Aumenta offset em x
        tex_offset_x += 0.1
    elif key == 'a':    # Diminui offset em x
        tex_offset_x -= 0.1
    elif key == 'w':    # Aumenta offset em y
        tex_offset_y += 0.1
    elif key == 's':    # Diminui offset em y
        tex_offset_y -= 0.1
       

def reshape(width, height):
    if height == 0:
        height = 1
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(width) / float(height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def init():
    glClearColor(0.2, 0.2, 0.2, 1.0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_TEXTURE_2D)
    load_texture()
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, 800/600.0, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def main():
    global tex_offset_x, tex_offset_y, tex_scale
    tex_offset_x = 0.0
    tex_offset_y = 0.0
    tex_scale = 1.0
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Cubo Texturizado e Interativo")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutTimerFunc(0, timer, 0)
    glutMainLoop()

if __name__ == '__main__':
    main()
