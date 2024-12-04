def main():
    blocos = int(input("Qual o tamanho da linha? "))
    x = blocos
    if blocos > 0:
        while x > 0:
            print("🔣" * blocos)
            x -= 1
    elif blocos <= 0:
        print("N existe bloco negativa amigo ☠")
main()
