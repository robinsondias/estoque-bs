print("ARQUIVO CORRETO RODANDO")

from produto import Produto
from utils import salvar_estoque, carregar_estoque

# Lista para armazenar os produtos cadastrados
estoque = carregar_estoque()

while True:
    print("\nESTOQUE")
    print("1 - Cadastrar Produto")
    print("2 - Listar Produtos")
    print("3 - Sair")

    opcao = input("Escolha uma Opção: ").strip()
    print("DEBUG:", repr(opcao))

    if opcao == "1":
        print("Entrou na opção 1")

        nome = input("Digite o nome do produto: ")

        try:
            quantidade = int(input("Digite a quantidade: "))
        except ValueError:
            print("Quantidade inválida! Use apenas números.")
            continue

        validade = input("Digite a validade (dd/mm/aaaa): ")
        categoria = input("Digite a categoria: ")

        produto = Produto(nome, quantidade, validade, categoria)

        estoque.append(produto)
        salvar_estoque(estoque)

        print("Produto cadastrado com sucesso!")
        print("Arquivo salvo!")

    elif opcao == "2":
        print("\nLISTA DE PRODUTOS")

        if len(estoque) == 0:
            print("Nenhum produto cadastrado.")
        else:
            for p in estoque:
                print(
                    f"Nome: {p.nome} | Quantidade: {p.quantidade} | Validade: {p.validade} | Categoria: {p.categoria}"
                )

    elif opcao == "3":
        salvar_estoque(estoque)
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida. Tente novamente!")
