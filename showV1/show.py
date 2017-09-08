#
# showV1/show.py
#
# Author: Matthew Atteberry
# CSCI 385: Computer Graphics, Reed College, Fall 2017
#
#Modified from:	
#	showV1/show.py
#
#	Author: Jim Fix
#	CSCI 385: Computer Graphics, Reed College, Fall 2017
#
#	This is a sample GLUT program that displays a tetrahedron 
#	made up of triangular facets.
#
#	The OpenGL drawing part of the code occurs in drawScene. 
#
#	This code was adapted from Sam Buss' SimpleDraw.py.
#

import math
import sys
from random import random
from math import pi

from OpenGL.GLUT import *
from OpenGL.GL import *

from PIL import Image #will need to install PIL with: [INSERT CMD]

wireframe = False
rotation1 = 0.0
rotation2 = 0.0
show_which = 0
smoothness = 10; #controls the amount of segments approximating curves
bumpH = 0.15;
degToRad = (2*math.pi/smoothness) #for geometric calculations
iR = 0.5 #inner torus radius
oR = 1 #outter torus radius
im = Image.open("volcano.png")
imRGB = im.convert('RGB')
xSize = 2/im.size[0]
ySize = 2/im.size[1]

def drawTetra(): #press 0

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

def drawCube(): #press 1

	# Draw all the triangular facets.
	glBegin(GL_TRIANGLES)

	# Each Face (Bottom, Top, Left, Right, Back, Front)
	# is made up of two triangles.
	# I used a rubix cube color scheme

	# bottom XZ face
	glColor3f(0.72,0.07,0.2) #Red

	glVertex3f( -0.5,-0.5, -0.5)
	glVertex3f( 0.5,-0.5, -0.5)
	glVertex3f( 0.5,-0.5, 0.5)


	glVertex3f( -0.5,-0.5, -0.5)
	glVertex3f( -0.5,-0.5, 0.5)
	glVertex3f( 0.5,-0.5, 0.5)

	# top XZ face 
	glColor3f(1.0,0.35,0.0) #Orange

	glVertex3f( -0.5,0.5, -0.5)
	glVertex3f( 0.5,0.5, -0.5)
	glVertex3f( 0.5,0.5, 0.5)

	glVertex3f( -0.5,0.5, -0.5)
	glVertex3f( -0.5,0.5, 0.5)
	glVertex3f( 0.5,0.5, 0.5)

	# left YZ face 
	glColor3f(0.0,0.6,0.28) #Green

	glVertex3f( -0.5,-0.5, -0.5)
	glVertex3f( -0.5,0.5, -0.5)
	glVertex3f( -0.5,0.5, 0.5)

	glVertex3f( -0.5,-0.5, -0.5)
	glVertex3f( -0.5,-0.5, 0.5)
	glVertex3f( -0.5,0.5, 0.5)

	# right YZ face 
	glColor3f(0.0,0.27,0.68) #Blue

	glVertex3f( 0.5,-0.5, -0.5)
	glVertex3f( 0.5,0.5, -0.5)
	glVertex3f( 0.5,0.5, 0.5)

	glVertex3f( 0.5,-0.5, -0.5)
	glVertex3f( 0.5,-0.5, 0.5)
	glVertex3f( 0.5,0.5, 0.5)

	# back XY face
	glColor3f(1.0,1.0,1.0) #White

	glVertex3f( -0.5,-0.5, -0.5)
	glVertex3f( 0.5,-0.5, -0.5)
	glVertex3f( 0.5,0.5, -0.5)

	glVertex3f( -0.5,-0.5, -0.5)
	glVertex3f( -0.5,0.5, -0.5)
	glVertex3f( 0.5,0.5, -0.5)

	# front XY face
	glColor3f(1.0,0.84,0.0) #Yellow

	glVertex3f( -0.5,-0.5, 0.5)
	glVertex3f( 0.5,-0.5, 0.5)
	glVertex3f( 0.5,0.5, 0.5)

	glVertex3f( -0.5,-0.5, 0.5)
	glVertex3f( -0.5,0.5, 0.5)
	glVertex3f( 0.5,0.5, 0.5)

	glEnd()

