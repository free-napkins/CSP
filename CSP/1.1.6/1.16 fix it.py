#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name painter is used
painter = trtl.Turtle()
painter.pensize(40)
painter.circle(20)

number_of_legs = 8
length_of_leg = 70
spacing = 360 / number_of_legs
painter.pensize(5)
repeat = 0
while (repeat < number_of_legs):
  painter.goto(0,20)
  painter.setheading(spacing*repeat)
  painter.forward(length_of_leg)
  repeat = repeat + 1
painter.hideturtle()

wn = trtl.Screen()
wn.mainloop()