from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import sys

# Global variables for rectangles, car, and signal
r1x1, r1x2, r1y1, r1y2 = -10, 5, 0, 5
r2x1, r2x2, r2x3, r2x4, r2y1, r2y2 = -8, 3, 1, -6, 5, 8
x1, y1, r1 = 1, 0, 2
x2, y2, r2 = -6, 0, 2
pointsize = 3  # Fill color for flood fill
signal_color = [1, 0, 0]  # Initial color of the signal (red)
car_moving = False  # Variable to control car movement

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
    glColor3f(*signal_color)
    x4, y4, r4 = -28, 32, 3
    glBegin(GL_LINE_LOOP)
    for i in range(1, 361):
        angle = math.pi * 2 * i / 360
        x = r4 * math.cos(angle)
        y = r4 * math.sin(angle)
        glVertex2f(x4 + x, y4 + y)
    glEnd()

def red():
    glColor3f(*signal_color)
    x3, y3, r3 = -28, 42, 3
    glBegin(GL_TRIANGLE_FAN)
    for i in range(1, 361):
        angle = math.pi * 2 * i / 360
        x = r3 * math.cos(angle)
        y = r3 * math.sin(angle)
        glVertex2f(x3 + x, y3 + y)
    glEnd()

def post():
    glColor3f(10 / 255, 75 / 255, 20 / 255)  # RGB: (10, 75, 20) normalized
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
    glColor3f(25 / 255, 50 / 255, 75 / 255)  # RGB: (25, 50, 75) normalized
    global x2, y2, r2
    glBegin(GL_TRIANGLE_FAN)
    for i in range(1, 361):
        angle = math.pi * 2 * i / 360
        x = r2 * math.cos(angle)
        y = r2 * math.sin(angle)
        glVertex2f(x2 + x, y2 + y)
    glEnd()
    if car_moving:
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
    if car_moving:
        x1 -= 1

def get_pixel(x, y):
    pixel = glReadPixels(x, y, 1, 1, GL_RGB, GL_FLOAT, None)
    return pixel[0][0]

def set_pixel(x, y, color):
    glColor3f(*color)
    glPointSize(3)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()

def floodfill(x, y, newcolor, oldcolor):
    color = get_pixel(x, y)
    if all(color == oldcolor):
        set_pixel(x, y, newcolor)
        floodfill(x + pointsize, y, newcolor, oldcolor)
        floodfill(x, y + pointsize, newcolor, oldcolor)
        floodfill(x - pointsize, y, newcolor, oldcolor)
        floodfill(x, y - pointsize, newcolor, oldcolor)

def mouseclick(button, state, x, y):
    global signal_color, car_moving
    y = 500 - y
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if signal_color == [1, 0, 0]:  # If signal is red, make it green and start car
            signal_color = [0, 1, 0]
            car_moving = True
        else:  # If signal is green, make it red and stop car
            signal_color = [1, 0, 0]
            car_moving = False
        floodfill(x, y, [0, 1, 0], [1, 0, 0])


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
    glutMouseFunc(mouseclick)
    init()
    glutMainLoop()

main()
