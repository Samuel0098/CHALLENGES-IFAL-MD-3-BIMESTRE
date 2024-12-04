def main():
    blocos = int(input("Qual o tamanho da linha? "))
    if blocos > 0:
        print("🔣" * blocos)
    elif blocos <= 0:
        print("N existe linha negativa amigo ☠")
main()
