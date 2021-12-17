from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def kepala():
    glColor3ub(17, 22, 186)
    glBegin(GL_POLYGON)
    glVertex2f(23, 28)
    glVertex2f(31, 28)
    glVertex2f(22, 20)
    glVertex2f(32, 20)
    glEnd()

def LampuKanan():
    glColor3ub(172, 173, 191)
    glBegin(GL_POLYGON)
    glVertex2f(31.2, 26.4)
    glVertex2f(298, 26.4)
    glVertex2f(292, 28)
    glVertex2f(31, 28)
    glEnd()

def LampuKiri():
    glColor3ub(172, 173, 191)
    glBegin(GL_POLYGON)
    glVertex2f(22.8, 26.4)
    glVertex2f(24.2, 26.4)
    glVertex2f(24.8, 28)
    glVertex2f(23, 28)
    glEnd()

def Mulut():
    glColor3ub(171, 15, 18)
    glBegin(GL_POLYGON)
    glVertex2f(22, 20)
    glVertex2f(24, 22)
    glVertex2f(24, 24)
    glVertex2f(26, 25)
    glVertex2f(28, 25)
    glVertex2f(30, 25)
    glVertex2f(30, 32)
    glVertex2f(32, 30)
    glEnd()

def Badan():
    glColor3ub(224, 215, 211)
    glBegin(GL_POLYGON)
    glVertex2f(22, 20)
    glVertex2f(32, 20)
    glVertex2f(32, 8)
    glVertex2f(22, 8)
    glEnd()

def HiasanSatu():
    glColor3ub(17, 22, 186)
    glBegin(GL_POLYGON)
    glVertex2f(22, 10)
    glVertex2f(32, 10)
    glVertex2f(27, 12)
    glEnd()

def HiasanDua():
    glColor3ub(171, 15, 18)
    glBegin(GL_POLYGON)
    glVertex2f(24, 20)
    glVertex2f(24, 14)
    glVertex2f(27, 16)
    glVertex2f(30, 14)
    glVertex2f(30, 20)
    glEnd()



def iterate():
    glViewport(0, 0, 100, 100) #utk mengatur area pandang
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 100, 0.0, 100, 0.0, 1.0) #utk mengatur berapa blok yang digunakan (skala) nilai x, y, z
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    kepala()
    LampuKanan()
    LampuKiri()
    Mulut()
    Badan()
    HiasanSatu()
    HiasanDua()
    glutSwapBuffers()

glutInit() #inisialisasi glut
glutInitDisplayMode(GLUT_RGBA) #utk mengatur display supaya berwarna
glutInitWindowSize(100, 100) #utk mengatur ukuran window
glutInitWindowPosition(0, 0) #utk mengatur letak window
#utk transparansi (tapi belum bisa)
#glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
#glEnable(GL_BLEND)
wind = glutCreateWindow("OpenGL Coding Practice") #utk memberi nama pada window
glutDisplayFunc(showScreen) #utk fungsi callback
glutIdleFunc(showScreen) #utk fungsi callback
glutMainLoop() #fungsi yang akan memulai keseluruhan program