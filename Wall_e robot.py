from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np
from math import *

def drawcircle(r=0.1, xc=0, yc=0):
    glBegin(GL_POLYGON)
    for theta in np.arange(0, 2 * pi, 0.001):
        x = r * cos(theta)
        y = r * sin(theta)
        glVertex(x + xc, y + yc)
    glEnd()

def drawrect(l=0.1, w=0.1, xc=0.0, yc=0.0, ro=0.0, go=0.0, bo=0.0, rf=0.0, gf=0.0, bf=0.0, lw=3.0):
    glLineWidth(lw)
    glColor3f(rf, gf, bf)
    glBegin(GL_POLYGON)
    glVertex(l / 2 + xc, w / 2 + yc)
    glVertex(l / 2 + xc, w / 2 - w + yc)
    glVertex(l / 2 - l + xc, w / 2 - w + yc)
    glVertex(l / 2 - l + xc, w / 2 + yc)
    glEnd()
    glColor3f(ro, go, bo)
    glBegin(GL_LINE_LOOP)
    glVertex(l / 2 + xc, w / 2 + yc)
    glVertex(l / 2 + xc, w / 2 - w + yc)
    glVertex(l / 2 - l + xc, w / 2 - w + yc)
    glVertex(l / 2 - l + xc, w / 2 + yc)
    glEnd()

def draw():
    glClearColor(1,1,1,0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0,0,0)

#nick
    drawrect(.08, .22, 0, .65, .2, .2, .3, 1, .8, 0.4, 3)
    drawrect(.095, .03, 0, .5756, .2, .2, .3, 1,.8, 0.4,3)
    drawrect(.095, .03, 0, .5456, .2, .2, .3, 1,.8, 0.4,3)
    drawrect(.095, .03, 0, .5165, .2, .2, .3, 1,.8, 0.4,3)
    drawrect(.095, .095, 0, .72, .2, .2, .3, 1,.8, 0.4, 3)

#right leg
    drawrect(.049, .039, -.273, -0.52, .2, .2, .3, .5, .55, .6, 3)
    drawrect(.25, .35, -.41, -0.48, 0,0,0, .49,.5, .51, 3)
    drawrect(.25, .05, -.41, -0.48, 0,0,0, .49,.5, .51, 3)
    drawrect(.25, .05, -.41, -0.43, 0,0,0, .49,.5, .51, 3)
    drawrect(.25, .05, -.41, -0.38, 0,0,0, .49,.5, .51, 3)
    drawrect(.25, .05, -.41, -0.53, 0,0,0, .49,.5, .51, 3)
    drawrect(.25, .05, -.41, -0.58, 0,0,0, .49,.5, .51, 3)
    drawrect(.049, .099, -.237, -0.5, .2, .2, .3, .5, .55, .6, 3)
    drawrect(.1, .14, -.22, -0.42, .2, .2, .3, .5, .55, .6, 3)
    glColor(0, 0, 0)
    drawcircle(.01, -.19, -.47)

#left leg
    drawrect(.049, .039, .273, -0.52, .2, .2, .3, .5, .55, .6, 3)
    drawrect(.25, .35, .41, -0.48, 0, 0, 0, .49, .5, .51, 3)
    drawrect(.25, .05, .41, -0.48, 0, 0, 0, .49, .5, .51, 3)
    drawrect(.25, .05, .41, -0.43, 0, 0, 0, .49, .5, .51, 3)
    drawrect(.25, .05, .41, -0.38, 0, 0, 0, .49, .5, .51, 3)
    drawrect(.25, .05, .41, -0.53, 0, 0, 0, .49, .5, .51, 3)
    drawrect(.25, .05, .41, -0.58, 0, 0, 0, .49, .5, .51, 3)
    drawrect(.049, .099, .237, -0.5, .2, .2, .3, .5, .55, .6, 3)
    drawrect(.1, .14, .22, -0.42, .2, .2, .3, .5, .55, .6, 3)
    glColor(0, 0, 0)
    drawcircle(.01, .19, -.47)

#bpdy
    drawrect(.66, .2, 0, .359, .2, .2, .3, 1, .8, 0.4, 3)
    drawrect(.6, .7, 0, 0, .2, .2, .3, 0.99, .82, 0.3, 3)
    drawrect(.26, .4, -.151, .088,  1, .88, 0.545, 1, .88, 0.545, 9)
    drawrect(.6, .2, 0, .4, .2, .2, .3, 1, .8, 0.4, 3)

# additions on body
    drawrect(.7, .07, 0, .4, .2, .2, .3, 1, .8, 0.4, 3)
    drawrect(.4, .2, 0, .4, .2, .2, .3, 1, .8, 0.4, 3)
    drawrect(.15, .1, -.1, .4, .2, .2, .3, .1, .8, .9, 4)
    glColor(.15,.27,.46)
    drawcircle(.05, .09, .4)
    glColor(1,0,0)
    drawcircle(.02, .09, .4)

#lefteye
    glColor(0,0,0)
    drawcircle(.021, .056, .66)
    glColor(0.83,0.917,0.945)
    drawcircle(.081, .119, .717)
    drawcircle(.041, .0747, .787)
    glColor(0.345,0.443,0.565)
    drawcircle(.065, .095, .75)
    drawcircle(.031, .095, .75)
    glColor(.999, .995, .97)
    drawcircle(.011, .094, .74)
    drawcircle(.019, .13, .77)

#righteye
    glColor(0,0,0)
    drawcircle(.021, -.056, .66)
    glColor(0.83,0.917,0.945)
    drawcircle(.081,- .119, .717)
    drawcircle(.041,- .0747, .787)
    glColor(0.345,0.443,0.565)
    drawcircle(.065, -.095, .75)
    drawcircle(.031, -.095, .75)
    glColor(.999, .995, .97)
    drawcircle(.011, -.094, .74)
    drawcircle(.019, -.13, .77)

#leftarm
    drawrect(.48, .1, -.44, .19, .2, .3, .3, .5, .55, .6, 3)
    drawrect(.25, .08, -.32, .28, .2, .3, .3, .85, .9, .95, 3)
    drawrect(.125, .08, -.381, .28, .2, .3, .3, .85, .9, .95, 3)
    drawrect(.325, .04, -.681, .26, .2, .3, .3, .85, .9, .95, 3)
    drawrect(.325, .04, -.681, .12, .2, .3, .3, .85, .9, .95, 3)
    drawrect(.25, .08, -.32, .15, .2, .3, .3, .85, .9, .95, 3)
    drawrect(.125, .08, -.381, .15, .2, .3, .3, .85, .9, .95, 3)
    drawrect(.022, .17, -.271, .22, .2, .3, .3, .85, .9, .95, 3)
# rightarm
    drawrect(.48, .1, .44, .19, .2, .3, .3, .5, .55, .6, 3)
    drawrect(.25, .08, .32, .28, .2, .3, .3, .85, .9, .95, 3)
    drawrect(.125, .08, .381, .28, .2, .3, .3, .85, .9, .95, 3)
    drawrect(.325, .04, .681, .26, .2, .3, .3, .85, .9, .95, 3)
    drawrect(.325, .04, .681, .12, .2, .3, .3, .85, .9, .95, 3)
    drawrect(.25, .08, .32, .15, .2, .3, .3, .85, .9, .95, 3)
    drawrect(.125, .08, .381, .15, .2, .3, .3, .85, .9, .95, 3)
    drawrect(.022, .17, .271, .22, .2, .3, .3, .85, .9, .95, 3)

    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(700,700)
glutCreateWindow(b"lab2 program ")
glutDisplayFunc(draw)
glutMainLoop()
