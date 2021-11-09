#import library
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Koordinat x dan y untuk posisi kotak
pos_x = 0
pos_y = 0
# Warna Kotak
hijau = 0
biru = 0
merah = 0
y = 0

# Membuat bentuk jalan
def bg():
    glBegin(GL_QUADS)
    glColor3ub(37, 188, 143)
    glVertex2f(0,0)
    glVertex2f(650,0)
    glVertex2f(650,500)
    glVertex2f(0,500)
    glEnd()

#JALAN RAYA
def jalan(jln):
    glBegin(GL_QUADS) 
    # glColor3ub(60,67,65)
    glColor3ub(0,0,0)
    glVertex2f(jln - 100, 500)
    glVertex2f(jln - 100, 0)
    glVertex2f(jln + 100, 0)
    glVertex2f(jln + 100, 500)
    glEnd()

def tepi(tp):
    glColor3ub(255, 255, 255) #kode warna pake color picker
    glLineWidth(10)
    glBegin(GL_LINES) #utk membuat objek garis
    glVertex2f(tp, 0) 
    glVertex2f(tp, 500)
    glEnd()

def garis_mid(gmx,gm):
    global y
    kecepatan = 1
    y += kecepatan
    if y >500:
        y = 0
    glTranslated(0,y,0)
    glColor3ub(255, 255, 255) #kode warna pake color picker
    glLineWidth(10)
    glBegin(GL_LINES) #utk membuat objek garis
    glVertex2f(gmx, gm) 
    glVertex2f(gmx, gm + 50)
    glEnd()


#fungsi iterasi
def iterate():
    glViewport(0, 0, 500, 500) #utk mengatur area pandang
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 650, 0.0, 500, 0.0, 1.0) #utk mengatur berapa blok yang digunakan (skala) nilai x, y, z
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #utk membersihkan layar
    glLoadIdentity()
    iterate()
    # bg()
    jalan(200)
    jalan(500)
    tepi(100)
    tepi(300)
    tepi(400)
    tepi(600)
    gmy = 20
    for i in range(7):
        garis_mid(200,gmy)
        garis_mid(500,gmy)
        gmy += 70
        
    glutSwapBuffers() #utk membersihkan layar, double buffering

def timer(value):
    glutPostRedisplay()
    glutTimerFunc(10,timer,0)

def update(value):
    glutPostRedisplay()
    glutTimerFunc(3000,update,0)

def init():
    glClearColor(2,1,0, 2.0)
    gluOrtho2D(-500.0, 500.0, -500.0, 500.0)

def main ():   
    glutInit() #inisialisasi glut
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGBA) #utk mengatur display supaya berwarna
    glutInitWindowSize(600, 500) #utk mengatur ukuran window
    glutInitWindowPosition(100,100) #utk mengatur letak window
    glutCreateWindow("2D Car Racing Game") #utk memberi nama pada window
    glutDisplayFunc(showScreen) #utk fungsi callback
    glutIdleFunc(showScreen) #utk fungsi callback
    timer(0)
    # glutTimerFunc(3000, update, 0)
    init()
    glutMainLoop() #fungsi yang akan memulai keseluruhan program

main()