def drawCyclinder(): #press 2
	
	# Draw all the triangular facets.
	glBegin(GL_TRIANGLES)

	for i in range(0,smoothness):

		#two triangles for segment of cylindr side
		glColor3f(math.sin(i*degToRad),0.1,1 - math.cos(i*degToRad))
		glVertex3f(math.sin(i*degToRad),-1.0, math.cos(i*degToRad))

		glColor3f(math.sin(i*degToRad),0.9,1 - math.cos(i*degToRad))
		glVertex3f(math.sin(i*degToRad),1.0, math.cos(i*degToRad))

		glColor3f(math.sin((i+1)*degToRad),0.9,1 - math.cos((i+1)*degToRad))
		glVertex3f(math.sin((i+1)*degToRad),1.0, math.cos((i+1)*degToRad))


		glColor3f(math.sin(i*degToRad),0.1,1 - math.cos(i*degToRad))
		glVertex3f(math.sin(i*degToRad),-1.0, math.cos(i*degToRad))

		glColor3f(math.sin((i+1)*degToRad),0.1,1 - math.cos((i+1)*degToRad))
		glVertex3f(math.sin((i+1)*degToRad),-1.0, math.cos((i+1)*degToRad))

		glColor3f(math.sin((i+1)*degToRad),0.9,1 - math.cos((i+1)*degToRad))
		glVertex3f(math.sin((i+1)*degToRad),1.0, math.cos((i+1)*degToRad))

		#bottom triangle
		glColor3f(math.sin(i*degToRad),0.1,1 - math.cos(i*degToRad))
		glVertex3f(math.sin(i*degToRad),-1.0, math.cos(i*degToRad))

		glColor3f(math.sin((i+1)*degToRad),0.1,1 - math.cos((i+1)*degToRad))
		glVertex3f(math.sin((i+1)*degToRad),-1.0, math.cos((i+1)*degToRad))

		glColor3f(0.0,0.0,0.0)
		glVertex3f(0,-1.0, 0)

		#top triangle
		glColor3f(math.sin(i*degToRad),0.9,1 - math.cos(i*degToRad))
		glVertex3f(math.sin(i*degToRad),1.0, math.cos(i*degToRad))

		glColor3f(math.sin((i+1)*degToRad),0.9,1 - math.cos((i+1)*degToRad))
		glVertex3f(math.sin((i+1)*degToRad),1.0, math.cos((i+1)*degToRad))

		glColor3f(1.0,1.0,1.0)
		glVertex3f(0,1.0, 0)

	glEnd()

def drawSphere(): #press 3

	# Draw all the triangular facets.
	glBegin(GL_TRIANGLES)

	for i in range(0,smoothness):
		for j in range(0,smoothness):
			#two triangles for segment of sphere
			glColor3f(math.sin(i*degToRad),-math.cos(0.5*j*degToRad),math.cos(i*degToRad))
			glVertex3f(math.sin(0.5*j*degToRad)*math.sin(i*degToRad),-math.cos(0.5*j*degToRad), math.sin(0.5*j*degToRad)*math.cos(i*degToRad))

			glColor3f(math.sin(i*degToRad),-math.cos(0.5*(j+1)*degToRad),math.cos(i*degToRad))
			glVertex3f(math.sin(0.5*(j+1)*degToRad)*math.sin(i*degToRad),-math.cos(0.5*(j+1)*degToRad), math.sin(0.5*(j+1)*degToRad)*math.cos(i*degToRad))

			glColor3f(math.sin((i+1)*degToRad),-math.cos(0.5*(j+1)*degToRad),math.cos((i+1)*degToRad))
			glVertex3f(math.sin(0.5*(j+1)*degToRad)*math.sin((i+1)*degToRad),-math.cos(0.5*(j+1)*degToRad), math.sin(0.5*(j+1)*degToRad)*math.cos((i+1)*degToRad))

			#--------------------------------------------------------------

			glColor3f(math.sin(i*degToRad),-math.cos(0.5*j*degToRad),math.cos(i*degToRad))
			glVertex3f(math.sin(0.5*j*degToRad)*math.sin(i*degToRad),-math.cos(0.5*j*degToRad), math.sin(0.5*j*degToRad)*math.cos(i*degToRad))

			glColor3f(math.sin((i+1)*degToRad),-math.cos(0.5*j*degToRad),math.cos((i+1)*degToRad))
			glVertex3f(math.sin(0.5*j*degToRad)*math.sin((i+1)*degToRad),-math.cos(0.5*j*degToRad), math.sin(0.5*j*degToRad)*math.cos((i+1)*degToRad))

			glColor3f(math.sin((i+1)*degToRad),-math.cos(0.5*(j+1)*degToRad),math.cos((i+1)*degToRad))
			glVertex3f(math.sin(0.5*(j+1)*degToRad)*math.sin((i+1)*degToRad),-math.cos(0.5*(j+1)*degToRad), math.sin(0.5*(j+1)*degToRad)*math.cos((i+1)*degToRad))

	glEnd()

