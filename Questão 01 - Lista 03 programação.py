# Desenvolva um programa que solicite ao usuário dois valores inteiros: o primeiro
# representando a quantidade de listas na matriz e o segundo indicando a quantidade de elementos em
# cada lista. Com base nesses valores, o programa deverá gerar aleatoriamente os elementos da matriz
# (utilizar List Comprehensions), exibir a matriz original e, em seguida, calcular e apresentar a matriz
# transposta.
# A matriz transposta de uma matriz M com m linhas e n colunas é obtida trocando as linhas pelas colunas
# e vice-versa, resultando em uma matriz Mt com n linhas e m colunas.
import random
m = int(input("Digite a quantidade de listas na matriz: "))
n = int(input("Digite a quantidade de elementos em cada lista: "))

matriz = [[random.randint(1, 100) for _ in range(n)] for _ in range(m)]

print("Matriz Original:")
for linha in matriz:
    print(linha)

Mt = [[matriz[j][i] for j in range(m)] for i in range(n)]

print("\nMatriz Transposta:")
for linha in Mt:
    print(linha)
