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

#alvo
alvoRaio = 10
print("O raio do alvo é", alvoRaio)

#localização do centro do alvo
x = 0
y = 0
coordenadas = (x, y)
objetivo = "Objetivo: Acerte qualquer lugar do alvo, menos a parede."

print("No plano bidimensional, o centro deste alvo está localizado: ", coordenadas)
print(objetivo)

#coordenadas
digX = input("Digite a coordenada de X: ")
digY = input("Digite a coordenada de Y: ")
x = int(digX)
y = int(digY)
coordenadas = (x, y)
print("Suas coordenadas são: ", coordenadas)

#cálculo
distX = x**2
distY = y**2
dist = distX + distY
distancia = math.sqrt(dist)
distancia = int(distancia)
resultado = distancia <= alvoRaio

if resultado == True:
    print("Parabéns, você acertou o alvo! O raio da sua jogada foi: ", distancia)
else: print("Você não acertou infelizmente! O raio da sua jogada foi: ", distancia)

print()

#repetir
while True:
    digX = input("Digite a coordenada de X (ou 'sair' para encerrar): ")

    if digX.lower() == 'sair':
        print("Encerrando programa!")
        break
    digY = input("Digite a coordenada de Y: ")
    x = int(digX)
    y = int(digY)
    coordenadas = (x, y)
    print("Suas coordenadas são: ", coordenadas)

    # cálculo
    distX = x ** 2
    distY = y ** 2
    dist = distX + distY
    distancia = math.sqrt(dist)
    distancia = int(distancia)
    resultado = distancia <= alvoRaio

    if resultado == True:
        print("Parabéns, você acertou o alvo! O raio da sua jogada foi: ", distancia)
    else:
        print("Você não acertou infelizmente! O raio da sua jogada foi: ", distancia)

    print()