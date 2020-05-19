from graphics import*
from time import sleep
from random import randint

#returns a random number between -moveAmount and +moveAmount
def getRandom(moveAmount):
    return randint(-moveAmount,moveAmount)
    

#returns boolean based on the collision of the two balls
def didCollide(ball1,ball2):
    ball1Center = ball1.getCenter()
    ball2Center = ball2.getCenter()
    ball1Xposition = ball1Center.getX()
    ball1Yposition = ball1Center.getY()
    ball2Xposition = ball2Center.getX()
    ball2Yposition = ball2Center.getY()
    ball1Radius = ball1.getRadius()
    ball2Radius = ball2.getRadius()
    distance = (((ball2Xposition-ball1Xposition)**2) + ((ball2Yposition-ball1Yposition)**2))**(1/2)
    radius = ball1Radius+ball2Radius
    if distance <= radius:
        answer = True
        randomColor(ball1)
        randomColor(ball2)
    else:
        answer = False
    return answer

#returns True if ball hits a vertical wall, False otherwise
def hitVertical(ball,win):
    ballCenter = ball.getCenter()
    ballXposition = ballCenter.getX()
    radius = ball.getRadius()
    width = win.getWidth()
    if ballXposition <= radius or ballXposition >= width-radius:
        answer = True
        randomColor(ball)
    else:
        answer = False
    return answer
    
#returns True if ball hits a horizontal wall, False otherwise
def hitHorizontal(ball,win):
    ballCenter = ball.getCenter()
    ballYposition = ballCenter.getY()
    radius = ball.getRadius()
    height = win.getHeight()
    if ballYposition <= radius or ballYposition >= height-radius:
        answer = True
        randomColor(ball)
    else:
        answer = False
    return answer

#returns a random color
def randomColor(circle):
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    circle.setFill(color_rgb(r,g,b))
    

#returns list of new velocities
def collisionV(listV,ball1,ball2,mass1,mass2):
    #Velocities of the balls in x and y direction
    velocityCar1X = listV[0][0]
    velocityCar1Y = listV[0][1]
    velocityCar2X = listV[1][0]
    velocityCar2Y = listV[1][1]
    #location of ball1 and ball2
    ball1Center = ball1.getCenter()
    ball2Center = ball2.getCenter()
    ball1Xposition = ball1Center.getX()
    ball1Yposition = ball1Center.getY()
    ball2Xposition = ball2Center.getX()
    ball2Yposition = ball2Center.getY()
    #find the difference of X's and Y's
    deltaX = ball2Xposition - ball1Xposition
    deltaY = ball2Yposition - ball1Yposition
    #finds distance between ball 1 and ball 2
    distance = ((deltaX**2) + (deltaY**2))**(1/2)
    #finds unit normal vector
    unX = deltaX/distance
    unY = deltaY/distance
    #finds unit tangent vector
    utX = -unY
    utY = unX
    #finds normal scalars
    v1n = (unX*velocityCar1X)+(unY*velocityCar1Y)
    v2n = (unX*velocityCar2X)+(unY*velocityCar2Y)
    #finds tangent scalars
    v1t = (utX*velocityCar1X)+(utY*velocityCar1Y)
    v2t = (utX*velocityCar2X)+(utY*velocityCar2Y)
    #tangental velocities after collision
    v1Prime = v1t
    v2Prime = v2t
    # collision formulas
    v1nPrime = (v1n*(mass1-mass2)+2*mass2*v2n)/(mass1+mass2)
    v2nPrime = (v2n*(mass2-mass1)+2*mass1*v1n)/(mass1+mass2)
    # normal vectors
    v1nPrimeX = v1nPrime * unX
    v1nPrimeY = v1nPrime * unY
    v2nPrimeX = v2nPrime * unX
    v2nPrimeY = v2nPrime * unY
    # tangental vectors
    v1tPrimeX = v1t * utX
    v1tPrimeY = v1t * utY
    v2tPrimeX = v2t * utX
    v2tPrimeY = v2t * utY
    # new velocity vectors
    v1X = v1nPrimeX + v1tPrimeX
    v1Y = v1nPrimeY + v1tPrimeY
    v2X = v2nPrimeX + v2tPrimeX
    v2Y = v2nPrimeY + v2tPrimeY
    return [[v1X,v1Y],[v2X,v2Y]]

def main():
    #create window
    win = GraphWin("Bumper Car Simulation",600,600)
    width = win.getWidth()
    height = win.getHeight()
    # create cars
    radius = 20
    car1 = Circle(Point(radius+30,height/2),radius)
    car2 = Circle(Point(width - (radius+30),height/2),radius)
    randomColor(car1)
    randomColor(car2)
    car1.draw(win)
    car2.draw(win)
    # initial velocities
    v1X = getRandom(15)  
    v1Y = getRandom(15)
    v2X = getRandom(15)
    v2Y = getRandom(15)
    velocityList = [[v1X,v1Y],[v2X,v2Y]]
    # car masses
    car1mass = 1
    car2mass = 1
    # loop that moves cars
    for i in range(500):
        sleep(.04)
        # test if the circles hav hit eachother
        if didCollide(car1,car2):
            velocityList = collisionV(velocityList,car1,car2,car1mass,car2mass)
        if hitVertical(car1,win):
            velocityList[0][0] = -velocityList[0][0]
        if hitVertical(car2,win):
            velocityList[1][0] = -velocityList[1][0]
        if hitHorizontal(car1,win):
            velocityList[0][1] = -velocityList[0][1]
        if hitHorizontal(car2,win):
            velocityList[1][1] = -velocityList[1][1]

        car1.move(velocityList[0][0],velocityList[0][1])
        car2.move(velocityList[1][0],velocityList[1][1])
        
main()      

        
