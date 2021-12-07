import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(10)
col = ['red' , 'blue' , 'cyan' , 'orange']
c=0

for i in range(60):
    t.forward(i*10)
    t.right(144)
    t.color(col[c])
    if c==3:
        c = 0
    else:
        c+=1