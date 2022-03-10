class Estoque:
    def __init__(self, produtos=[]):
        self.__produtos = produtos

    def __str__(self):
        return "\n\nProdutos: {}".format(" ".join(map(str, self.__produtos)))

    def adicionarNovoProduto(self, produto):
        self.__produtos.append(produto)

    def reabastecerEstoque(self, produto, quantidade):
        for i in range(len(self.__produtos)):
            if(produto == self.__produtos[i]):
                produto.set_quantidade_estoque(
                    produto.get_quantidade_estoque() + quantidade)
