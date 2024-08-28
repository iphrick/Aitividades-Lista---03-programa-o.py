import random
import math
n = 0
while n <= 0:
        n = int(input("Digite o número de elementos na lista (n deve ser positivo): "))
        if n > 0:
            break
        else:
            print("Por favor, digite um número positivo.")

lista = [random.randint(0, 99) for _ in range(n)]
media = sum(lista) / n
lista_ordenada = sorted(lista)
if n % 2 == 0:
    mediana = (lista_ordenada[n // 2 - 1] + lista_ordenada[n // 2]) / 2
else:
    mediana = lista_ordenada[n // 2]
variancia = sum((x - media) ** 2 for x in lista) / n
desvio_padrao = math.sqrt(variancia)
print(f"Lista gerada: {lista}")
print(f"Média: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Variância populacional: {variancia:.2f}")
print(f"Desvio-padrão populacional: {desvio_padrao:.2f}")


