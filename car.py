from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import sys

r1x1, r1x2, r1y1, r1y2 = -10, 5, 0, 5
r2x1, r2x2, r2x3, r2x4, r2y1, r2y2 = -8, 3, 1, -6, 5, 8
x1 = 1
y1 = 0
r1 = 2
x2 = -6
y2 = 0
r2 = 2
fill_color = [0, 0, 1]  # Fill color for flood fill

def init():
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(-50, 50, -50, 50)

def rectangle1():
    global r1x1, r1x2, r1y1, r1y2
    glColor3f(1, 0, 0)
    glPointSize(2)
    glBegin(GL_POLYGON)
    glVertex2f(r1x1, r1y1)
    glVertex2f(r1x2, r1y1)
    glVertex2f(r1x2, r1y2)
    glVertex2f(r1x1, r1y2)
    glEnd()
    r1x1 -= 1
    r1x2 -= 1

def rectangle2():
    global r2x1, r2x2, r2x3, r2x4, r2y1, r2y2
    glColor3f(1, 0, 0)
    glPointSize(2)
    glBegin(GL_POLYGON)
    glVertex2f(r2x1, r2y1)
    glVertex2f(r2x2, r2y1)
    glVertex2f(r2x3, r2y2)
    glVertex2f(r2x4, r2y2)
    glEnd()
    r2x1 -= 1
    r2x2 -= 1
    r2x3 -= 1
    r2x4 -= 1

def green():
    glColor3f(0, 1, 0)
    x4 = -28
    y4 = 32
    r4 = 3
    glBegin(GL_LINE_LOOP)
    for i in range(1, 361):
        angle = math.pi * 2 * i / 360
        x = r4 * math.cos(angle)
        y = r4 * math.sin(angle)
        glVertex2f(x4 + x, y4 + y)
    glEnd()

def red():
    glColor3f(1, 0, 0)
    x3 = -28
    y3 = 42
    r3 = 3
    glBegin(GL_LINE_LOOP)
    for i in range(1, 361):
        angle = math.pi * 2 * i / 360
        x = r3 * math.cos(angle)
        y = r3 * math.sin(angle)
        glVertex2f(x3 + x, y3 + y)
    glEnd()

def post():
    glColor3f(10, 75, 20)
    glPointSize(2)
    glBegin(GL_POLYGON)
    glVertex2f(-29, 9)
    glVertex2f(-28, 9)
    glVertex2f(-28, 25)
    glVertex2f(-29, 25)
    glEnd()

def signal():
    glColor3f(1, 1, 1)
    glPointSize(2)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-35, 25)
    glVertex2f(-22, 25)
    glVertex2f(-22, 48)
    glVertex2f(-35, 48)
    glEnd()

def tier1():
    glColor3f(25, 50, 75)
    global x2, y2, r2
    glBegin(GL_TRIANGLE_FAN)
    for i in range(1, 361):
        angle = math.pi * 2 * i / 360
        x = r2 * math.cos(angle)
        y = r2 * math.sin(angle)
        glVertex2f(x2 + x, y2 + y)
    glEnd()
    x2 -= 1

def tier2():
    glColor3f(1, 1, 1)
    global x1, y1, r1
    glBegin(GL_TRIANGLE_FAN)
    for i in range(1, 361):
        angle = math.pi * 2 * i / 360
        x = r1 * math.cos(angle)
        y = r1 * math.sin(angle)
        glVertex2f(x1 + x, y1 + y)
    glEnd()
    x1 -= 1

def flood_fill(x, y):
    glReadBuffer(GL_FRONT)
    pixels = glReadPixels(x, 500 - y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE)
    color_under_cursor = list(map(lambda x: x / 255.0, pixels[0][0]))

    if color_under_cursor == [1, 0, 0]:
        glReadBuffer(GL_BACK)
        glDrawBuffer(GL_BACK)
        glReadPixels(0, 0, 500,500, GL_RGB, GL_UNSIGNED_BYTE)
        glDrawBuffer(GL_FRONT)
        glReadBuffer(GL_FRONT)
        flood_fill_recursive(x, y)

def flood_fill_recursive(x, y):
    pixels = glReadPixels(x, 500 - y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE)
    current_color = list(map(lambda x: x / 255.0, pixels[0][0]))

    if current_color != fill_color and current_color == [1, 0, 0]:
        glColor3f(*fill_color)
        glBegin(GL_POINTS)
        glVertex2f(x, 500 - y)
        glEnd()
        glFlush()

        flood_fill_recursive(x + 1, y)
        flood_fill_recursive(x - 1, y)
        flood_fill_recursive(x, y + 1)
        flood_fill_recursive(x, y - 1)

def mouse_callback(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        flood_fill(x, y)


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    rectangle1()
    rectangle2()
    tier1()
    tier2()
    post()
    signal()
    green()
    red()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow('car animation')
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutMouseFunc(mouse_callback)
    init()
    glutMainLoop()

main()
