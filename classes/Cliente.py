from datetime import datetime

class Cliente:

    def __init__(self, id, nome, data_nascimento, endereco):
        self.__id = id
        self.__nome = nome
        self.__data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
        self.__endereco = endereco

    # GETS
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_data_nascimento(self):
        return self.__data_nascimento
    def get_endereco(self):
        return self.__edereco

    # SETS
    def set_id(self, id):
        self.__id = id
    def set_nome(self, nome):
        self.__nome = nome
    def set_data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento
    def set_endereco(self, endereco):
        self.__endereco = endereco

    def realizar_compra(self, compra, atendente):
        atendente.registrarCompra(compra, self.__conta)
        print("Compra realizada! Obrigado pela preferencia.")
    
    def pagar_valor(self, valor):
        if valor <= self.__conta.get__valor_a_pagar():
            self.__conta.set__valor_a_pagar(self.__conta.get__valor_a_pagar() - valor)
            print("Pagamento realizado")
        else: 
            self.__conta.set__valor_a_pagar(0)
            print("Conta paga! Troco de R$" + valor - self.__conta.get__valor_a_pagar())
