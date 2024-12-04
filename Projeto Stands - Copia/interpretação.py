def main ():
    num = (input("Digite uma expressão númerica: ")).split()
    calc(num[0], num[1], num[2])

def calc(num1, operador, num2):
    num1 = int(num1)
    num2 = int(num2)

    if operador == "-":
        print(num1 - num2)
    
    elif operador == "+":
        print(num1 + num2)
    
    elif operador == "/":
        print(num1 / num2)
    
    elif operador == "*":
        print(num1 * num2)
    
    else:
        print("Operador Inválido!")
main()