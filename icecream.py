import turtle #Imports the things we need for the turtle
wn = turtle.Screen() #Sets the stage

#The turtles
nina = turtle.Turtle() #Creates a turtle, my little Nina
salina = turtle.Turtle()
jose = turtle.Turtle()
#^^^ Initial Setup ^^^

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

#Creates icecream cone
def icecreamCone(turtle):
    cone(turtle)
    icecream(turtle)
    
#Moves turtle out of the way
def move(turtle):
    turtle.penup()
    turtle.setpos(0,0)
    turtle.color("white")
       

    
#^^^ Function Dump ^^^



    
#Getting turtles into position
nina.penup()
salina.penup()
jose.penup()

salina.setpos(-50, 0)
jose.setpos(-25, 30)

#Initializes the functions



for turtle in ["nina", "salina", "jose"]:
    icecreamCone(turtle)

move(nina)
move(salina)
move(jose)

wn.exitonclick()