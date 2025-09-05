#აქ მე ვხატავ სახლს Turtle ბიბლიოთეკის გამოყენებით.
from turtle import *

width(3)

#draw a square

forward(200)
left(90)

forward(200)
left(90) 

forward(200)
left(90)

forward(200)

#draw a door
begin_fill()
left(90)
forward(70)

left(90)
forward(110)

right(90)  
forward(60)
  
right(90)
forward(110)
end_fill()

#draw a სახურავი

penup()
goto(200, 200)
pendown()

color("black")
begin_fill()
right(150)
forward(200)

left(120)
forward(200) 
end_fill()

#draw a window

color("black")
penup()
goto(194, 190)
pendown()

right(60)
forward(70)

left(90)
forward(60)

left(90)
forward(70)

left(90)
forward(60)

left(90)
forward(35)

left(90)
forward(60)

left(90)
forward(35)

left(90)
forward(35)

left(90)
forward(70)

#draw a window 2

penup()
goto(6, 190)
pendown()

right(180)
forward(70)

right(90)
forward(60)

right(90)
forward(70)

right(90)
forward(60)

right(90)
forward(35)

right(90)
forward(60)

right(90)
forward(35)

right(90)
forward(35)

right(90)
forward(70)





exitonclick()