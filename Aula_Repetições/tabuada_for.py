## Criar a tabuada de um número dentro do laço de repetição for, até 100


numero = int(input("Informe um número: "))
max_contagem = 100

for i in range (1,max_contagem + 1,1):
    print(i, "x", numero, "=", i * numero)