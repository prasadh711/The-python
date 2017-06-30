import pygame
import sys
from random import randint
from pygame.locals import *
pygame.init()
setDisplay=pygame.display.set_mode((600,600))
pygame.display.set_caption("sample")
fps=3
img=pygame.image.load("image1.jpg")        #image1 is board
imgx=0
imgy=0
img1=pygame.image.load("sq2.jpg")           #image2 is yellow square
i1x=250
i1y=300
img2=pygame.image.load("sq1.png")            #image 3 is another square
i2x=40
i2y=0
fpstime=pygame.time.Clock()
def getc(n):                             #to set coordinates for particular number on board
    if(n<=10 and n>=1):
        y=525
        if(n==1):
            x=20
        elif(n==2):
            x=80
        elif(n==3):
            x=140
        elif(n==4):
            x=190
        elif(n==5):
            x=250
        elif(n==6):
            x=300
        elif(n==7):
            x=360
        elif(n==8):
            x=410
        elif(n==9):
            x=465
        elif(n==10):
            x=520
        return x,y
    if(n<=20 and n>=11):
        y=470
        if(n==20):
            x=20
        elif(n==19):
            x=80
        elif(n==18):
            x=140
        elif(n==17):
            x=190
        elif(n==16):
            x=250
        elif(n==15):
            x=300
        elif(n==14):
            x=360
        elif(n==13):
            x=410
        elif(n==12):
            x=465
        elif(n==11):
            x=520
        return x,y
    if(n<=30 and n>=21):
        y=410
        if(n==21):
            x=20
        elif(n==22):
            x=80
        elif(n==23):
            x=140
        elif(n==24):
            x=190
        elif(n==25):
            x=250
        elif(n==26):
            x=300
        elif(n==27):
            x=360
        elif(n==28):
            x=410
        elif(n==29):
            x=465
        elif(n==30):
            x=520
        return x,y
    if(n<=40 and n>=31):
        y=360
        if(n==40):
            x=20
        elif(n==39):
            x=80
        elif(n==38):
            x=140
        elif(n==37):
            x=190
        elif(n==36):
            x=250
        elif(n==35):
            x=300
        elif(n==34):
            x=360
        elif(n==33):
            x=410
        elif(n==32):
            x=465
        elif(n==31):
            x=520
        return x,y
    if(n<=50 and n>=41):
        y=300
        if(n==41):
            x=20
        elif(n==42):
            x=80
        elif(n==43):
            x=140
        elif(n==44):
            x=190
        elif(n==45):
            x=250
        elif(n==46):
            x=300
        elif(n==47):
            x=360
        elif(n==48):
            x=410
        elif(n==49):
            x=465
        elif(n==50):
            x=520
        return x,y
    if(n<=60 and n>=51):
        y=250
        if(n==60):
            x=20
        elif(n==59):
            x=80
        elif(n==58):
            x=140
        elif(n==57):
            x=190
        elif(n==56):
            x=250
        elif(n==55):
            x=300
        elif(n==54):
            x=360
        elif(n==53):
            x=410
        elif(n==52):
            x=465
        elif(n==51):
            x=520
        return x,y
    if(n<=70 and n>=61):
        y=195
        if(n==61):
            x=20
        elif(n==62):
            x=80
        elif(n==63):
            x=140
        elif(n==64):
            x=190
        elif(n==65):
            x=250
        elif(n==66):
            x=300
        elif(n==67):
            x=360
        elif(n==68):
            x=410
        elif(n==69):
            x=465
        elif(n==70):
            x=520
        return x,y
    if(n<=80 and n>=71):
        y=135
        if(n==80):
            x=20
        elif(n==79):
            x=80
        elif(n==78):
            x=140
        elif(n==77):
            x=190
        elif(n==76):
            x=250
        elif(n==75):
            x=300
        elif(n==74):
            x=360
        elif(n==73):
            x=410
        elif(n==72):
            x=465
        elif(n==71):
            x=520
        return x,y
    if(n<=90 and n>=81):
        y=80
        if(n==81):
            x=20
        elif(n==82):
            x=80
        elif(n==83):
            x=140
        elif(n==84):
            x=190
        elif(n==85):
            x=250
        elif(n==86):
            x=300
        elif(n==87):
            x=360
        elif(n==88):
            x=410
        elif(n==89):
            x=465
        elif(n==90):
            x=520
        return x,y
    if(n<=100 and n>=91):
        y=20
        if(n==100):
            x=20
        elif(n==99):
            x=80
        elif(n==98):
            x=140
        elif(n==97):
            x=190
        elif(n==96):
            x=250
        elif(n==95):
            x=300
        elif(n==94):
            x=360
        elif(n==93):
            x=410
        elif(n==92):
            x=465
        elif(n==91):
            x=520
        return x,y       
p1=0
def check1(p):              #if snake appears jump to end of snake
    if(p==16 or p==31 or p==47 or p==63 or p==66 or p==97):
        pygame.time.delay(1000)
    if(p==16):
        return 13
    elif(p==31):
        return 4
    elif(p==47):
        return 25
    elif(p==63):
        return 60
    elif(p==66):
        return 52
    elif(p==97):
        return 75
    else:
        return p
def check2(p):      #if ladder occurs jump to top of ladder
    if(p==3 or p==10 or p==27 or p==56 or p==61 or p==72):
        pygame.time.delay(1000)
    if(p==3):
        return 39
    elif(p==10):
        return 12
    elif(p==27):
        return 53
    elif(p==56):
        return 84
    elif(p==61):
        return 99
    elif(p==72):
        return 90
    else:
        return p
while True:
    n=0
    setDisplay.blit(img,(imgx,imgy))
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            n=randint(1,6)
            p1=p1+n
            i1x,i1y=getc(p1)
            setDisplay.blit(img1,(i1x,i1y))    
            p1=check1(p1)
            p1=check2(p1)
            i1x,i1y=getc(p1)
    setDisplay.blit(img1,(i1x,i1y))
    pygame.display.update()
