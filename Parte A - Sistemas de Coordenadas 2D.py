# Parte A - Sistemas de Coordenadas 2D --- Feito por: Pedro Henrique de A. Rodrigues :)

import math

origem_x, origem_y = input("Digite as coordenadas (x y) da origem transladada: ").split()
origem_x = int(origem_x)
origem_y = int(origem_y)

n = int(input("Digite a quantidade de pontos que deverão ser lidos: "))

# armazenar os pontos nos quadrantes para mostrar na saída
quadrante1 = quadrante2 = quadrante3 = quadrante4 = 0

menor_distancia = maior_distancia = None
menor_distancia_ponto = maior_distancia_ponto = None

for i in range(n):
    x, y = input(f"Digite as coordenadas do ponto (x y): ").split()
    x = int(x)
    y = int(y)

    if x > origem_x and y > origem_y:
        print(f"O ponto ({x},{y}) está no 1º quadrante")
        quadrante1 += 1

    elif x < origem_x and y > origem_y:
        print(f"O ponto ({x},{y}) está no 2º quadrante")
        quadrante2 += 1

    elif x < origem_x and y < origem_y:
        print(f"O ponto ({x},{y}) está no 3º quadrante")
        quadrante3 += 1

    elif x > origem_x and y < origem_y:
        print(f"O ponto ({x},{y}) está no 4º quadrante")
        quadrante4 += 1

    else:
        print(f"O ponto ({x},{y}) está sobre o eixo de coordenadas")

    # fórmula da distância euclidiana
    distancia = math.sqrt((x - origem_x) ** 2 + (y - origem_y) ** 2)

    # atualização tanto da menor distância euclidiana quanto da maior, substituindo os pontos anteriores caso os valores sejam verdade no if
    if menor_distancia is None or distancia < menor_distancia:
        menor_distancia = distancia
        menor_distancia_ponto = (x, y)

    if maior_distancia is None or distancia > maior_distancia:
        maior_distancia = distancia
        maior_distancia_ponto = (x, y)

print(f"O ponto {menor_distancia_ponto} é o mais próximo, distância = {round(menor_distancia, 2)}")
print(f"O ponto {maior_distancia_ponto} é o mais longe, distância = {round(maior_distancia, 2)}")
print(f"Existe(m) {quadrante1} ponto(s) no 1º quadrante, {quadrante2} no 2º quadrante, {quadrante3} no 3º quadrante e {quadrante4} no 4º quadrante.")

