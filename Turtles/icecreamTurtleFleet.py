"""

Maso283
[03.22.21]

A fleet of three turtles designed to build a starship
with an icecream mystique.

"""

import turtle #Imports the things we need for the turtle
wn = turtle.Screen() #Sets the stage

#The turtles we need
nina = turtle.Turtle() # Mi Nina
salina = turtle.Turtle()# Mi Salina
jose = turtle.Turtle() # Mi Jose
#^^^ Initial Setup ^^^

# Function that makes the icecream.
def icecream(turtle):
    turtle.color("navajowhite")
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(-26)
    turtle.end_fill()
    turtle.penup()
    
    #Creates D R I P
    turtle.penup()
    turtle.setpos(30,0)
    turtle.pensize(5)
    turtle.pendown()
    turtle.setpos(30,-60)

# Function that makes the cone.
def cone(turtle):
    turtle.color("peru")
    turtle.pendown()
    turtle.begin_fill()
    
    turtle.right(75)
    turtle.forward(100)
    turtle.left(150)
    turtle.forward(100)
    turtle.left(15)
    turtle.right(180)
    turtle.circle(-26, 180)
    turtle.end_fill()
    turtle.penup()    

# The function that puts it all together.
def icecreamCone(turtle):
    cone(turtle)
    icecream(turtle)
    
# Moves turtle out of the way once finished.
def move(turtle):
    turtle.penup()
    turtle.setpos(0,0)
    turtle.color("white")
       

    
#^^^ Function Dump ^^^

# Readying turtles' pens
for turtle in [nina, salina, jose]:
    turtle.penup()

# Salina and Jose get into position
salina.setpos(-50, 0)
jose.setpos(-25, 30)

# Fleet's instructions
for turtle in [nina, salina, jose]:
    icecreamCone(turtle)
    move(turtle)
    


wn.exitonclick()
