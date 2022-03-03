class Estoque:
    def __init__(self, produtos=[]):
        self.__produtos = produtos

    def adicionarNovoProduto(self,produto):
        self.__produtos.append(produto)
    def reabastecerEstoque(self, produto, quantidade):
        for i in range(len(self.__produtos)):
            if(produto == self.__produtos[i]):
                self.__quantidade_estoque += quantidade

