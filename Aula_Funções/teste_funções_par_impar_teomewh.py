# Declarando uma função para retornar se um valor inserido é par ou ímpar.

def par_ou_ímpar(numero):
    """Essa função não retorna nada, uma vez que se usa apenas do comando 'print', que mostra na tela o resultado.
    """
    if numero % 2 == 0:
        print("O número informado é par!")
    else:
        print("O número informado é ímpar!")

numero = int(input("Informe um número inteiro: "))

par_ou_ímpar(numero)