import turtle
from random import randint
#lis object
lis =turtle.Turtle()
lis.color('blue')
lis.shape('turtle')

lis.penup()
lis.goto(-200,200)
lis.pendown()

galina =turtle.Turtle()
galina.color('red')
galina.shape('turtle')


galina.penup()
galina.goto(-200,100)
galina.pendown()

abby =turtle.Turtle()
abby.color('orange')
abby.shape('turtle')

abby.penup()
abby.goto(-200,0)
abby.pendown()

for move in range(200):
    lis.forward(randint(1,5))
    abby.forward(randint(1,5))
    galina.forward(randint(1,5))
turtle.done()
