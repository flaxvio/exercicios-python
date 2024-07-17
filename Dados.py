import turtle

dado = turtle.Turtle(shape = 'circle')
x = 0
y = 200

dado.speed(5)
dado.penup()
dado.goto(x,y)

def desenho_quad():
    for quadrado in range(4):
        dado.pendown()
        dado.forward(200)
        dado.right(90)
        dado.penup()


#ladoA
desenho_quad()
dado.goto(x+100, y-100)
dado.stamp()
dado.penup()

#ladoB
dado.goto(x+200,y)
desenho_quad()
dado.goto(x+250, y-100)
dado.stamp()
dado.goto(x+350, y-100)
dado.stamp()

#ladoC
dado.goto(x+400,y)
desenho_quad()
dado.goto(x+450, y-100)
dado.stamp()
dado.goto(x+500, y-100)
dado.stamp()
dado.goto(x+550, y-100)
dado.stamp()

#ladoD
dado.goto(x,y-200)
desenho_quad()
dado.goto(x+50, y-250)
dado.stamp()
dado.goto(x+50, y-350)
dado.stamp()
dado.goto(x+150, y-250)
dado.stamp()
dado.goto(x+150, y-350)
dado.stamp()

#ladoE
dado.goto(x+200,y-200)
desenho_quad()
dado.goto(x+250, y-250)
dado.stamp()
dado.goto(x+250, y-350)
dado.stamp()
dado.goto(x+300, y-300)
dado.stamp()
dado.goto(x+350, y-250)
dado.stamp()
dado.goto(x+350, y-350)
dado.stamp()

#ladoF
dado.goto(x+400,y-200)
desenho_quad()
dado.goto(x+450, y-250)
dado.stamp()
dado.goto(x+450, y-300)
dado.stamp()
dado.goto(x+450, y-350)
dado.stamp()
dado.goto(x+550, y-250)
dado.stamp()
dado.goto(x+550, y-300)
dado.stamp()
dado.goto(x+550, y-350)
dado.stamp()

dado.hideturtle()
turtle.done()