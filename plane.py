
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

rx1=100
rx2=280
ry1=275
ry2=325

t1x1=150
t1x2=320
t1x3=340
t1y1=275
t1y2=350

t2x1=150
t2x2=220
t2x3=300
t2y1=325
t2y2=380

sx1=150
sx2=200
sy1=285
sy2=320

x1=100
y1=300

x2=0
y2=280
 
r=28

l1x1=0
l1y1=280
l1x2=0
l1y2=180

l2x1=-50
l2y1=200
l2x2=50
l2y2=200

count=100

def init():
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(-400, 400, -400, 400)
def head():
    global x2,y2
    glColor3f(0,0,1) 
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x2,y2)  
    for i in range(360+1):
        theta = i * (2*math.pi / 360)
        x = x2 + r * math.cos(theta)
        y = y2+ r * math.sin(theta)
        glVertex2f(x, y)
    y2-=.5
    glEnd()
def line1():
    global l1x1,l1x2,l1y1,l1y2
    glColor3f(0,0,1)
    glBegin(GL_LINES)
    glVertex2f(l1x1,l1y1)
    glVertex2f(l1x2,l1y2)
    l1y1-=.5
    l1y2-=.5
    glEnd()

def line2():
    global l2x1,l2x2,l2y1,l2y2
    glColor3f(0,0,1)
    glBegin(GL_LINES)
    glVertex2f(l2x1,l2y1)
    glVertex2f(l2x2,l2y2)
    l2y1-=.5
    l2y2-=.5
    glEnd()
    
def square():
    global sx1,sx2,sy1,sy2
    glColor3f(.5,.5,.5)
    glBegin(GL_QUADS)
    glVertex2f(sx1,sy1)
    glVertex2f(sx2,sy1)
    glVertex2f(sx2, sy2)
    glVertex2f(sx1, sy2)
    sx1-=.5
    sx2-=.5
    glEnd()

def rectangle():
    global rx1,rx2,ry1,ry2
    glColor3f(1,1,1)
    glBegin(GL_QUADS)
    glVertex2f(rx1,ry1)
    glVertex2f(rx2,ry1)
    glVertex2f(rx2,ry2)
    glVertex2f(rx1,ry2)
    rx1-=.5
    rx2-=.5
    glEnd()

def triangle1():
    global t1x1,t1x2,t1x3,t1y1,t1y2
    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    glVertex2f(t1x1,t1y1)
    glVertex2f(t1x2,t1y1)
    glVertex2f(t1x3,t1y2)
    t1x1-=.5
    t1x2-=.5
    t1x3-=.5
    glEnd()
def triangle2():
    global t2x1,t2x2,t2x3,t2y1,t2y2
    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    glVertex2f(t2x1,t2y1)
    glVertex2f(t2x2,t2y1)
    glVertex2f(t2x3,t2y2)
    t2x1-=.5
    t2x2-=.5
    t2x3-=.5
    glEnd()

def circle():
    global x1,y1
    global r
    global count
    global steps
    glColor3f(1,1,1) 
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x1,y1)  
    for i in range(360+1):
        theta = i * (2*math.pi / 360)
        x = x1 + r * math.cos(theta)
        y = y1+ r * math.sin(theta)
        glVertex2f(x, y)
    x1-=.5
    count-=1
    glEnd()

def draw():
    global count
    glClear(GL_COLOR_BUFFER_BIT)
    rectangle()
    triangle1()
    triangle2()
    square()
    #chimney()
    circle()
    if count<=0:
        head()
        line1()
        line2()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    glutInitWindowPosition(0, 0)
    glutInitWindowSize(800, 800)
    glutCreateWindow('polygon')
    glutDisplayFunc(draw)
    init()
    glutIdleFunc(draw)  
    glutMainLoop()

if __name__ == "__main__":
    main()