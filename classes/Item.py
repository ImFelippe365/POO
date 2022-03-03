class Item:

    def __init__(self, produto, quantidade):
        self.__produto = produto
        self.__quantidade = quantidade

    # GETS
    def get_produto(self):
        return self.__produto
    def get_quantidade(self):
        return self.__quantidade

    # SETS
    def set_produto(self, novo_produto):
        self.__produto = novo_produto
    def set_quantidade(self, nova_quantidade):
        self.__quantidade = nova_quantidade