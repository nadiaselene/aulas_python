## inserindo informações para criar um dicionário
## inserir uma nova chave chamada "animais de estimação" no dicionário em que o usuário vai informar o valor

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

dados_nadia["animação de estimação"] = input("Você possui algum animal de estimação? ")

print(dados_nadia)