import turtle
import os
import math
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

#Draw the border
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.speed(0)
mypen.color("white")

mypen.pensize(3)
for side in range(4):
    mypen.fd(600)
    mypen.lt(90)
mypen.hideturtle()

#Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
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
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200,200)
    y = random.randint(-100,250)
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

bulletspeed = 15

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
        bulletstate = "fire"
        #Move the bullet just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x,y)
        bullet.showturtle()

def isCollision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
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

    #Move the enemy
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)

  
    #Move the enemy back and down 
    if enemy.xcor() > 279:
        y = enemy.ycor()
        y -= 20
        enemyspeed *= -1
        enemy.sety(y)

    if enemy.xcor() < -279:
        y = enemy.ycor()
        y -= 20
        enemyspeed *= -1
        enemy.sety(y)

    #Move the bullet
    y = bullet.ycor()
    y += bulletspeed
    bullet.sety(y) 

    #Check if the bullet has gone to the top
    if bullet.ycor() > 360 :
        bullet.hideturtle()
        bulletstate = "ready"


    #Check for a collision beetween bullet and enemy
    if isCollision(bullet, enemy):
		#Reset the bullet
	    bullet.hideturtle()
	    bulletstate = "ready"
	    bullet.setposition(0, -400)
		#Reset the enemy
	    enemy.setposition(-200, 250)

    if isCollision(player, enemy):
	    player.hideturtle()
	    enemy.hideturtle()
	    print ("Game Over")
	    break    

          



turtle.done()