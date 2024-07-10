import math

#cabeçalho
traco = '-'
esp = " "
qnt = 90
qntEsp = esp*30
title = "Quantos metros consigo subir?"
objetivo = ("Uma escada encostada diretamente na parede não cairá se a sua angulação for menor que 90º.\nPortanto, o quão alto eu consigo subir dando a angulação e o comprimento da escada?")

print(traco*qnt)
print(qntEsp, title)
print(traco*qnt)
print(objetivo)
print()

#vairáveis de comprimento e angulação
altura = int(input("Digite o comprimento da escada: "))
angulo = int(input("Digite o ângulo da escada: "))
print()

#conversão de angulo para raio
radiano = ((math.pi*angulo)/180)

#cáculo
comprimento = int((altura*(math.sin(radiano))))

#resultado
print("Você conseguirá subir aproximadamente:", comprimento,"metros")
print ()

while True:
    altura = input("Digite o comprimento da escada (ou 'sair' para encerrar o programa): ")
    if altura.lower() == 'sair':
        print("Encerrando programa!")
        break

    altura = int(altura)
    angulo = int(input("Digite o ângulo da escada: "))
    print()

    # conversão de angulo para raio
    radiano = ((math.pi * angulo) / 180)

    # cáculo
    comprimento = int((altura * (math.sin(radiano))))

    # resultado
    print("Você conseguirá subir aproximadamente:", comprimento, "metros")
    print()