import random
import math

while True:
    try:
        n = int(input("Digite o valor de n (entre 7 e 60): "))
        if 7 <= n <= 60:
            break
        else:
            print("Por favor, digite um número entre 7 e 60.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

lista_aleatoria = random.sample(range(1, 61), n)

combinacoes = []
lista_aleatoria.sort()
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            for l in range(k+1, n):
                for m in range(l+1, n):
                    for o in range(m+1, n):
                        combinacao = [lista_aleatoria[i], lista_aleatoria[j], lista_aleatoria[k],
                                      lista_aleatoria[l], lista_aleatoria[m], lista_aleatoria[o]]
                        combinacoes.append(combinacao)

with open('numeros_escolhidos.txt', 'w') as file:
    file.write(';'.join(map(str, lista_aleatoria)))

with open('combinacoes.txt', 'w') as file:
    for combinacao in combinacoes:
        file.write(';'.join(map(str, combinacao)) + '\n')

print(f"Números escolhidos: {lista_aleatoria}")

print(f"Número de combinações geradas: {len(combinacoes)}")

total_combinacoes = math.comb(60, 6)
probabilidade_sena = 1 / total_combinacoes
probabilidade_quina = len(combinacoes) / total_combinacoes
probabilidade_quadra = len(combinacoes) / total_combinacoes
print(f"Probabilidade de acertar a sena: {probabilidade_sena:.10f} %")
print(f"Probabilidade de acertar a quina: {probabilidade_quina:.10f} %")
print(f"Probabilidade de acertar a quadra: {probabilidade_quadra:.10f} %")
