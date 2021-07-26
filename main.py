from turtle import Turtle, Screen

#Create Turtle and Screen
t: Turtle = Turtle()
s: Screen = Screen()

#draw a square w/o loop
t.forward(150)
t.right(90)
t.forward(150)
t.right(90)
t.forward(150)
t.right(90)
t.forward(150)
t.right(90)

#draw a square with a loop
for item in range(4):
  t.forward(75)
  t.right(90)




  
