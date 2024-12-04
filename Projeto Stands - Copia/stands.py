stands = {
    "STAR PLATINUM" : {
        "Úsuario" : "Jotaro Kujo",
        "Primeira Aparição" : "Parte 3",
        "Classe" : "Stand Curto-Alcance",
        "Habilidade Ult" : "The World",
        "Inimigo Principal" : "Dio Brando"
        
    },
   "SILVER CHARIOT" : {
        "Úsuario" : "Jean Pierre Polnareff",
        "Primeira Aparição" : "Parte 3",
        "Classe" : "Stand Curto-Alcance",
        "Habilidade Ult" : "Sword Launch",
        "Inimigo Principal" : "J. Geil"
        
    },
    "THE WORLD" : {
        "Úsuario" : "Dio Brando",
        "Primeira Aparição" : "Parte 3",
        "Classe" : "Stand Curto-Alcance",
        "Habilidade Ult" : "Time Stop",
        "Inimigo Principal" : "Familia Joestar"
        
    },
    "CRAZY DIAMOND" : {
        "Úsuario" : "Josuke Higashikata",
        "Primeira Aparição" : "Parte 4",
        "Classe" : "Stand Curto-Alcance",
        "Habilidade Ult" : "Restauração",
        "Inimigo Principal" : "Rohan Kishibe"
        
    },
    "KILLER QUEEN" : {
        "Úsuario" : "Yoshikage Kira",
        "Primeira Aparição" : "Parte 4",
        "Classe" : "Stand Curto-Alcance",
        "Habilidade Ult" : "Transmutação em Bomba Ar",
        "Inimigo Principal" : "Diamond is Unbreakable"
        
    },
    "HEAVENS DOOR" : {
        "Úsuario" : "Rohan Kishibe",
        "Primeira Aparição" : "Parte 4",
        "Classe" : "Stand Curto-Alcance",
        "Habilidade Ult" : "Comandos Escritos",
        "Inimigo Principal" : "Indisponivel..."
        
    },
    "GOLD EXPERIENCE" : {
        "Úsuario" : "Giorno Giovanna",
        "Primeira Aparição" : "Parte 5",
        "Classe" : "Stand Curto-Alcance",
        "Habilidade Ult" : "Sentidos Aguçados",
        "Inimigo Principal" : "Abbacchio"
        
    },
    "KING CRIMSON" : {
        "Úsuario" : "Diavolo",
        "Primeira Aparição" : "Parte 5",
        "Classe" : "Stand Curto-Alcance",
        "Habilidade Ult" : "Apagamento de Tempo",
        "Inimigo Principal" : "Giorno Giovanna"
        
    },
    "STONE FREE" : {
        "Úsuario" : "Jolyne Cujoh",
        "Primeira Aparição" : "Parte 6",
        "Classe" : "Stand Curto-Alcance",
        "Habilidade Ult" : "Apagamento de Tempo",
        "Inimigo Principal" : "Enrico Pucci"
        
    },
    "MADE IN HEAVEN" : {
        "Úsuario" : "Enrico Pucci",
        "Primeira Aparição" : "Parte 6",
        "Classe" : "Stand Curto-Alcance",
        "Habilidade Ult" : "Aceleração do Tempo",
        "Inimigo Principal" : "Jolyne Cujoh"
        
    },
}

def exibir(nome):
    if nome in stands:
        stand = stands[nome]
        print(f"\nÚsuario: {stand['Úsuario']}")
        print(f"Primeira Aparição: {stand['Primeira Aparição']}")
        print(f"Classe: {stand['Classe']}")
        print(f"Habilidade Ult: {stand['Habilidade Ult']}")
        print(f"Inimigo Principal: {stand['Inimigo Principal']}")
    else:
        print("Stand não detectado")
def pesquisar_stands():
    nome_stand = input("\nProcurar Stand no radar, Digite o nome: ").upper()
    exibir(nome_stand)




def perguntar_continuar():
    resposta = input("\nDeseja continuar a procurar stands no radar? (sim/não): ").lower()
    if resposta == "sim":
        return True
    elif resposta == "não":
        return False
    else:
        print("Resposta Invalida!!")
        return perguntar_continuar()

def radar():
    while True:
        pesquisar_stands()
        continuar = perguntar_continuar()
        if not continuar:
            print("\nRadar Desligado!")
            break
radar()