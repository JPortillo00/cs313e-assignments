#  File: USFlag.py
#  Description: Draw the US Flag USA! USA! USA!
#  Student's Name: Jairo Portillo
#  Student's UT EID: jep2896
#  Course Name: CS 313E 
#  Unique Number: 51320
#
#  Date Created:9/11/2016
#  Date Last Modified:9/15/2016

def drawWhiteStar(ttl,radius,x,y):
    ttl.penup() 
    ttl.goto(x,y) 
    ttl.pendown()
    size = radius * 1.90211
    angle = 72     
    ttl.left(90)    
    ttl.forward(radius)
    ttl.left(90)
    ttl.color("white")
    ttl.begin_fill()    
    ttl.left(angle)
    ttl.forward(size)
    for side in range(4):        
        ttl.left(angle*2)
        ttl.forward(size)
    ttl.end_fill()
    ttl.penup()
    ttl.right(180-angle)

def drawRectangle(ttl,size,xScale,yScale,lineColor,fillColor):
    x = xScale*size
    y = yScale*size
    ttl.pencolor(lineColor)
    ttl.fillcolor(fillColor)
    ttl.begin_fill()     
    ttl.pendown()
    ttl.forward(x)
    ttl.right(90)
    ttl.forward(y)
    ttl.right(90)
    ttl.forward(x)
    ttl.right(90)
    ttl.forward(y)
    ttl.right(90)
    ttl.end_fill()
    ttl.penup()
    
    
    
    


def main():

    import turtle

    ttl = turtle.Turtle()

    #color
    red = "red"
    white = "white"
    blue = "blue"
    black = "black"

    size = int(input("Enter the height of the Hoist(Vertical Height) for the Flag in pixels:"))
    

    height = size
    width = 1.9 * size
    xMax = width + 200          # (xMax,yMax) size of window
    yMax = height + 200

    #scales
    WtoH = 1.9                  #Width to Height
    CHtoH = 7/13 * 1.0          #Canton Height to Width
    CWtoH = 2/5 * 1.9           #Canton Width to Width
    RoStoH = .5 * 1/13 * 4/5    #Radius of Star to Height
    HoStoH =  1.0/13            #Height of Stripes to Heightz
    
    screen = turtle.Screen()
    screen.setup(xMax, yMax,0,0)
    xInit = -(.5 * xMax - 100) # (xInit,yInit) = Top Right corner of Flag
    yInit = .5 * yMax - 100
    ttl.speed(0)
    ttl.penup()    
    ttl.goto(xInit,yInit)
    ttl.pendown()
    drawRectangle(ttl,size,WtoH,1,black,white) 
    ttl.penup()
    ttl.goto(xInit,-yInit)
    for stripes in range(13):       #Draws and Fills Stripes
        ttl.left(90)
        ttl.forward(HoStoH * height)
        ttl.right(90)
        if stripes % 2 == 1:
            drawRectangle(ttl,size,1.9,HoStoH,black,white)
        else:
            drawRectangle(ttl,size,1.9,HoStoH,black,red)
    ttl.goto(xInit,yInit)
    drawRectangle(ttl,size,CWtoH,CHtoH,black,blue)
    radius = size * RoStoH
    ttl.goto(xInit,yInit)    
    dx = 1.9/30 * size          #Change in x for space between stars
    dy = 7/130 * size           #Change in y for space between stars
    for row in range(1,10):     #Draw and Fills in Stars for Canton
        x = xInit
        y = yInit
        if row % 2 == 1:
            x = x + dx
            y = y - row * dy            
            drawWhiteStar(ttl,radius,x,y)
            for col in range(1,6):
                x = x + 2*dx
                drawWhiteStar(ttl,radius,x,y)
        else:
            x = x + 2*dx
            y = y - row * dy
            drawWhiteStar(ttl,radius,x,y)
            for col in range(1,5):
                x = x + 2*dx
                drawWhiteStar(ttl,radius,x,y)
    
    ttl.goto(xInit,yInit)

main()
