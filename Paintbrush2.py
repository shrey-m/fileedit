#Paintbrush 2 TEST TEST TEST
from pygame import*
from math import*
from random import*

by = 0
putdown = False
canvasRect = Rect(50,50,700,500)
mx,my = 0,0

screen = display.set_mode((800,600))
screen.fill(16777215)
running=True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

    green=(0,255,0)
    omx,omy=mx,my
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    draw.rect(screen,(0,0,0),canvasRect,2)

    radSpray = 10 #Will be determined with scroll in future.

    if mb[0]==1 and canvasRect.collidepoint(mx,my):
        draw.circle(screen,(green),(mx,my),radSpray)

        screen.set_clip(canvasRect)

        xdiff=(mx-omx)
        ydiff=(my-omy)

        distance=hypot(xdiff,ydiff)
        trued=int(distance)

        if distance==0:
            distance=1                       
                    
        for i in range(0,trued):
            x=int(omx+i/distance*xdiff) #take the ratio, and multiply it by xdifference
            y=int(omy+i/distance*ydiff) #take the ratio, and multiply it by xdifference
            draw.circle(screen,(green),(x,y),radSpray)

        for faster in range(0,1):

            putdown=False        

            xSpray=randint(-1*radSpray,radSpray+1)
            ySpray=randint(-1*radSpray,radSpray+1)

            if (xSpray)**2+(ySpray)**2 <= (radSpray)**2:

                while putdown == False:
                
                    if screen.get_at((mx+xSpray,my+ySpray+by)) == green:
                        by+=1
                    else:
                        draw.circle(screen,green,(mx+xSpray,my+ySpray+by),2)
                        putdown=True
                        by = 0
    
        #print(by)
    display.flip()

quit()

