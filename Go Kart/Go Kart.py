from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def kepala():
    glColor3ub(150, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(70, 130)
    glVertex2f(80, 140)
    glVertex2f(95, 150)
    glVertex2f(125, 150)
    glVertex2f(140, 140)
    glVertex2f(150, 130)
    glVertex2f(80, 130)
    glVertex2f(140, 130)
    glEnd()

def Badan():
    glColor3ub(145, 142, 142)
    glBegin(GL_POLYGON)
    glVertex2f(80, 130)
    glVertex2f(90, 120)
    glVertex2f(90, 80)
    glVertex2f(130, 80)
    glVertex2f(130, 120)
    glVertex2f(140, 130)
    glEnd()

def SayapKanan():
    glColor3ub(0, 30, 180)
    glBegin(GL_POLYGON)
    glVertex2f(130, 80)
    glVertex2f(140, 70)
    glVertex2f(150, 60)
    glVertex2f(150, 20)
    glVertex2f(140, 20)
    glVertex2f(140, 60)
    glVertex2f(130, 70)
    glEnd()

def SayapKiri():
    glColor3ub(0, 30, 180)
    glBegin(GL_POLYGON)
    glVertex2f(90, 80)
    glVertex2f(80, 70)
    glVertex2f(70, 60)
    glVertex2f(70, 20)
    glVertex2f(80, 20)
    glVertex2f(80, 60)
    glVertex2f(90, 70)
    glEnd()

def Belakang():
    glColor3ub(218,165,32)
    glBegin(GL_POLYGON)
    glVertex2f(90, 80)
    glVertex2f(130, 80)
    glVertex2f(130, 70)
    glVertex2f(130, 50)
    glVertex2f(130, 30)
    glVertex2f(120, 40)
    glVertex2f(120, 60)
    glVertex2f(100, 60)
    glVertex2f(100, 40)
    glVertex2f(90, 30)
    glVertex2f(90, 50)
    glVertex2f(90, 70)
    glEnd()


def iterate():
    glViewport(0, 0, 200, 200) #utk mengatur area pandang
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 160, 0.0, 160, 0.0, 1.0) #utk mengatur berapa blok yang digunakan (skala) nilai x, y, z
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    kepala()
    Badan()
    SayapKanan()
    SayapKiri()
    Belakang()
    glutSwapBuffers()

glutInit() #inisialisasi glut
glutInitDisplayMode(GLUT_RGBA) #utk mengatur display supaya berwarna
glutInitWindowSize(200, 200) #utk mengatur ukuran window
glutInitWindowPosition(0, 0) #utk mengatur letak window
#utk transparansi (tapi belum bisa)
#glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
#glEnable(GL_BLEND)
wind = glutCreateWindow("OpenGL Coding Practice") #utk memberi nama pada window
glutDisplayFunc(showScreen) #utk fungsi callback
glutIdleFunc(showScreen) #utk fungsi callback
glutMainLoop() #fungsi yang akan memulai keseluruhan program