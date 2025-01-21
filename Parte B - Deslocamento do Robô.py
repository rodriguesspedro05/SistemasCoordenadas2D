# Parte B - Deslocamento do Robô --- Feito por: Pedro Henrique de A. Rodrigues :)

x_origem = int(input("Digite a coordenada X do ponto de origem A do robô: "))
y_origem = int(input("Digite a coordenada Y do ponto de origem A do robô: "))

tempo = int(input("Digite por quanto tempo o robô irá caminhar: "))

# uma unidade para cima, duas para direita, repetindo a sequência até o final da caminhada
u_cima = tempo//3
u_direita = (tempo//3)*2


# adequar a contagem caso haja resto, sendo que se for 1 entao o robô se move para cima mais um passo; 
# e caso o resto seja 2, sobrou 2 intervalos, entao o robô deverá mover para cima por mais um passo e para a direita por mais dois passos
resto = tempo % 3

if resto == 1:
    u_cima += 1

elif resto == 2:
    u_cima += 1
    u_direita += 2

#calculando as coordenadas do robô
x_final = x_origem + u_direita
y_final = y_origem + u_cima

print(f"ao final da caminhada o robô estará no ponto ({x_final},{y_final}) do plano cartesiano.")