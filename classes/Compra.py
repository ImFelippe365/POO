
class Compra:

    def __init__(self, id, valor_total, lista_itens = []):
        self.__id = id
        self.__valor_total = float(valor_total)
        self.__lista_itens = []
        
    #GETS
    def get_id(self):
        return self.__id
    def get_lista_itens(self):
        return self.__lista_itens
    def get_valor_total(self):
        return self.__valor_total

    #SETS
    def set_id(self,id):
        self.__id = id
    def set_lista_itens(self,lista_itens):
        self.__lista_itens = lista_itens
    def set_valor_total(self,valor_total):
        self.__valor_total = valor_total

