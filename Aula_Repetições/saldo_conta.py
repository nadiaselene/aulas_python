# Programa que recebe saldo em conta sem limite de entradas, mas quando o usuário apertar enter sem nenhum valor, exibe a soma de todos os valores

saldo = 0 #começa com o saldo zerado

while True:
    entrada = input("Informe o saldo: ")
    
    if entrada == "":
        break
    saldo += float(entrada)

print("O valor total é igual a ", saldo)