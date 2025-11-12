## Quais números são divisíveis no intervalo de 4-100

contagem = 4

while contagem <= 100:
    resto = contagem % 4
    if resto == 0:
        print(contagem)
    
    contagem += 1    
    
print("Você chegou ao final.")