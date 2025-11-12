def juros_compostos(valor,taxa,meses):
    """
    Essa função serve para calcular o montante final de uma aplicação (valor),
    a uma determinada taxa de juros %, aplicada durante um tempo também pré determinado em meses.
    
    """
    return valor * (1+taxa) ** meses
        
valor = int(input("Informe o valor a ser aplicado: "))
taxa = float(input("Informe a taxa do rendimento: "))/100
meses = int(input("Informe o período da aplicação em meses: "))

resultado = juros_compostos(valor, taxa, meses)

print(f"O valor final após {meses} meses será de {resultado: .2f} reais.")




