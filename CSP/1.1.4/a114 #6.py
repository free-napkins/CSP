num1 = input("give me a number ")
num2 = input("now give me another number ")
x = int(num1)
y = int(num2)
rem = x % y
repeat = 0
while repeat == 0:
  if (rem != 0):
    print ("these numbers dont divide evenly")
    num1 = input("give me a number ")
    num2 = input("now give me another number ")
    x = int(num1)
    y = int(num2)
    rem = x % y
  else:
    print ("good job")
    repeat = 1