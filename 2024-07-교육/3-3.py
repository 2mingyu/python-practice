import turtle as t

t.shape("turtle")

n = 100
t.bgcolor("black")
t.color("green")
t.speed(0)

for x in range(n):
  t.forward(x)
  t.left(45)