import turtle as t

n = 5
t.shape("turtle")
t.color("red")
t.begin_fill()
for x in range(n):
    t.forward(100)
    t.left(360/n)
t.end_fill()