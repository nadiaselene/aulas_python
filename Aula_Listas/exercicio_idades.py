## pedir para o usuário informar idades para compor uma lista
## enqunto ele inserir números, a lista continua
## caso ele aperte enter sem digitar, a lista finaliza
## traga também a média e a soma das idades


idades = []

while True:
    nova_idade = input ("Informe uma idade: ")
    if nova_idade == "":
        break
    idades.append(int(nova_idade))

qtd_idades = len(idades)
soma_idades = sum(idades)
media = soma_idades/qtd_idades

print("As idades inseridas na lista foram: ", idades)
print("A soma total das idades é igual a: ",  soma_idades)
print("A média das idades é igual a :", media)
