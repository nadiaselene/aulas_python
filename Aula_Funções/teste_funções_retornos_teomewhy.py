# Vamos criar funções para retornarem cálculos matemáticos entre dois números inseridos no sistema

def soma (a,b):
    """Essa função serve para retornar a soma de dois valores numéricos inputados no sistema.
    """
    return a + b

def subtração (a,b):
    """_Essa função serve para retornar a subtração de dois valores numéricos inputados no sistema.
    """
    return a - b

def divisão (a,b):
    """_Essa função serve para retornar a divisão de dois valores numéricos inputados no sistema.
    """
    return a / b

def multiplicação (a,b):
    """_Essa função serve para retornar a multiplicação de dois valores numéricos inputados no sistema.
    """
    return a * b

def média (a,b):
    """_Essa função serve para retornar a média de dois valores numéricos inputados no sistema.
    """
    return soma(a, b)/2

a = float(input("Informe um valor inteiro para o parâmetro a: "))
b = float(input("Informe um valor inteiro para o parâmetro b: "))

print(f"O valor da soma é {soma(a,b)}")
print(f"O valor da subtração é {subtração(a,b)}")
print(f"O valor da divisão é {divisão(a,b): .2f}")
print(f"O valor da multiplicação é {multiplicação(a,b)}")
print(f"O valor da média é {média(a,b): .2f}")