import turtle
import os
import math
import random
import pygame

pygame.init()
pygame.mixer.init()



wn = turtle.Screen()
wn.bgcolor("black")
wn.bgpic("/home/dhyanrasberry/dhyan/games/space_invaders_background.gif")
wn.tracer(1)


#Register the shapes
turtle.register_shape("/home/dhyanrasberry/dhyan/games/invader.gif")
turtle.register_shape("/home/dhyanrasberry/dhyan/games/player.gif")







wn.title("Space Invaders")

#Draw the border
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.speed(0)
mypen.color("white")

#set the score to 0
score = 0

#Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290,280)
scorestring = "Score: %s" %score
score_pen.write(scorestring,False,align="left",font=("Arial",14,"normal"))
score_pen.hideturtle()


mypen.pensize(3)
for side in range(4):
    mypen.fd(600)
    mypen.lt(90)
mypen.hideturtle()

#Create the player turtle
player = turtle.Turtle()
player.color("brown")
player.shape("/home/dhyanrasberry/dhyan/games/player.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

playerspeed = 15


#Choose a number of enemys
number_of_enemys_ = 5
#Create an empty list of enemys
enemies = []

#Add enemies to the list
for count in range(number_of_enemys_):
    #Create the enemy
    enemies.append(turtle.Turtle())

for enemy in enemies:   
    enemy.color("lightgreen")
    enemy.shape("/home/dhyanrasberry/dhyan/games/invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200,200)
    y = random.randint(200,250)
    enemy.setposition(x,y)

enemyspeed = 3



#Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed = 50 

#Define bullet state
#Ready - Ready to fire
#Fire - bullet is firing
bulletstate = "ready"


#Move the player left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = - 280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    #Declare bulletstate as a global if it needs changed
    global bulletstate
    if bulletstate == "ready":
        pygame.mixer.music.load('/home/dhyanrasberry/dhyan/games/laser.wav')
        pygame.mixer.music.play()
        bulletstate = "fire"
        #Move the bullet just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x,y)
        bullet.showturtle()

def isCollision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 20:
	    return True
    else:
	    return False        



#Create keyboard bindings
turtle.listen()
turtle.onkey(move_left,"Left")

turtle.listen()
turtle.onkey(move_right,"Right")

turtle.listen()
turtle.onkey(fire_bullet,"space")


#Main game loop
while True:
    for enemy in enemies:
        x=enemy.xcor()
        x +=enemyspeed
        enemy.setx(x)
  
        #Move the enemy back and down 
        if enemy.xcor() > 279:
            #Move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 20
                e.sety(y)
            enemyspeed *= -1
        #Change enemy direction      
        if enemy.xcor() < -279:
            #Move all enemyies down
            for e in enemies:
                y = e.ycor()
                y -= 20
                e.sety(y)
                #Change enemy direction
            enemyspeed *= -1
                


    #Check for a collision beetween bullet and enemy
        if isCollision(bullet, enemy):
            pygame.mixer.music.load('/home/dhyanrasberry/dhyan/games/explosion.wav')
            pygame.mixer.music.play()
            #Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            #Reset the enemy
            x = random.randint(-200,200)
            y = random.randint(200,250)
            enemy.setposition(x,y)
            #Update the score
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring,False,align="left",font=("Arial",14,"normal"))
            

            
        for enemy in enemies:
            if player.ycor() >= enemy.ycor():
                player.hideturtle()
                enemy.hideturtle()
                print ("GAME OVER")
                break    

    #Move the bullet
    y = bullet.ycor()
    y += bulletspeed
    bullet.sety(y) 

    #Check if the bullet has gone to the top
    if bullet.ycor() > 360 :
        bullet.hideturtle()
        bulletstate = "ready"


 
          
          
turtle.done()