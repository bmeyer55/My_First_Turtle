import turtle as trtl
p = trtl.Turtle()

p.speed(6)

#house base
p.fillcolor('#ca2930')
p.begin_fill()
p.forward(200)
p.left(90)
p.forward(150)
p.left(90)
p.forward(100)
p.left(90)
p.forward(70)
p.right(90)
p.forward(100)
p.left(90)
p.forward(80)
p.end_fill()

p.left(90)
p.forward(160)
#door
p.fillcolor('#8c8a80')
p.begin_fill()
p.left(90)
p.forward(40)
p.right(90)
p.forward(20)
p.right(90)
p.forward(40)
p.right(90)
p.forward(20)
p.end_fill()
#windows
p.fillcolor('#000000')
p.begin_fill()
p.right(90)
p.penup()
p.forward(110)
p.pendown()
p.forward(15)
p.right(90)
p.forward(20)
p.right(90)
p.forward(15)
p.right(90)
p.forward(20)
p.end_fill()
p.penup()
p.forward(40)
p.pendown()
p.begin_fill()
p.right(90)
p.forward(15)
p.right(90)
p.forward(20)
p.right(90)
p.forward(15)
p.right(90)
p.forward(20)
p.end_fill()
p.penup()
p.left(90)
p.forward(70)
p.pendown()
p.fillcolor('#000000')
p.begin_fill()
p.forward(15)
p.left(90)
p.forward(20)
p.left(90)
p.forward(15)
p.left(90)
p.forward(20)
p.left(90)
p.forward(15)
p.end_fill()
p.penup()
p.forward(25)
p.right(90)
p.forward(120)
p.right(180)
p.forward(15)
p.pendown()
#garage door
p.fillcolor('#cda766')
p.begin_fill()
p.left(90)
p.forward(55)
p.right(45)
p.forward(10)
p.right(45)
p.forward(60)
p.right(45)
p.forward(10)
p.right(45)
p.forward(55)
p.right(90)
p.forward(74)
p.end_fill()
p.right(90)
p.forward(15)
p.right(90)
p.forward(74)
p.left(90)
p.forward(15)
p.left(90)
p.forward(74)
p.right(90)
p.forward(15)
p.right(90)
p.forward(74)

#tree
p.penup()
p.right(90)
p.forward(45)
p.right(90)
p.forward(200)
p.pendown()
p.right(90)
p.pensize(3)
p.forward(35)
p.pensize(2)
p.forward(35)
p.forward(30)
p.right(180)
p.forward(50)
p.right(140)
p.pensize(1)
p.forward(30)
p.right(180)
p.forward(30)
p.left(140)
p.forward(25)
p.right(30)
p.forward(25)
p.right(180)
p.forward(25)
p.left(30)
p.forward(75)
p.left(90)
p.penup()
p.forward(110)
p.left(90)
p.forward(80)
p.pendown()
#roof
p.fillcolor('#000000')
p.begin_fill()
p.left(90)
p.forward(10)
p.right(160)
p.forward(65)
p.right(46)
p.forward(54)
p.end_fill()
p.penup()
p.left(116)
p.forward(70)
p.pendown()
p.fillcolor('#000000')
p.begin_fill()
p.left(90)
p.forward(10)
p.right(160)
p.forward(65)
p.right(40)
p.forward(66)

p.end_fill()
p.penup()
p.right(180)
p.forward(240)
p.pendown()
#sun
p.fillcolor('yellow')
p.begin_fill()
p.circle(12)
p.end_fill()
p.penup()
p.forward(50)

#gound line
p.left(113)
p.forward(248)
p.left(87)
p.pendown()
p.forward(300)
p.right(180)
p.forward(500)
p.right(180)
p.forward(200)
#snowman
p.circle(11)
p.penup()
p.left(90)
p.forward(21)
p.right(90)
p.pendown()
p.circle(9)
p.left(90)
p.penup()
p.forward(17)
p.right(90)
p.pendown()
p.circle(7)
p.penup()
p.left(90)
p.forward(12)
p.right(90)
p.pendown()
#snowman hat
p.forward(10)
p.right(180)
p.forward(20)
p.right(180)
p.forward(5)
p.fillcolor('#000000')
p.begin_fill()
p.left(90)
p.forward(10)
p.right(90)
p.forward(10)
p.right(90)
p.forward(10)
p.end_fill()
p.penup()
p.forward(5)
p.right(90)
p.pendown()
p.pencolor('orange')
p.pensize(3)
p.forward(5)
#Extra Snowman stuff
p.pensize(2)
p.penup()
p.right(180)
p.forward(1)
p.right(90)
p.forward(12)
p.pendown()
p.pencolor('black')
p.forward(1)
p.penup()
p.forward(3)
p.pendown()
p.forward(1)
p.penup()
p.forward(3)
p.pendown()
p.forward(1)
p.penup()
p.forward(50)


window = trtl.Screen()
window.mainloop()
  