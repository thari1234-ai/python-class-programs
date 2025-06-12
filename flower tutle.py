import turtle
rose = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("white")
rose.speed(0) 
rose.color("black","black")  
for i in range(360):  
    rose.circle(100)  
    rose.left(2)
rose.hideturtle()
