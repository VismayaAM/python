from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

angle = 0

def init():
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(-1, 1, -1, 1)

def draw_square():
    global angle
    glClear(GL_COLOR_BUFFER_BIT)

    glPushMatrix()
    glRotatef(angle, 0, 0, 1)
    glColor3f(1, 1, 1)
    glBegin(GL_QUADS)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.5, 0.5)
    glVertex2f(-0.5, 0.5)
    glEnd()
    glPopMatrix()

    glutSwapBuffers()

def animate_square(value):
    global angle
    angle += 2
    if angle > 360:
        angle -= 360
    glutPostRedisplay()
    glutTimerFunc(16, animate_square, 0)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow('Rotating Square')
    glutDisplayFunc(draw_square)
    glutTimerFunc(25, animate_square, 0)
    init()
    glutMainLoop()

main()