def drawTorus(): #press 4


	# Draw all the triangular facets.
	glBegin(GL_TRIANGLES)
	
	for i in range(0,smoothness):
		for j in range(0,smoothness):
			#two triangles for segment of sphere
			glColor3f(math.sin(i*degToRad),-math.cos(j*degToRad),math.cos(i*degToRad))
			glVertex3f((oR + iR*math.sin(j*degToRad))*math.sin(i*degToRad),iR*math.cos(j*degToRad), (oR + iR*math.sin(j*degToRad))*math.cos(i*degToRad))

			glColor3f(math.sin(i*degToRad),-math.cos((j+1)*degToRad),math.cos(i*degToRad))
			glVertex3f((oR + iR*math.sin((j+1)*degToRad))*math.sin(i*degToRad),iR*math.cos((j+1)*degToRad),(oR + iR*math.sin((j+1)*degToRad))*math.cos(i*degToRad))

			glColor3f(math.sin((i+1)*degToRad),-math.cos((j+1)*degToRad),math.cos((i+1)*degToRad))
			glVertex3f((oR + iR*math.sin((j+1)*degToRad))*math.sin((i+1)*degToRad),iR*math.cos((j+1)*degToRad), (oR + iR*math.sin((j+1)*degToRad))*math.cos((i+1)*degToRad))

			#--------------------------------------------------------------

			glColor3f(math.sin(i*degToRad),-math.cos(j*degToRad),math.cos(i*degToRad))
			glVertex3f((oR + iR*math.sin(j*degToRad))*math.sin(i*degToRad),iR*math.cos(j*degToRad),(oR + iR*math.sin(j*degToRad))*math.cos(i*degToRad))

			glColor3f(math.sin((i+1)*degToRad),-math.cos(j*degToRad),math.cos((i+1)*degToRad))
			glVertex3f((oR + iR*math.sin(j*degToRad))*math.sin((i+1)*degToRad),iR*math.cos(j*degToRad), (oR + iR*math.sin(j*degToRad))*math.cos((i+1)*degToRad))

			glColor3f(math.sin((i+1)*degToRad),-math.cos((j+1)*degToRad),math.cos((i+1)*degToRad))
			glVertex3f((oR + iR*math.sin((j+1)*degToRad))*math.sin((i+1)*degToRad),iR*math.cos((j+1)*degToRad),(oR + iR*math.sin((j+1)*degToRad))*math.cos((i+1)*degToRad)) 


	glEnd()

