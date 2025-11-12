# Faça um programa que receba 4 alturas e depois realize a soma delas

soma_altura = 0 #valor final da soma que queremos
entradas = 4 #total de entrada de alturas que podemos ter

while entradas > 0:
    altura = float(input("Informe o valor da altura: "))
    soma_altura += altura #aqui eu vou somando já as alturas informadas
    entradas = entradas -1 #faz o caminho inverso, a cada vez que insere uma altura, reduz uma entrada

print(soma_altura)

# enquanto tinha entradas a serem feitas ele foi somando

## outra opção a ser feita é:
# soma_altura = 0
# entradas = 1 

#while entradas <= 4:
#    altura = float(input("Informe o valor da altura: "))
#    soma_altura += altura 
#    entradas += 1

# print(soma_altura)