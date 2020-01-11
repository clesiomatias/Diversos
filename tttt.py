import turtle
import time
import math
import random
 
#background
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Jump")
wn.setup(width = 650, height = 650)
wn.tracer(0)
 
#border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.forward(600)
    border_pen.left(90)
border_pen.hideturtle()
 
#draw platform
platform_pen = turtle.Turtle()
platform_pen.speed(0)
platform_pen.color("white")
platform_pen.penup()
platform_pen.setposition(-257, -270)
platform_pen.pendown()
platform_pen.pensize(3)
platform_pen.forward(514)
platform_pen.hideturtle()
 
#player
player = turtle.Turtle()
player.color("blue")
player.shape("square")
player.penup()
player.speed(0)
player.setposition(0, -0)
player.setheading(90)
grav = -0.1
player.dy = 1
player.dx = 0
 
#set the score 0
score = 0
 
#draw score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s"%score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()
 
#set gravity state
gravstate = "ready"
 
#create enemy
enem = turtle.Turtle()
enem.color("red")
enem.shape("circle")
enem.penup()
enem.speed(0)
q = random.randint(-257, 257)
w = (-257)
enem.setposition(q, w)
enem.setheading(90)
 
#choose a number of particals
number_of_particals = 1000
#create a empty list of particals
particals = []
#add particals to list
for i in range(number_of_particals):
#create particals
    particals.append(turtle.Turtle())
for partical in particals:
    partical.color("red")
    partical.shape("square")
    partical.shapesize(0.2, 0.2)
    partical.penup()
    partical.speed(0)
    h = random.randint(1, 600)
    partical.setheading(h)
    partical.setposition(q, w)
 
#Filler
Filler = turtle.Turtle()
Filler.color("blue")
Filler.shape("circle")
Filler.penup()
Filler.speed(0)
Filler.setposition(-500, -0)
Filler.setheading(90)
 
#set jumpstate
jumpstate = "notready"
 
#set explosion state
es = "notready"
 
#player Jump
def move_up():
    if jumpstate == "ready":
        player.dy += 5
        y = player.ycor()
        y += 5
        player.sety(y)
       
#player movement left
def move_left():
    x = player.xcor()
    x -= 10
    if x < -280:
        x = - 280
    player.setx(x)
   
#player movement right
def move_right():
    x = player.xcor()
    x += 10
    if x > 280:
        x = 280
    player.setx(x)
 
#set up collisions
def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False
 
#key presses
turtle.listen()
turtle.onkey(move_up, "space")
turtle.onkeypress(move_left, "Left")
turtle.onkeypress(move_right, "Right")
 
#main game loop
while True:
 
    #updating screen
    time.sleep(0.02)
    wn.update()
   
    #move Filler
    x = Filler.xcor()
    x -= 50
    Filler.setx(x)
 
    #applay gravity
    if gravstate == "ready":
        player.dy += grav
        y = player.ycor()
        y += player.dy
        player.sety(y)
 
    #make sure player wont fall of the screen
    if player.ycor() <= -257:
        gravstate = "not ready"
        jumpstate = "ready"
        y = -257
        player.sety(y)
 
    #make sure gravity is working in its area
    if player.ycor() > -257:
        jumpstate = "notready"
        gravstate = "ready"
 
    #check for collisions with enemy
    if isCollision(player, enem):
        es = "ready"
 
        #set explosion position
        for partical in particals:
            partical.setposition(q, w)
           
        #move enemy
        q = random.randint(-257, 257)
        w = (-257)
        enem.setposition(q, w)
       
        #update the score
        score += 10
        scorestring = "Score: %s" %score
        score_pen.clear()
        score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
 
    #triger explosion
    if es == "ready":
        for partical in particals:
            a = random.randint(10, 20)
            partical.forward(a)
 
wn.mainloop()