def drawBumpMap(): #press 5

	# Draw all the triangular facets.
	glBegin(GL_TRIANGLES)

	#Fill terrain
	for x in range(1,im.size[0]-1):
		for y in range(1,im.size[1]-1):

			#luminance equations allow for interpretation of color pictures as bump maps! https://en.wikipedia.org/wiki/Relative_luminance
			r,g,b = imRGB.getpixel((x,y))
			r,g,b = r/255,g/255,b/255
			currentPix = 0.2126*r + 0.7152*g+ 0.0722*b
			r,g,b = imRGB.getpixel((x+1,y))
			r,g,b = r/255,g/255,b/255
			currentXPix = 0.2126*r + 0.7152*g+ 0.0722*b
			r,g,b = imRGB.getpixel((x,y+1))
			r,g,b = r/255,g/255,b/255
			currentYPix = 0.2126*r + 0.7152*g+ 0.0722*b
			r,g,b = imRGB.getpixel((x+1,y+1))
			r,g,b = r/255,g/255,b/255
			currentXYPix = 0.2126*r + 0.7152*g+ 0.0722*b




			glColor3f(x/im.size[0],currentPix,y/im.size[1])
			glVertex3f( -1.0 + xSize*x, currentPix*bumpH,  -1.0 + ySize*y)

			glColor3f(x/im.size[0],currentXPix,y/im.size[1])
			glVertex3f( -1.0 + xSize*(x+1), currentXPix*bumpH,  -1.0 + ySize*y)

			glColor3f((x+1)/im.size[0],currentXYPix,(y+1)/im.size[1])
			glVertex3f( -1.0 + xSize*(x+1), currentXYPix*bumpH,  -1.0 + ySize*(y+1))



			glColor3f(x/im.size[0],currentPix,y/im.size[1])
			glVertex3f( -1.0 + xSize*x, currentPix*bumpH,  -1.0 + ySize*y)

			glColor3f((x+1)/im.size[0],currentYPix,(y+1)/im.size[1])
			glVertex3f( -1.0 + xSize*x, currentYPix*bumpH,  -1.0 + ySize*(y+1))

			glColor3f((x+1)/im.size[0],currentXYPix,(y+1)/im.size[1])
			glVertex3f( -1.0 + xSize*(x+1), currentXYPix*bumpH,  -1.0 + ySize*(y+1))


	glEnd()
	

def drawObject():
	
	#ensure refernce to show_which
	global show_which

	if show_which == 0:
		drawTetra()
	elif show_which ==1:
		drawCube()
	elif show_which ==2:
		drawCyclinder()
	elif show_which ==3:
		drawSphere()
	elif show_which ==4:
		drawTorus()
	elif show_which ==5:
		drawBumpMap()


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

	#ensure refernce to smoothness,degToRad & show_which
	global smoothness
	global show_which
	global degToRad
	global bumpH
	global im
	global imRGB 
	global xSize 
	global ySize

	# Handle the SPACE bar.
	if key == b' ':
		im = Image.open(input("Enter a picture file (>256x256 very slow!) like 'brick.jpg' [wrong names will cause a crash]:"))
		imRGB = im.convert('RGB')
		xSize = 2/im.size[0]
		ySize = 2/im.size[1]
		glutPostRedisplay()

	# Handle the '-' key.
	if key == b'\055':
		smoothness -= 1
		if(smoothness < 1):
			smoothness = 1
		degToRad = (2*math.pi/smoothness)
		# Redraw.
		glutPostRedisplay()

	# Handle the '+' key.
	if key == b'\053':
		smoothness += 1
		# Redraw.
		degToRad = (2*math.pi/smoothness)
		glutPostRedisplay()

	#handles keys for increasing and decreaing bump height
	if key == b'w':
		bumpH += 0.05
		glutPostRedisplay()
	if key == b's':
		bumpH -= 0.05
		if(smoothness < 0.05):
			smoothness = 0.05
		glutPostRedisplay()


	# Handle ESC key.
	if key == b'\033':	
	# "\033" is the Escape key
		sys.exit(1)

	#handles number keys to show different surfaces
	if key == b'\060':
		show_which = 0
		glutPostRedisplay()
	if key == b'\061':
		show_which = 1
		glutPostRedisplay()
	if key == b'\062':
		show_which = 2
		glutPostRedisplay()
	if key == b'\063':
		show_which = 3
		glutPostRedisplay()
	if key == b'\064':
		show_which = 4
		glutPostRedisplay()
	if key == b'\065':
		show_which = 5
		glutPostRedisplay()

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
	print('Press ESC to quit.')
	print('Press space to enter a new image file')
	print('Press + or - to increase/decrease smoothness')
	print('Press w or s to increase/decrease height of bump maps!')

	print('0 = tetrahedron ; 1 = cube ; 2 = cylinder ; 3 = sphere ; 4 = torus ; 5 = bump map \n')

	glutMainLoop()

	return 0

if __name__ == '__main__': main(len(sys.argv),sys.argv)
