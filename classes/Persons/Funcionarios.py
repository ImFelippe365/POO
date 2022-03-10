from datetime import datetime
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
        self.__compras_realizadas = {}
    
    def pagar_conta(self, conta, valor):
        conta.set_data_ultimo_pagamento(datetime.now())
        if valor <= conta.get__valor_a_pagar():
            conta.set__valor_a_pagar(conta.get__valor_a_pagar() - valor)
            print("Pagamento realizado")
        else: 
            conta.set__valor_a_pagar(0)
            print("Conta paga! Troco de R$" + valor - conta.get__valor_a_pagar())
        

    def registrarCompra(self, compra, conta, valor=None):
        self.__compras_realizadas[conta.get_titular()] = compra 
        conta.set_data_ultima_compra(datetime.now())
        if compra.get_metodoPagamento() == "add_na_conta":
            historico_conta = []

            if self.__compras_realizadas.has_key(conta):
                historico_conta = self.__compras_realizadas[conta]

            historico_conta.append(compra)
            conta.set_valor_a_pagar(conta.get_valor_a_pagar() + compra.get_valor_total())
            
        elif compra.get_metodoPagamento() == "Espécie":
            if compra.get_valor_total() == valor:
                print("Pagamento realizado, obrigado pela preferência")
            elif compra.get_valor_total() < valor:
                print(f"Pagamento insuficiente. O valor da compra é R$ {compra.get_valor_total()}")
            else:
                print(f"Pagamento realizado. Seu troco é de R$ {valor - compra.get_valor_total()}")
        else:
            print(f"O pagamento de R$ {compra.get_valor_total()} foi realizado com sucesso.\n")


        print("Compra registrada")
        print(self.__compras_realizadas)

class Entregador(Funcionario):
    def __init__(self, id, nome, cpf, endereco, sexo, contrato):
        Funcionario.__init__(self, id, nome, cpf, endereco, sexo, contrato)
        
    def iniciar_entrega(self, destino, compra, pagamento = None):
        print("Entrega sendo realizada para o endereço: ")
        print(destino)

        if (compra.get_valor_total >= 100):
            print("Como o valor da compra foi acima de R$ 100,00, você não precisa pagar uma taxa de entrega.")
        else:
            if pagamento == 15:
                print("Entrega em progresso")
            elif pagamento > 15:
                print("Entrega em progresso!\nTroco de R$" + pagamento - 15)
            else:
                print("O valor a ser pago deve ser de R$15.00")

    
    def status(self, local):
        return local
