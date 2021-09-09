import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

x = -150
y = -150

num_floors = 21
floor = 0

while floor > num_floors:
  painter.penup()
  painter.goto(x, y)
  painter.color("gray")
  y = y + 5 
  floor = floor + 1
  rem = floor % 2
  if (rem == 0):
    painter.color("blue")
   
  painter.pendown()
  painter.forward(50)

floor = 0

x = 0
y = -150

repeat = 0

while repeat < 1:
  floor = 0
  while floor < num_floors:
    painter.penup()
    painter.goto(x, y)
    painter.color("gray")
    y = y + 5 
    floor = floor + 1
    rem = floor % 2
    if (rem == 0):
      painter.color("green")
    
    painter.pendown()
    painter.forward(50)

wn = trtl.Screen()
wn.mainloop()