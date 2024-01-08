from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

def draw_house():
    # Draw black square for the front wall
    glColor3f(0,1,1)
    glBegin(GL_QUADS)
    glVertex2f(-150,-400)
    glVertex2f(150,-400)
    glVertex2f(-150,-100)
    glVertex2f(150, -100)
    glEnd()

    # Draw brown triangle for the roof
    glColor3f(0.5, 0.2, 0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-50, 100)
    glVertex2f(50, 100)
    glVertex2f(0, 150)
    glEnd()

    # Draw red rectangle for the chimney
    glColor3f(1, 0, 0)
    glBegin(GL_QUADS)
    glVertex2f(20, 120)
    glVertex2f(30, 120)
    glVertex2f(30, 150)
    glVertex2f(20, 150)
    glEnd()

    # Draw two circles above the chimney
    glColor3f(0, 0, 1)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(25, 170)  # Center of the circles
    radius = 10
    num_segments = 100
    for i in range(num_segments + 1):
        theta = i * (2.0 * 3.141592653589793 / num_segments)
        x = 25 + radius * math.cos(theta)
        y = 170 + radius * math.sin(theta)
        glVertex2f(x, y)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(25, 170)  # Center of the circles
    radius = 5
    for i in range(num_segments + 1):
        theta = i * (2.0 * 3.141592653589793 / num_segments)
        x = 25 + radius * math.cos(theta)
        y = 170 + radius * math.sin(theta)
        glVertex2f(x, y)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    draw_house()

    glutSwapBuffers()

def init():
    glClearColor(0,0,0,1)
    gluOrtho2D(-100, 100, 0, 200)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(800, 800)
    glutCreateWindow('House Drawing')

    glutDisplayFunc(display)
    init()
    glutMainLoop()

if __name__ == "__main__":
    main()
