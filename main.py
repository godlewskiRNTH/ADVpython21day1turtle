from turtle import Turtle, Screen

#Create Turtle and Screen
t: Turtle = Turtle()
s: Screen = Screen()

'''request length from user in console
sideLength: int = int(input('Enter a side length please: '))
'''
#pop up window for input
sideLength: int = s.numinput('Input Window', 'Enter a side length please: ')

'''
#draw a square w/o loop
t.forward(sideLength)
t.right(90)
t.forward(sideLength)
t.right(90)
t.forward(sideLength)
t.right(90)
t.forward(sideLength)
t.right(90)
'''

#draw a simple square with a loop
for item in range(4):
    t.forward(sideLength-10)
    t.right(90)

#draw a square within a square with a loop
while (sideLength > 10):
  for item in range(4):
    t.forward(sideLength-10)
    t.right(90)
  sideLength-=10


#next step




  
