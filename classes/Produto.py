class Produto:
    def __init__(self, id, nome, preco, data_validade, data_fabricacao, quantidade_estoque):
        self.__id = id
        self.__nome = nome
        self.__preco = preco
        self.__data_validade = data_validade
        self.__data_fabricacao = data_fabricacao
        self.__quantidade_estoque = quantidade_estoque

    #GETS
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_preco(self):
        return self.__preco
    def get_data_validade(self):
        return self.__data_validade
    def get_data_fabricacao(self):
        return self.__data_fabricacao
    def get_quantidade_estoque(self):
        return self.__quantidade_estoque

    #SETS
    def set_id(self, id):
        self.__id = id
    def set_nome(self, nome):
        self.__nome = nome
    def set_preco(self, preco):
        self.__preco = preco
    def set_data_validade(self, data_validade):
        self.__data_validade = data_validade
    def set_data_fabricacao(self, data_fabricacao):
        self.__data_fabricacao = data_fabricacao
    def set_quantidade_estoque(self, quantidade_estoque):
        self.__quantidade_estoque = quantidade_estoque

