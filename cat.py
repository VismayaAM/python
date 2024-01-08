from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

# Initial positions
dog_pos = [0, 0]
cat_pos = [0, 0]
tree_pos = [0, 0]

# Animation parameters
animation_step = 0.1

def draw_circle(radius, x, y):
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)
    for i in range(360):
        angle = i * 3.14159 / 180
        glVertex2f(x + radius * math.cos(angle), y + radius * math.sin(angle))
    glEnd()

def draw_rect(x, y, width, height):
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    glEnd()

def draw_dog(x, y):
    # Body
    glColor3f(1, 0, 0) # Red color for dog
    draw_circle(15, x, y)

    # Head
    glColor3f(1, 0, 0)
    draw_circle(8, x + 20, y)

    # Eyes
    glColor3f(0, 0, 0) # Black color for eyes
    draw_circle(2, x + 18, y + 2)
    draw_circle(2, x + 22, y + 2)

    # Ears
    glColor3f(1, 0, 0)
    draw_circle(3, x + 16, y + 15)
    draw_circle(3, x + 24, y + 15)

    # Legs
    glColor3f(0, 0, 0)
    draw_rect(x + 10, y - 20, 2, 10)
    draw_rect(x + 17, y - 20, 2, 10)
    draw_rect(x + 10, y - 30, 2, 10)
    draw_rect(x + 17, y - 30, 2, 10)

def draw_cat(x, y):
    # Body
    glColor3f(0, 0, 1) # Blue color for cat
    draw_circle(8, x, y)

    # Head
    glColor3f(0, 0, 1)
    draw_circle(5, x + 12, y)

    # Eyes
    glColor3f(0, 0, 0)
    draw_circle(1, x + 11, y + 1)
    draw_circle(1, x + 13, y + 1)

    # Ears
    glColor3f(0, 0, 1)
    glBegin(GL_TRIANGLES)
    glVertex2f(x + 10, y + 8)
    glVertex2f(x + 13, y + 12)
    glVertex2f(x + 16, y + 8)
    glEnd()

    # Legs
    glColor3f(0, 0, 0)
    draw_rect(x + 5, y - 10, 1, 5)
    draw_rect(x + 9, y - 10, 1, 5)
    draw_rect(x + 5, y - 15, 1, 5)
    draw_rect(x + 9, y - 15, 1, 5)

'''def draw_tree(x, y):
    glColor3f(0, 0.5, 0) # Green color for tree
    glBegin(GL_QUADS)
    glVertex2f(x - 5, y - 30)
    glVertex2f(x + 5, y - 30)
    glVertex2f(x + 5, y + 30)
    glVertex2f(x - 5, y + 30)
    glEnd()'''

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    draw_dog(*dog_pos)
    draw_cat(*cat_pos)
    #draw_tree(*tree_pos)

    glutSwapBuffers()

def update_scene(value):
    global dog_pos, cat_pos
    # Update positions for animation
    dog_pos[0] += animation_step
    cat_pos[0] += animation_step

    # If the dog catches the cat, reset positions
    if dog_pos[0] >= cat_pos[0]:
        dog_pos = [0, 0]
        cat_pos = [0, 0]

    glutPostRedisplay()
    glutTimerFunc(30, update_scene, 0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Dog Chasing Cat")

    glClearColor(1, 1, 1, 1)
    gluOrtho2D(-50, 50, -50, 50)

    glutDisplayFunc(display)
    glutTimerFunc(25, update_scene, 0)

    glutMainLoop()

if __name__ == "__main__":
    main()