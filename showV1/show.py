#
# showV1/show.py
#
# Author: Jim Fix
# CSCI 385: Computer Graphics, Reed College, Fall 2017
#
# This is a sample GLUT program that displays a tetrahedron 
# made up of triangular facets.
#
# The OpenGL drawing part of the code occurs in drawScene. 
#
# This code was adapted from Sam Buss' SimpleDraw.py.
#

import sys
from random import random
from math import pi

from OpenGL.GLUT import *
from OpenGL.GL import *

wireframe = False
rotation1 = 0.0
rotation2 = 0.0
show_which = 0


def drawTetra():

    # This describes the facets of a tetrahedron whose
    # vertices sit at 4 of the 8 corners of the 
    # of the cube volume [-1,1] x [-1,1] x [-1,1].
    
    # Draw all the triangular facets.
    glBegin(GL_TRIANGLES)

    # The three vertices are +-+ ++- -++ ---

    # missing ---
    glColor3f(1.0,1.0,0.0)
    glVertex3f( 1.0,-1.0, 1.0)
    glVertex3f( 1.0, 1.0,-1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    # missing ++-
    glColor3f(0.0,1.0,1.0)
    glVertex3f( 1.0,-1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0,-1.0,-1.0)
    # missing -++
    glColor3f(1.0,0.0,1.0)
    glVertex3f(-1.0,-1.0,-1.0)
    glVertex3f( 1.0, 1.0,-1.0)
    glVertex3f( 1.0,-1.0, 1.0)
    # missing +-+
    glColor3f(1.0,1.0,1.0)
    glVertex3f( 1.0, 1.0,-1.0)
    glVertex3f(-1.0,-1.0,-1.0)
    glVertex3f(-1.0, 1.0, 1.0)

    glEnd()
    

def drawObject():
    
    if show_which == 0:
        drawTetra()
    elif show_which == 1:
	drawCube()
    elif show_which == 2:
	draw(gen_cyllinder(100))
    elif show_which == 3:
	draw(gen_sphere(100))
    elif show_which == 4:
	drawTaurus(100)
    else show_which == 5:
	drawShape(100)

    # Add other objects for the assignment here.
def drawCube():
	x_axis = [[( 1.0,-1.0, 1.0),( 1.0, 1.0,-1.0),( 1.0,-1.0,-1.0)],[( 1.0,-1.0, 1.0),( 1.0, 1.0,-1.0),( 1.0, 1.0, 1.0)],[(-1.0,-1.0, 1.0),(-1.0, 1.0,-1.0),(-1.0,-1.0,-1.0)],[(-1.0,-1.0, 1.0),(-1.0, 1.0,-1.0),(-1.0, 1.0, 1.0)]]
        y_axis = [[(-1.0, 1.0, 1.0),( 1.0, 1.0,-1.0),( 1.0, 1.0, 1.0)],[(-1.0, 1.0, 1.0),( 1.0, 1.0,-1.0),(-1.0, 1.0,-1.0)],[( 1.0,-1.0,-1.0),(-1.0,-1.0, 1.0),( 1.0,-1.0, 1.0)],[(-1.0,-1.0, 1.0),( 1.0,-1.0,-1.0),(-1.0,-1.0,-1.0)]]
        z_axis = [[( 1.0,-1.0, 1.0),(-1.0, 1.0, 1.0),( 1.0, 1.0, 1.0)],[( 1.0,-1.0, 1.0),(-1.0, 1.0, 1.0),(-1.0,-1.0, 1.0)],[( 1.0,-1.0,-1.0),(-1.0, 1.0,-1.0),( 1.0, 1.0,-1.0)],[( 1.0,-1.0,-1.0),(-1.0, 1.0,-1.0),(-1.0,-1.0,-1.0)]]

        sq = x_axis+y_axis+z_axis

        draw(sq)
def draw(ls):
    i=0
    while i < len(ls):
        v = ls[i]
        v1 = v[0]
        v2 = v[1]
        v3 = v[2]
        triangle(v1[0],v1[1],v1[2],v2[0],v2[1],v2[2],v3[0],v3[1],v3[2])
        i=i+1

def triangle(x1,y1,z1,x2,y2,z2,x3,y3,z3):
    r = (x1+x2+x3)/6 +.5
    g = (y1+y2+y3)/6 +.5
    b = (z1+z2+z3)/6 +.5
    glColor3f(r,g,b)
    glVertex3f(x1,y1,z1)
    glVertex3f(x2,y2,z2)
    glVertex3f(x3,y3,z3)

def gen_cyllinder(n):
    topcircle = []
    bottomcircle = []
    walls = []
    p = 0
    while p<n:
        a = sin(p*2*pi/n)
        b = cos(p*2*pi/n)
        p=p+1
        c = sin(p*2*pi/n)
        d = cos(p*2*pi/n)
        topcircle.append([(1,0,0),(1,a,b),(1,c,d)])
        walls.append([(1,c,d),(1,a,b),(-1,c,d)])
        bottomcircle.append([(-1,0,0),(-1,a,b),(-1,c,d)])
        walls.append([(-1,a,b),(1,a,b),(-1,c,d)])
    return (topcircle+bottomcircle+walls)

def gen_sphere(n):
    s = 0
    ret = []
    while s < n:
        q = 1-(s/n)*2
        r = 1-((s+1)/n)*2
        p = 0
        while p < n:
            q1=(1-q**2)**0.5
            r1=(1-r**2)**0.5
            a = sin(p*2*pi/n)
            b = cos(p*2*pi/n)
            p=p+1
            c = sin(p*2*pi/n)
            d = cos(p*2*pi/n)
            ret.append([(q,c*q1,d*q1),(q,a*q1,b*q1),(r,c*r1,d*r1)])
            ret.append([(r,a*r1,b*r1),(q,a*q1,b*q1),(r,c*r1,d*r1)])
        s=s+1
    return ret
	
def drawScene():
    """ Issue GL calls to draw the scene. """

    # Clear the rendering information.
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Clear the transformation stack.
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Transform the objects drawn below by a rotation.
    glRotatef(rotation1*180.0/pi,1.0,0.0,0.0)
    glRotatef(rotation2*180.0/pi,0.0,1.0,0.0)

    # Draw a floating "pixel."
    glColor(1.0,1.0,1.0)
    glPointSize(20)
    #
    glBegin(GL_POINTS)
    glVertex3f(0.0,0.0,2.0)
    glEnd()

    # Draw the object.
    drawObject()

    # Render the scene.
    glFlush()


def myKeyFunc(key, x, y):
    """ Handle a "normal" keypress. """

    # Handle the SPACE bar.
    if key == b' ':
        # Redraw.
        glutPostRedisplay()

    # Handle ESC key.
    if key == b'\033':	
	# "\033" is the Escape key
        sys.exit(1)


def myArrowFunc(key, x, y):
    """ Handle a "special" keypress. """
    global rotation1
    global rotation2

    # Apply an adjustment to the overall rotation.
    if key == GLUT_KEY_UP:
        rotation1 -= pi/12.0
    if key == GLUT_KEY_DOWN:
        rotation1 += pi/12.0
    if key == GLUT_KEY_RIGHT:
        rotation2 += pi/12.0
    if key == GLUT_KEY_LEFT:
        rotation2 -= pi/12.0

    # Redraw.
    glutPostRedisplay()


def initRendering():
    """ Initialize aspects of the GL scene rendering.  """
    glEnable (GL_DEPTH_TEST)


def resizeWindow(w, h):
    """ Register a window resize by changing the viewport.  """
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if w > h:
        glOrtho(-w/h*2.0, w/h*2.0, -2.0, 2.0, -2.0, 2.0)
    else:
        glOrtho(-2.0, 2.0, -h/w * 2.0, h/w * 2.0, -2.0, 2.0)


def main(argc, argv):
    """ The main procedure, sets up GL and GLUT. """

    glutInit(argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowPosition(0, 20)
    glutInitWindowSize(360, 360)
    glutCreateWindow( b'object showcase - Press ESC to quit' )
    initRendering()

    # Register interaction callbacks.
    glutKeyboardFunc(myKeyFunc)
    glutSpecialFunc(myArrowFunc)
    glutReshapeFunc(resizeWindow)
    glutDisplayFunc(drawScene)

    print()
    print('Press the arrow keys to rotate the object.')
    print('Press ESC to quit.\n')
    print()

    glutMainLoop()

    return 0

if __name__ == '__main__': main(len(sys.argv),sys.argv)
