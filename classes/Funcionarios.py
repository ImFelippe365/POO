
class Funcionario:

    def __init__(self, id, nome, cpf, endereco, sexo, contrato):
        self.__id = id
        self.__nome = nome
        self.__cpf = cpf
        self.__endereco = endereco
        self.__sexo = sexo
        self.__contrato = contrato
    def get_id(self):
        return self.__id
        
    def get_nome(self):
        return self.__nome
    
    def get_cpf(self):
        return self.__cpf
    def get_endereco(self):
        return self.__endereco

    def get_sexo(self):
        return self.__sexo
    def get_contrato(self):
        return self.__contrato
    def set_id(self, novo_id):
        self.__id = novo_id
    def set_nome(self, novo_nome):
        self.__nome = novo_nome
    
    def set_cpf(self, novo_cpf):
        self.__cpf = novo_cpf
        
    def set_endereco(self, novo_endereco):
        self.__endereco = novo_endereco
        
    def set_sexo(self, novo_sexo):
        self.__sexo = novo_sexo
        
    def set_contrato(self, novo_contrato):
        self.__contrato = novo_contrato

class Atendente(Funcionario):

    def __init__(self, id, nome, cpf, endereco, sexo, contrato):
        Funcionario.__init__(self, id, nome, cpf, endereco, sexo, contrato)

    def registrarCompra(compra, conta):
        pass

class Entregador(Funcionario):
    def __init__(self, id, nome, cpf, endereco, sexo, contrato):
        Funcionario.__init__(self, id, nome, cpf, endereco, sexo, contrato)
        
    def iniciar_entrega(self, destino, compra, pagamento = None):
        if (compra.get_valor_total >= 100):
            print("Como o valor da compra foi acima de R$ 100,00, você foi isento da taxa para entrega.")
        else:
            if pagamento == 15:
                print("Entrega em progresso")
            elif pagamento > 15:
                print("Entrega em progresso!\nTroco de R$" + pagamento - 15)
            else:
                print("O valor a ser pago deve ser de R$15.00")
    
    def status(self, local):
        return local
