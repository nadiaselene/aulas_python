# Faça um programa que receba 4 alturas e depois realize a soma delas

entradas = 4
soma_altura = 0

for entrada in range (0,entradas + 1):
    altura = float(input("Informe a altura: "))
    entradas -= 1
    soma_altura += altura
    if entradas == 0:
        print(soma_altura)
