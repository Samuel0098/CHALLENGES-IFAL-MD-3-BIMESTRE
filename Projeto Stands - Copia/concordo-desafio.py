def main ():
    resposta = input("Você concorda? ").lower()
    concordo(resposta)

def concordo(resposta):
    if resposta == "sim" or resposta == "s" or resposta == "si":
        print("Eu concordo")
    elif resposta == "n" or resposta == "nao" or resposta == "não":
        print("Eu não concordo")

main() 









#print("Olá\rMundo")

#resposta = input("Qual seu nome? ")

#def saudacao(nome):
   # print(f"Olá, {nome}!")

#saudacao(resposta)