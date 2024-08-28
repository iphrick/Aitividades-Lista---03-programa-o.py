# Faça um programa que leia dois valores: x e n (x e n deverão ser solicitados ao
# usuário), onde x é a quantidade de elementos que a lista deverá armazenar positivo e n serão os valores
# inteiros a serem inseridos na lista, o programa deve terminar a leitura dos números quando for informado
# o valor 0 (o valor 0 não deverá fazer parte da lista). A lista só deverá armazenar os x menores números
# informados
list = []
x = int(input("Informe a quantidade de elementos na lista: "))

while True:
 n = int(input("Informe um valor: "))
 if n == 0: 
  break
 if len(list) < x:
  list.append(n)
 elif n < max(list):
  list.remove(max(list))
  list.append (n)
 print(sorted(list))
print(sorted(list))
