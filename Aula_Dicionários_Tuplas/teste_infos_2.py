## inserindo informações para criar um dicionário
## buscar qual a segunda e quarta formação
## buscar a penúltima empresa em que trabalhou, considerando que a primeira que aparece foi a última empresa
## buscar o primeiro cargo, considerando que o primeiro que aparece foi o último

dados_nadia = {
    "nome":"Nadia Selene",
    "idade": 29,
    "filhos":False,
    "Comida":"Hamburguer",
    "estudos":["adm", "finanças", "neurociências", "yoga", "data science"],
    "experiências":[
        {"cargo" : "analista roci", "empresa" : "Banco Mercantil"},
        {"cargo" : "analista cadastro", "empresa" : "Toro Investimentos"},
        {"cargo" : "consultora", "empresa" : "KPMG"},
        {"cargo" : "assistente", "empresa" : "Banco Inter"}
        ]
    }

print("A primeira e segunda formação da ", dados_nadia["nome"], "são", dados_nadia["estudos"][1:4:2])
print("A penúltima empresa em que a ", dados_nadia["nome"], "trabalhou foi", dados_nadia["experiências"][1]["empresa"])
print("O primeiro cargo em que a ", dados_nadia["nome"], "trabalhou foi", dados_nadia["experiências"][3]["cargo"])