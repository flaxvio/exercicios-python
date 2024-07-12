import math

#cabeçalho
traco = '-'
esp = " "
qnt = 70
qntEsp = esp*13
title = "Será que você consegue acertar o alvo?"
print(traco*qnt)
print(qntEsp, title)
print(traco*qnt)

#localização do centro do alvo
x = 0
y = 0
coordenadas = (x, y)
objetivo = ("Objetivo: Dê as coordenadas X e Y e acerte o centro do alvo!")
print(objetivo)

#coordenadas
digX = input("Digite a coordenada de X: ")
digY = input("Digite a coordenada de Y: ")
x = int(digX)
y = int(digY)
coordenadas = (x, y)
print("Suas coordenadas são: ", coordenadas)

#alvo
alvoRaio = 10

import turtle
turtle.Screen()
t = turtle.Turtle(shape = 'arrow')
t.speed(10)
t.penup()
t.goto(0,-200)
t.pendown()
t.pencolor("red")
t.circle(200)
t.penup()
t.goto(0,-180)
t.pendown()
t.pencolor("black")
t.circle(180)
t.penup()
t.goto(0,-160)
t.pendown()
t.pencolor("red")
t.circle(160)
t.penup()
t.goto(0, -140)
t.pendown()
t.pencolor("black")
t.circle(140)
t.penup()
t.goto(0,-120)
t.down()
t.pencolor("red")
t.circle(120)
t.penup()
t.goto(0, -100)
t.pendown()
t.pencolor("black")
t.circle(100)
t.penup()
t.goto(0,-80)
t.pendown()
t.pencolor("red")
t.circle(80)
t.penup()
t.goto(0,-60)
t.pendown()
t.pencolor("black")
t.circle(60)
t.penup()
t.goto(0,-40)
t.pendown()
t.pencolor("red")
t.circle(40)
t.penup()
t.goto(0,-20)
t.pendown()
t.pencolor("black")
t.circle(20)
t.penup()
t.goto(0,-10)
t.fillcolor("black")
t.begin_fill()
t.pendown()
t.circle(10)
t.end_fill()
t.penup()
t.goto(coordenadas)

#cálculo
distX = x**2
distY = y**2
dist = distX + distY
distancia = math.sqrt(dist)
distancia = int(distancia)
resultado = distancia <= alvoRaio
fonte1 = ("Comic Sans", 20, "italic")

if resultado == True:
    t.write("Parabéns, você acertou o alvo!", False, fonte1)
    print("Parabéns, você acertou o alvo! O raio da sua jogada foi: ", distancia)

else:
    print("Você não acertou, infelizmente! O raio da sua jogada foi: ", distancia)
    t.write("Você não acertou, infelizmente!", False, "center", fonte1)

print()

#repetir
while True:
    digX = input("Digite a coordenada de X (ou 'sair' para encerrar): ")

    if digX.lower() == 'sair':
        print("Encerrando programa!")
        t.clear()
        break

    digY = input("Digite a coordenada de Y: ")
    x = int(digX)
    y = int(digY)
    coordenadas = (x, y)
    print("Suas coordenadas são: ", coordenadas)

    # alvo
    alvoRaio = 10
    t.goto(coordenadas)

    # cálculo
    distX = x ** 2
    distY = y ** 2
    dist = distX + distY
    distancia = math.sqrt(dist)
    distancia = int(distancia)
    resultado = distancia <= alvoRaio
    fonte1 = ("Comic Sans", 20, "italic")

    if resultado == True:
        t.write("Parabéns, você acertou o alvo!", False, fonte1)
        print("Parabéns, você acertou o alvo! O raio da sua jogada foi: ", distancia)

    else:
        print("Você não acertou, infelizmente! O raio da sua jogada foi: ", distancia)
        t.write("Você não acertou, infelizmente!", False, "center", fonte1)

    print()