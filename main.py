class Produto:
    def __init__(self, nome, categoria, quantidade_estoque, preco):
        self.nome = nome
        self.categoria = categoria
        self.quantidade_estoque = quantidade_estoque
        self.preco = preco
        
    def __repr__(self):
        return f"Produto [Nome={self.nome}, Categoria={self.categoria}, Quantidade em Estoque={self.quantidade_estoque}, Preço={self.preco}]"

class AgilStore:
    def __init__(self, ):
        self.inventario = {}
        self.contador_id = 1

    def gerar_id_unico(self):
        id_unico = self.contador_id
        self.contador_id += 1
        return id_unico
    
    #adicionar produtos ao inventário
    def adicionar_produtos(self):
        #função para adicionar novos produtos ao inventário
        print("Por favor insira as informações do produto!")

        nome = input("Insira o nome do produto: ")
        categoria = input("Insira a categoria do produto: ")

        while True:
            try:
                quantidade_estoque = int(input("Quantidade em Estoque: "))
                if quantidade_estoque < 0:
                    print("A quantidade deve ser um número inteiro positivo.")
                    continue
                break
            except ValueError:
                print("Por favor, insira um número válido para a quantidade em estoque.")
        
        while True:
            try:
                preco = float(input("Insira o preço: "))
                if preco < 0:
                    print("Insira um preço válido, deve ser um valor positivo.")
                    continue
                break
            except ValueError:
                print("Por favor, insira um valor válido para o preço do produto.")
        
        #gerar id único para o produto
        id_produto = self.gerar_id_unico()

        #criando objeto produto
        produto = Produto(nome, categoria, quantidade_estoque, preco)

        # Armazenar o produto no inventário com o ID gerado
        self.inventario[id_produto] = produto
        print("Produto '{}' adicionado com sucesso! ID: {}" .format(nome, id_produto))

    #lista dos produtos
    def listar_produtos(self):
        if not self.inventario:
            print("Nenhum produto no inventario.\n")
        else:
            print("Inventário atual: ")
            for id_produto, produto in self.inventario.items():
                print("ID: {} -> Produto: {}" .format(id_produto, produto))
    
    def atualizar_produto(self):
        # função para atualizar as informações de um produto existente
        print("\n---> Atualizar Produto <---")
        id_produto = int(input("Digite o ID do produto a ser atualizado: "))

        #verifica se o produto existe no inventário
        if id_produto not in self.inventario:
            print("Produto com ID solicitado não foi encontrado.")
            return
        produto = self.inventario[id_produto]
        print("Produto encontrado: {}" .format(produto))

        #solicitando quais campos o usuário deseja atualizar
        while True:
            print("\nQuais campos você deseja atualizar?")
            print("1. Nome")
            print("2. Categoria")
            print("3. Quantidade em Estoque")
            print("4. Preço")
            print("5. Cancelar atualização")
            opcao_escolhida = input("Escolha uma das opções acima(1-5): ")

            if opcao_escolhida == "1":
                novo_nome = input("Novo nome: ")
                produto.nome = novo_nome
                print("Novo nome atualizado para '{}' com sucesso!" .format(novo_nome))
            elif opcao_escolhida == "2":
                nova_categoria = input("Nova categoria: ")
                produto.nome = novo_nome
                print("Categoria atualizada para '{}' com sucesso!" .format(nova_categoria))
            elif opcao_escolhida == "3":
                while True:
                    try:
                        nova_quantidade = int(input("Digite a nova quantidade em estoque: "))
                        if nova_quantidade < 0:
                            print("A quantidade deve ser um número inteiro positivo.")
                            continue
                        produto.quantidade_estoque = nova_quantidade
                        print("Quantidade em estoque atualizada para {} com sucesso!" .format(nova_quantidade))
                        break
                    except ValueError:
                        print("Por favor, insira um número válido para a quantidade.")
            elif opcao_escolhida == "4":
                while True:
                    try:
                        novo_preco = float(input("Digite o novo preço: "))
                        if novo_preco < 0:
                            print("O novo preço deve ser um valor positivo!")
                            continue
                        produto.preco = novo_preco
                        print("Novo preço atualizado para {} com sucesso!" .format(novo_preco))
                        break
                    except ValueError:
                        print("Por favor, escolha um valor válido para o preço.")
            elif opcao_escolhida == "5":
                print("Sair da atualização")
                break
            else:
                print("Opção inválida, tente novamente!")
        
    def excluir_produto(self):
        print("-->Excluir Produto<--")
        id_produto = int(input("Digite o ID do produto a ser exluído: "))

        #verificando se o produto existe
        if id_produto not in self.inventario:
            print("O produto com o ID solicitado não existe.")
            return
        
        produto = self.inventario[id_produto]
        print("Produto '{}' encontrado" .format(produto))

        #confirmar exclusão
        confirmar = print("Voce tem certeza que deseja excluir o produto '{}' ID: {}? (s/n)" .formart(produto.nome, id_produto)) .strip().lower()
        if confirmar == 's':
            del self.inventario[id_produto]
            print("Produto '{}' ID: {} excluido com sucesso!" .format(produto.nome, id_produto))
        else:
            print("Exclusão cancelada.")
    # Buscar Produto
    def buscar_produto(self):
        print("\n---> Buscar Produto <---")
        tipo_busca = input("Deseja buscar por ID ou por nome? (Digite 'id' ou 'nome'): ").strip().lower()
        if tipo_busca == "id":
                try:
                    id_produto = int(input("Digite o ID do produto: "))
                    if id_produto in self.inventario:
                        print(f"Produto encontrado: {self.inventario[id_produto]}")
                    else:
                        print("Produto com o ID informado não foi encontrado.")
                except ValueError:
                    print("Por favor, insira um ID válido.")
        elif tipo_busca == "nome":
            nome_parcial = input("Digite o nome ou parte do nome do produto: ").lower()
            encontrados = [produto for produto in self.inventario.values() if nome_parcial in produto.nome.lower()]
            if encontrados:
                print("Produtos encontrados:")
                for produto in encontrados:
                    print(produto)
            else:
                print("Nenhum produto com o nome informado foi encontrado.")
        else:
            print("Opção inválida. Escolha 'id' ou 'nome'.")


#função principal
def main():
    agilstore = AgilStore()

    while True:
        print("\n1. Adicionar produto")
        print("2. Listar produtos")
        print("3. Atualizar produto")
        print("4. Excluir produto")
        print("5. Buscar produto")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            agilstore.adicionar_produtos()
        elif opcao == "2":
            agilstore.listar_produtos()
        elif opcao == "3":
            agilstore.atualizar_produto()
        elif opcao == "4":
            agilstore.excluir_produto()
        elif opcao == "5":
            agilstore.buscar_produto()
        elif opcao == "6":
            print("Encerrando aplicação...")
            break
        else:
            print("Opção inválida. Tente novamente escolhendo as opções de 1 a 6!")

if __name__ == "__main__":
    main()