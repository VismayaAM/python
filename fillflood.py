from OpenGL.GL import *
from OpenGL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
sys.setrecursionlimit(10000)
windowsize=700
pointsize=3
def init():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(0,windowsize,0,windowsize)
def display():
    triangle()
def getpixel(x,y):
    pixel=glReadPixels(x,y,1,1,GL_RGB,GL_FLOAT,None)
    return pixel[0][0]
def setpixel(x,y,fillcolor):
    glColor3f(*fillcolor)
    glPointSize(pointsize)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()
    glFlush()
def triangle():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.2,0.5,0.7)
    glBegin(GL_POLYGON)
    glVertex2f(100,100)
    glVertex2f(400,100)
    glVertex2f(400,500)
    glEnd()
    glFlush()
def floodfill(x,y,fillcolor,oldcolor):
    color=getpixel(x,y)
    if all(color==oldcolor):
        setpixel(x,y,fillcolor)
        floodfill(x+pointsize,y,fillcolor,oldcolor)
        floodfill(x,y+pointsize,fillcolor,oldcolor)
        floodfill(x-pointsize,y,fillcolor,oldcolor)
        floodfill(x,y-pointsize,fillcolor,oldcolor)
def mouse_click(button,state,x,y):
    y=windowsize-y
    if button==GLUT_LEFT_BUTTON and state==GLUT_DOWN:
        floodfill(x,y,[0,1,1],getpixel(x,y))
def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowPosition(0,0)
    glutInitWindowSize(700,700)
    glutCreateWindow("Sample")
    glutDisplayFunc(lambda:display())
    glutMouseFunc(mouse_click)
    init()
    glutMainLoop()

main()