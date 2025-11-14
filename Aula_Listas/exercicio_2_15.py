## Escreva um programa que receba uma lista de números do usuário e conte quantas vezes um número específico aparece na lista.
## Solicite ao usuário um número e exiba a contagem.

contagem = 0

lista = []

while True:
    numero = input("Informe um número: ")
    if numero == "":
        break
    lista.append(int(numero))

    contagem += 1

print("O total de números informados é igual a ", contagem)
print("Segue lista dos valores informados: ", lista)
