import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.penup()
painter.color("salmon")
painter.pensize(2)

spiral_space = 0

while (spiral_space < 80): 
  painter.color("red")
  painter.goto(0,0)
  painter.right(20)
  painter.forward(40+(spiral_space*2))
  painter.pendown()
  painter.penup()
  spiral_space = spiral_space + 1
  rem = spiral_space % 5
  if (rem == 0):
    painter.color("navy")
    rem = spiral_space % 10
    if (rem == 0):
      painter.color("green")
  painter.pendown()
  painter.circle(10)
  painter.penup()

wn = trtl.Screen()
wn.mainloop()