import random


numero = random.randint(0, 10)

while True:
    palpite = int(input("Insira seu palpite: "))

    if palpite == numero:
        print("Parabéns você acertou!")
        break
    elif (palpite < numero):
        print("Seu palpite foi menor.")
    else:
        print("Se palpite foi maior")
