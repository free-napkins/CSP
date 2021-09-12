#   a116_ladybug.py
import turtle as trtl
ladybug = trtl.Turtle()

# configure legs
ladybug.pensize(5)
legs = 8
leg_length = 60
spacing = 230 / legs
right_legs = 0
left_legs = 0
legloop1 = 0
legloop2 = 0
loop = 0

# draw legs
print("spaceing=", spacing)
while (legloop1 < 3):
  ladybug.penup()
  ladybug.goto(0,-30)
  ladybug.setheading(spacing*right_legs-45)
  ladybug.pendown()
  ladybug.forward(leg_length)
  right_legs = right_legs + 1
  legloop1 = legloop1 + 1
ladybug.penup()
while (legloop2 < 3):
  ladybug.penup
  ladybug.goto(0,-30)
  ladybug.pendown()
  ladybug.setheading(spacing*left_legs-140)
  ladybug.forward(leg_length)
  left_legs = left_legs - 1
  legloop2 = legloop2 + 1

# create ladybug head
ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)

# and body
ladybug.penup()
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 1
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
while (num_dots <= 2 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)
  num_dots = num_dots + 1

  # position next dots
  ypos = ypos + 25
  xpos = xpos + 5
  num_dot = num_dots + 1

ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()