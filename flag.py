from turtle import*
speed(0)
setup(800,400)

penup()
goto(-400,200)
pendown()






colors=["blue","yellow","red","white","orange"]
for x in range(5):
    clr=colors[x % 5]
    color(clr)
    begin_fill()
    forward(800)
    right(90)
    forward(60)
    right(90)
    forward(800)
    end_fill()
    right(180)
    end_fill()


penup()
goto(-400,-101)
pendown()

color("orange")
begin_fill()
forward(160)
right(90)
forward(90)
right(90)
forward(160)
end_fill()
right(180)
forward(160)
end_fill()

color("white")
begin_fill()
forward(160)
left(90)
forward(90)
left(90)
forward(160)
end_fill()
left(180)
forward(160)
end_fill()

color("red")
begin_fill()
forward(160)
right(90)
forward(90)
right(90)
forward(160)
end_fill()
right(180)
forward(160)
end_fill()

color("yellow")
begin_fill()
forward(160)
left(90)
forward(90)
left(90)
forward(160)
end_fill()
left(180)
forward(160)
end_fill()


color("blue")
begin_fill()
forward(160)
right(90)
forward(90)
right(90)
forward(160)
end_fill()
right(180)
forward(160)
end_fill()


done()