import turtle

#campo
retangulo = turtle.Turtle()
retangulo.penup()
retangulo.goto(-300, -150)
retangulo.pendown()

retangulo.fillcolor("orange")
retangulo.begin_fill()

for i in range(2):
    retangulo.forward(600)
    retangulo.left(90)
    retangulo.forward(300)
    retangulo.left(90)

retangulo.end_fill()


#divisão do campo
retangulo.penup()
retangulo.goto(0, 150)
retangulo.right(90)
retangulo.pendown()
retangulo.forward(300)
retangulo.penup()
retangulo.hideturtle()

#centro
circuloCentral = turtle.Turtle()
circuloCentral.penup()
circuloCentral.goto(0, -50)
circuloCentral.pendown()
circuloCentral.circle(50)
circuloCentral.penup()
circuloCentral.hideturtle()

#lado direito

#lateral primária
circuloDireito = turtle.Turtle()
circuloDireito.penup()
circuloDireito.goto(200, 50)
circuloDireito.pendown()
circuloDireito.left(180)
circuloDireito.circle(50,180)
circuloDireito.right(10)
circuloDireito.forward(100)
circuloDireito.left(100)
circuloDireito.penup()
circuloDireito.forward(135)
circuloDireito.left(100)
circuloDireito.pendown()
circuloDireito.forward(100)
circuloDireito.left(80)
circuloDireito.forward(100)
circuloDireito.penup()

#lateral secundária
circuloDireito.goto(300, 125)
circuloDireito.right(90)
circuloDireito.pendown()
circuloDireito.forward(80)
circuloDireito.circle(125, 180)
circuloDireito.forward(80)
circuloDireito.hideturtle()

#cesta
cestaDireita = turtle.Turtle()
cestaDireita.penup()
cestaDireita.goto(275, 25)
cestaDireita.right(90)
cestaDireita.pendown()
cestaDireita.forward(50)
cestaDireita.penup()
cestaDireita.goto(275, 0)
cestaDireita.right(90)
cestaDireita.pendown()
cestaDireita.forward(12)
cestaDireita.right(90)
cestaDireita.circle(10)
cestaDireita.hideturtle()

#esquerda

#lateral primária
circuloEsquerdo = turtle.Turtle()
circuloEsquerdo.penup()
circuloEsquerdo.goto(-200, -50)
circuloEsquerdo.pendown()
circuloEsquerdo.right(360)
circuloEsquerdo.circle(50,180)
circuloEsquerdo.right(10)
circuloEsquerdo.forward(100)
circuloEsquerdo.left(100)
circuloEsquerdo.penup()
circuloEsquerdo.forward(135)
circuloEsquerdo.left(100)
circuloEsquerdo.pendown()
circuloEsquerdo.forward(100)
circuloEsquerdo.left(80)
circuloEsquerdo.forward(100)
circuloEsquerdo.penup()

#lateral secundária
circuloEsquerdo.goto(-300, -125)
circuloEsquerdo.right(90)
circuloEsquerdo.pendown()
circuloEsquerdo.forward(80)
circuloEsquerdo.circle(125, 180)
circuloEsquerdo.forward(80)
circuloEsquerdo.hideturtle()

#Cesta
cestaEsquerda = turtle.Turtle()
cestaEsquerda.penup()
cestaEsquerda.goto(-275, 25)
cestaEsquerda.right(90)
cestaEsquerda.pendown()
cestaEsquerda.forward(50)
cestaEsquerda.penup()
cestaEsquerda.goto(-275, 0)
cestaEsquerda.left(90)
cestaEsquerda.pendown()
cestaEsquerda.forward(12)
cestaEsquerda.right(90)
cestaEsquerda.circle(10)
cestaEsquerda.hideturtle()

turtle.done()
