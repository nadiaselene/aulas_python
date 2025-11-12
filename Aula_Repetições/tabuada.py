## o uso do laço de repetição while exige uma condição para que o código continue rodando

## alterando o código para fazer a tabuada conforme número inserido pelo usuário

## contagem = contagem + 1 é a mesma coisa de contagem += 1

numero = int(input("Informe um número inteiro: "))
contagem = 1
while contagem <= 100:
    print(numero, "x", contagem, "=", numero * contagem)
    contagem = contagem + 1
print("Tabuada finalizada!")