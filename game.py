import turtle
import math
import random
import pygame



file = '/home/dhyanrasberry/dhyan/python/lesson2/bounce.mp3'
pygame.init()
pygame.mixer.init()





wn=turtle.Screen()
wn.bgcolor("black")
wn.bgpic("/home/dhyanrasberry/dhyan/python/lesson2/kbgame-bg.gif")
wn.tracer(3)

mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300,-300)
mypen.pensize(5)
#mypen.pendown()
mypen.color("white")
mypen.hideturtle()
mypen.pendown()


#for side in range(4):
#    mypen.forward(600)
#    mypen.left(90)
#    mypen.forward(600)
#    mypen.left(90)
#    mypen.hideturtle()




player=turtle.Turtle()
player.color("yellow")





player.shape("triangle")
player.penup()
speed = 1


score = 0

#Create goal
maxGoals = 10
goals = []

colors = ["green", "yellow", "red" ,"orange" ,"pink" ,"purple" ,"lightgreen" ,"darkblue" ,"white" ,"blue"] 

for count in range(maxGoals):
    
    goals.append(turtle.Turtle()) 
    goals[count].color(colors[count])
    goals[count].shape("circle")
    goals[count].penup()
    goals[count].speed(0)
    goals[count].setposition(random.randint(-290,290),random.randint(-290,290))

   






def turnleft() :
    player.left(30)  


def turnright() :
    player.right(30)

def increasespeed() :
    global speed 
    speed = speed + 1

def decreasespeed() :
    global speed
    speed = speed - 1

def isCollision(t1,t2):
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if d < 20:
        return True
    else:
         return False   




turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(increasespeed, "Up")
turtle.onkey(decreasespeed,   "Down")      

  

while True:
    player.forward(speed)


    if player.xcor() > 300 or player.xcor() < -300:
        player.right(180)  
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        if(player.xcor() > 300):
            player.setx(300)
            
        if(player.xcor() < -300):
            player.setx(-300)

    if player.ycor() > 300 or player.ycor() < -300:
        player.right(180)    
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
     
        if(player.ycor() > 300):
            player.sety(300)
        if(player.ycor() < -300):
            player.sety(-300)


    
    for count in range(maxGoals):
        goals[count].forward(2)
        
        if goals[count].xcor() > 290 or goals[count].xcor()<-290:
            goals[count].right(180)


        if goals[count].ycor() > 290 or goals[count].ycor()<-290:   
            goals[count].right(180)
            



        if isCollision(player,goals[count]):
            pygame.mixer.music.load('/home/dhyanrasberry/dhyan/python/lesson2/collision.mp3')
            pygame.mixer.music.play()
            goals[count].setposition(random.randint(-100,100), random.randint(-100,100)) 
            goals[count].right(random.randint(0,360))
            score += 1
            #score on screen
            mypen.undo()
            mypen.penup
            mypen.hideturtle
            mypen.setposition(-290,310)
            scoresting = "Score: %s" %score
            mypen.write(scoresting,align="left",font=("Arial",14,"normal"))
     



turtle.done()

