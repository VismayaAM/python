from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

cloud_y = 65  # Initial y-coordinate of the cloud center
r=20
cnt=0
steps=cloud_y
def init():
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(-400, 400, -400, 400)

def square():
    glColor3f(1, 0, 0)
    glBegin(GL_QUADS)
    glVertex2f(-150, -100)
    glVertex2f(150, -100)
    glVertex2f(150, -400)
    glVertex2f(-150, -400)
    glEnd()

def rectangle():
    glColor3f(.5,.35,.05)
    glBegin(GL_QUADS)
    glVertex2f(-50, -200)
    glVertex2f(50, -200)
    glVertex2f(50, -400)
    glVertex2f(-50, -400)
    glEnd()

def triangle():
    glColor3f(0, 0, 1)
    glBegin(GL_POLYGON)
    glVertex2f(-150, -100)
    glVertex2f(10, 1)
    glVertex2f(150, -100)
    glEnd()

def chimney():
    glColor3f(150, 75, 0)
    glBegin(GL_POLYGON)
    glVertex2f(75, 40)
    glVertex2f(150, 40)
    glVertex2f(150, -100)
    glVertex2f(75, -47)
    glEnd()

def cloud():
    global cloud_y
    global r
    global cnt
    global steps
    glColor3f(.5,.5,.5)  # White color
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(100, cloud_y)  # Center of the first circle
    for i in range(360+1):
        theta = i * (2*math.pi / 360)
        x = 100 + r * math.cos(theta)
        y = cloud_y + r * math.sin(theta)
        glVertex2f(x, y)
    glEnd()

    glColor3f(.5,.5,.5)  # White color
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(133, cloud_y)  # Center of the second circle (shifted to the right)
    for i in range(360+1):
        theta = i * (2*math.pi / 360)
        x = 133 + r * math.cos(theta)
        y = cloud_y + r * math.sin(theta)
        glVertex2f(x, y)
    glEnd()
   
    # Update cloud's vertical position for animation
    cloud_y += 1
    steps+=1
    if steps==125:
        cloud()
        steps=65
    cnt+=1
    if cloud_y > 400:
        cloud_y = 65  # Reset to the starting position
    if cnt==8:
        r+=1
        cnt=0
    if cloud_y ==65:
        r=20
def draw():
    #global steps
    glClear(GL_COLOR_BUFFER_BIT)
    square()
    rectangle()
    triangle()
    chimney()
    cloud()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    glutInitWindowPosition(0, 0)
    glutInitWindowSize(800, 800)
    glutCreateWindow('polygon')
    glutDisplayFunc(draw)
    init()
    glutIdleFunc(draw)  # Register the draw function for animation
    glutMainLoop()

if __name__ == "__main__":
    main()
