from parser import parse_input

if __name__ == '__main__':
    caminho = input("Caminho do arquivo .obsact: ").strip()
    with open(caminho, "r") as f:
        dados = f.read()
        parse_input(dados)
        print("Código gerado em output.c com sucesso.")
