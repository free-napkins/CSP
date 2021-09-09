import turtle as trtl

painter = trtl.Turtle()
painter.penup()
painter.goto(-200, 0)
painter.pendown()
painter.speed(0)

x = -400
y = 0
move_x = 1
move_y = 1
painter.penup()
painter.goto(x,y)
painter.pendown()

repeat = 1

while (repeat > 0):
  while (x < 0):

    while (y < 100):
      x = x + move_x
      y = y + move_y
      painter.goto(x,y)
    move_y = -1
    
    while (y > 0):
      x = x + move_x
      y = y + move_y
      painter.goto(x,y)
    move_y = 1

  x = 0
  y = 0
  move_x = 1
  move_y = 1
  painter.penup()
  painter.goto(x,y)
  painter.pendown()
  while (x > -400):

    while (y > -100):
      x = x - move_x
      y = y - move_y
      painter.goto(x,y)
    move_y = 1
    
    while (y < 0):
      x = x - move_x
      y = y + move_y
      painter.goto(x,y)
    move_y = 1

wn = trtl.Screen()
wn.mainloop()