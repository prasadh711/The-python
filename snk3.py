WAVFILE = 'Jump4.wav'
WAVFILE1 = 'Powerup7.wav'
import pygame
import sys
from random import randint
from pygame.locals import *
pygame.init()
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
setDisplay=pygame.display.set_mode((1200,600))
pygame.display.set_caption("sample")
fps=3
black=(0,0,0)
img=pygame.image.load("image1.jpg")
imgx=0
imgy=0
img1=pygame.image.load("sq2.jpg")
i1x=20
i1y=820
img2=pygame.image.load("sq1.png")
i2x=300
i2y=250
d1=pygame.image.load("dice1.jpg")
d1x=700
d1y=120
d2=pygame.image.load("dice2.jpg")
d2x=700
d2y=120
d3=pygame.image.load("dice3.jpg")
d3x=700
d3y=120
d4=pygame.image.load("dice4.jpg")
d4x=700
d4y=120
d5=pygame.image.load("dice5.jpg")
d5x=700
d5y=120
d6=pygame.image.load("dice6.jpg")
d6x=700
d6y=120
p11=pygame.image.load("screenshot1.jpg")
p11x=700
p11y=150
p12=pygame.image.load("screenshot2.jpg")
p12x=700
p12y=150
p21=pygame.image.load("screenshot3.jpg")
p21x=810
p21y=45
p22=pygame.image.load("screenshot4.jpg")
p22x=800
p22y=40
p31=pygame.image.load("screenshot6.jpg")
p31x=700
p31y=100
p32=pygame.image.load("screenshot5.jpg")
p32x=700
p32y=100
snake=pygame.image.load("snake.png")
snakex=700
snakey=120
ladder=pygame.image.load("ladder.jpg")
ladderx=700
laddery=120
def getc(n):
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
def check1(p):
    if(p==16 or p==31 or p==47 or p==63 or p==66 or p==97):
        s = pygame.mixer.Sound(WAVFILE1)
        ch = s.play()
        while ch.get_busy():
            pygame.time.delay(0)
        
        setDisplay.blit(snake,(snakex,snakey))
        pygame.display.update()
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
def check2(p):
    if(p==3 or p==10 or p==27 or p==56 or p==61 or p==72):
         
        s = pygame.mixer.Sound(WAVFILE)
        ch = s.play()
        while ch.get_busy():
            pygame.time.delay(0)
        setDisplay.blit(ladder,(ladderx,laddery))
        pygame.display.update()
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
pno=0
p2=0
def diceprint(n):
    if(n==1):
        setDisplay.blit(d1,(d1x,d1y))
    if(n==2):
        setDisplay.blit(d2,(d2x,d2y))
    if(n==3):
        setDisplay.blit(d3,(d3x,d3y))
    if(n==4):
        setDisplay.blit(d4,(d4x,d4y))
    if(n==5):
        pygame.draw.rect(setDisplay,black,(700,0,700,700))
        setDisplay.blit(d5,(d5x,d5y))
    if(n==6):
        setDisplay.blit(d6,(d6x,d6y))               
while True:
    n=0
    setDisplay.blit(img,(imgx,imgy))
    setDisplay.blit(img2,(i2x,i2y))
    for event in pygame.event.get():
        if event.type==QUIT:
           # print " are you sure you want to quit!!!!\n enter 1 to quit"
            #n=int(input( " are you sure you want to quit!!!!\n enter 1 to quit"))
            #if(n==1):
                pygame.quit()
                sys.exit()
        if event.type==pygame.KEYDOWN:
            n=randint(1,6)
            if(pno==0):
                p1=p1+n
                if(p1>100):
                    p1=p1-n
                diceprint(n)
                i1x,i1y=getc(p1)
                setDisplay.blit(p21,(p21x,p21y))
                setDisplay.blit(img1,(i1x,i1y))    
                p1=check1(p1)
                p1=check2(p1)
                i1x,i1y=getc(p1)
                pno=pno+1
            elif(pno==1):
                p2=p2+n
                if(p2>100):
                    p2=p2-n
                diceprint(n)
                i2x,i2y=getc(p2)
                setDisplay.blit(p22,(p22x,p22y))
                setDisplay.blit(img2,(i2x,i2y))    
                p2=check1(p2)
                
                p2=check2(p2)
                
                i2x,i2y=getc(p2)
                pno=pno+1
    pno=(pno)%2
    setDisplay.blit(img1,(i1x,i1y))
    setDisplay.blit(img2,(i2x,i2y))
    pygame.display.update()
    if(p1==100):
        break
    elif(p2==100):
        break
    pygame.time.delay(1000)
    if(pno==0):
        pygame.draw.rect(setDisplay,black,(700,0,700,700))
        setDisplay.blit(p11,(p11x,p11y))
    else:
        pygame.draw.rect(setDisplay,black,(700,0,700,700))
        setDisplay.blit(p12,(p12x,p12y))
    pygame.display.update()    
    
if(p1==100):
    pygame.draw.rect(setDisplay,black,(700,0,700,700))
    setDisplay.blit(p32,(p32x,p32y))
if(p2==100):
    pygame.draw.rect(setDisplay,black,(700,0,700,700))
    setDisplay.blit(p31,(p31x,p31y))
pygame.display.update()  
