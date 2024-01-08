from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Window dimensions
width, height = 800, 600

def boundary_fill(x, y, fillColor, borderColor):
    currentColor = glReadPixels(x, y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE)
    if currentColor != borderColor:
        glColor3fv(fillColor)
        glBegin(GL_POINTS)
        glVertex2i(x, y)
        glEnd()
        glFlush()
        boundary_fill(x + 1, y, fillColor, borderColor)
        boundary_fill(x - 1, y, fillColor, borderColor)
        boundary_fill(x, y + 1, fillColor, borderColor)
        boundary_fill(x, y - 1, fillColor, borderColor)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)  # Set color to white
    glPointSize(1.0)  # Set point size

    # Draw a square
    glColor3f(1.0, 0.0, 0.0)  # Set square color to red
    glBegin(GL_POLYGON)
    glVertex2i(100, 100)
    glVertex2i(200, 100)
    glVertex2i(200, 200)
    glVertex2i(100, 200)
    glEnd()

    boundary_fill(150, 150, (0.0, 0.0, 1.0), (1.0, 0.0, 0.0))  # Fill the square with blue

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutCreateWindow("Boundary Fill Algorithm for Square")

    glClearColor(0.0, 0.0, 0.0, 0.0)  # Set background color to black
    gluOrtho2D(0, width, 0, height)
    glutDisplayFunc(display)

    glutMainLoop()
main()
