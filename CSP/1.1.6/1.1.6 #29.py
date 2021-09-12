
import turtle as trtl

# paint body
painter = trtl.Turtle()
painter.pensize(40)
painter.shape("circle")
painter.shapesize(3)
painter.stamp()

# configure legs
painter.pensize(5)
legs = 8
leg_length = 70
spacing = 200 / legs
right_legs = 0
left_legs = 0
legloop1 = 0
legloop2 = 0
loop = 0

# draw legs
print("spaceing=", spacing)
while (legloop1 < 4):
  painter.goto(0,0)
  painter.setheading(spacing*right_legs+45)
  painter.forward(leg_length)
  right_legs = right_legs + 1
  legloop1 = legloop1 + 1
while (legloop2 < 4):
  painter.goto(0,0)
  painter.setheading(spacing*left_legs-65)
  painter.forward(leg_length)
  left_legs = left_legs - 1
  legloop2 = legloop2 + 1

painter.shapesize(0.5)
painter.penup()
painter.goto(-25,15)
painter.pendown()
painter.shape("circle")
painter.color("red")
painter.stamp()
painter.penup()
painter.goto(-28,-2)
painter.stamp()

painter.hideturtle()
wn = trtl.Screen()
wn.mainloop()