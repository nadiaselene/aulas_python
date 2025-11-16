## Solicite ao usuário o nome de uma fruta e exiba o preço correspondente.
## Maçã: R$1,50, Banana: R$2,75, Uva: R$1,90, Pera: R$1,25, Laranja: R$0,65, Limão: R$1,25, Goiaba: R$2,15, Abacaxi: R$3,20, Jaca: R$5,80

tabela_preços = {"Maçã" : "R$1,50", "Banana" : "R$2,75", "Uva" : "R$1,90", 
                "Pera" : "R$1,25", "Laranja" : "R$0,65", "Limão" : "R$1,25",
                "Goiaba" : "R$2,15", "Abacaxi" : "R$3,20", "Jaca" : "R$5,80"}

fruta = input("Gentileza informar qual fruta você deseja: ")

if fruta in tabela_preços:
    print("O valor da fruta", fruta, "é igual a", tabela_preços[fruta])
else:
    print("Não existe essa fruta no estoque.")