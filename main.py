import os
import glob
from parser import parse_input

def mostrar_menu():
    """Exibe o menu principal"""
    print("\n" + "="*50)
    print("        ANALISADOR SINTÁTICO OBSACT")
    print("="*50)
    print("1. Inserir caminho de arquivo")
    print("2. Rodar todos os exemplos")
    print("3. Sair")
    print("="*50)

def processar_arquivo_individual():
    """Processa um arquivo individual"""
    caminho = input("Caminho do arquivo .obsact: ").strip()
    
    if not os.path.exists(caminho):
        print(f"Erro: Arquivo '{caminho}' não encontrado.")
        return
    
    # Extrair o nome do arquivo sem extensão
    nome_arquivo = os.path.splitext(os.path.basename(caminho))[0]
    
    # Criar pasta outputs se não existir
    pasta_outputs = "outputs"
    if not os.path.exists(pasta_outputs):
        os.makedirs(pasta_outputs)
    
    # Definir caminho do arquivo de saída
    arquivo_saida = os.path.join(pasta_outputs, f"{nome_arquivo}.c")
    
    try:
        with open(caminho, "r") as f:
            dados = f.read()
            parse_input(dados, arquivo_saida)
            print(f"Código gerado em {arquivo_saida} com sucesso.")
    except Exception as e:
        print(f"Erro ao processar arquivo: {e}")

def processar_exemplos():
    """Processa múltiplos exemplos baseado em índices"""
    # Listar todos os arquivos .obsact na pasta exemplos
    arquivos_exemplo = sorted(glob.glob("exemplos/teste*.obsact"))
    
    if not arquivos_exemplo:
        print("Nenhum arquivo de exemplo encontrado na pasta 'exemplos'.")
        return
    
    print(f"\nArquivos de exemplo disponíveis:")
    for i, arquivo in enumerate(arquivos_exemplo, 1):
        print(f"{i}. {os.path.basename(arquivo)}")
    
    try:
        entrada_inicial = input(f"\nÍndice inicial (1-{len(arquivos_exemplo)}): ").strip()
        entrada_final = input(f"Índice final (1-{len(arquivos_exemplo)}): ").strip()
        
        # Se o usuário der enter, usar primeiro e último índice
        index_inicial = int(entrada_inicial) if entrada_inicial else 1
        index_final = int(entrada_final) if entrada_final else len(arquivos_exemplo)
        
        if index_inicial < 1 or index_final > len(arquivos_exemplo) or index_inicial > index_final:
            print("Erro: Índices inválidos.")
            return
        
        # Criar pasta outputs se não existir
        pasta_outputs = "outputs"
        if not os.path.exists(pasta_outputs):
            os.makedirs(pasta_outputs)
        
        print(f"\nProcessando exemplos de {index_inicial} a {index_final}...")
        
        for i in range(index_inicial - 1, index_final):
            arquivo = arquivos_exemplo[i]
            nome_arquivo = os.path.splitext(os.path.basename(arquivo))[0]
            arquivo_saida = os.path.join(pasta_outputs, f"{nome_arquivo}.c")
            
            try:
                with open(arquivo, "r") as f:
                    dados = f.read()
                    parse_input(dados, arquivo_saida)
                    print(f"✓ {nome_arquivo}.obsact -> {arquivo_saida}")
            except Exception as e:
                print(f"✗ Erro ao processar {nome_arquivo}.obsact: {e}")
        
        print(f"\nProcessamento concluído! Arquivos gerados na pasta 'outputs'.")
        
    except ValueError:
        print("Erro: Por favor, insira números válidos para os índices.")

def main():
    """Função principal com loop do menu"""
    while True:
        mostrar_menu()
        
        try:
            opcao = input("Escolha uma opção (1-3): ").strip()
            
            if opcao == "1":
                processar_arquivo_individual()
            elif opcao == "2":
                processar_exemplos()
            elif opcao == "3":
                print("Encerrando aplicação...")
                break
            else:
                print("Opção inválida. Por favor, escolha 1, 2 ou 3.")
                
        except KeyboardInterrupt:
            print("\n\nEncerrando aplicação...")
            break
        except Exception as e:
            print(f"Erro inesperado: {e}")

if __name__ == '__main__':
    main()
