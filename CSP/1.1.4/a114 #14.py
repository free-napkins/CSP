import turtle as trtl

painter = trtl.Turtle()
painter.shape("circle")
painter.hideturtle()
painter.penup()
painter.speed(0)

y = 200
while (y > -400): 
  y = y - 50
  x = -350
  painter.goto(x,y)
  painter.color("purple")
  painter.stamp()
  while (x < 0):
    x = x + 50
    painter.goto(x,y)
    painter.color("orange")
    painter.stamp()


wn = trtl.Screen()
wn.mainloop()