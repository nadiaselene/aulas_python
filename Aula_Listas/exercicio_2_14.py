## Considere a seguinte lista:
## [123, 435, 987, 1984, 2, 19, 423, -178, 320]

## Faça um programa que retorne a posição do menor e do maior valor encontrado:

## O maior valor está na posição x
## O menor valor está na posição y

lista = [123, 435, 987, 1984, 2, 19, 423, -178, 320]

maior_numero = max(lista)
menor_numero = min(lista)

pos_max = lista.index(maior_numero)
pos_min = lista.index(menor_numero)

print("O maior valor está na posição ", pos_max)
print("O menor valor está na posição ", pos_min)