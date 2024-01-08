from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL import *
import sys

sys.setrecursionlimit(10**6)
pointsize=3
windowsize=500

def init():
    glClearColor(0,0,0,1)
    gluOrtho2D(0,500,0,500)


def rectangle():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0,0,1)
    #glPointSize(2)
    glBegin(GL_QUADS)
    glVertex2f(100,100)
    glVertex2f(300,100)
    glVertex2f(300,300)
    glVertex2f(100,300)
    glEnd()
    glFlush()

def get_pixel(x,y):
    pixel=glReadPixels(x,y,1,1,GL_RGB,GL_FLOAT,None)
    return pixel[0][0]

def set_pixel(x,y,color):
    glColor3f(*color)
    glPointSize(pointsize)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()
    glFlush()

def floodfill(x,y,newcolor,oldcolor):
    color=get_pixel(x,y)
    if all(color==oldcolor):
        set_pixel(x,y,newcolor)
        floodfill(x+pointsize,y,newcolor,oldcolor)
        floodfill(x,y+pointsize,newcolor,oldcolor)
        floodfill(x-pointsize,y,newcolor,oldcolor)
        floodfill(x,y-pointsize,newcolor,oldcolor)

def mouse_click(button,state,x,y):
    if button==GLUT_LEFT_BUTTON and state==GLUT_DOWN:
        floodfill(x,y,[0,1,0],get_pixel(x,y))

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(windowsize,windowsize)
    glutInitWindowPosition(0,0)
    glutCreateWindow('filling')
    glutDisplayFunc(lambda:rectangle())
    glutMouseFunc(mouse_click)
    init()
    glutMainLoop()

main()