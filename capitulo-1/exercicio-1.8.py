import math

angulo_graus = int(input("Digite um ângulo entre 0 e 360 graus: "))
angulo_radianos = math.radians(angulo_graus)
seno = math.sin(angulo_radianos)
print(f"O seno de {angulo_graus} graus é {seno}")

cosseno = math.cos(angulo_radianos)
print(f"O cosseno de {angulo_graus} graus é {cosseno}")

tangente = math.tan(angulo_radianos)
print(f"O tangente de {angulo_graus} graus é {tangente}")
