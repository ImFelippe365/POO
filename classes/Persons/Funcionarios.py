

from datetime import datetime
from classes.Finances.Compra import Compra
from classes.Finances.Conta import Conta
from classes.Produtcs.Item import Item
from classes.Produtcs.Produto import Produto

from colorama import Fore, Style
"""Classe mae, todas as variaçoes de funcionarios herdarão dela"""

from abc import ABC, abstractmethod

class Funcionario(ABC):

    """Metodo costrutor: criando os atributos da classe e inicializando 
    os mesmos, todos privados, endereço e contrato recebem instancias das 
    classes com tal nome"""
    def __init__(self, id, nome, cpf, endereco, sexo, contrato):
        self.__id = id
        self.__nome = nome
        self.__cpf = cpf
        self.__endereco = endereco
        self.__sexo = sexo
        self.__contrato = contrato

    """Metodo abstrato, esse metodo será reescrito em cada uma das classes filha
    ja que o calculo realizado varia para cada tipo de funcionario"""
    @abstractmethod
    def calculo_previdencia_social(self):
        print(f"Imposto a ser pago com base no seu salário: R$ {7.5*1100/100}")

    """"Gets e sets, para caso o uso seja necessario"""

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

""""Classe filha, herdando de funcionario, recebe todos os atributos da classe mae"""
class Atendente(Funcionario):

    """Os atributos herdados são passados no metodo construtor, alem 
    de um atributo proprio dessa classe"""

    def __init__(self, id, nome, cpf, endereco, sexo, contrato):
        """aributos herdados"""
        Funcionario.__init__(self, id, nome, cpf, endereco, sexo, contrato)
        self.__contrato = contrato
        self.__compras_realizadas = {}

    """Metodo reescrito"""
    def calculo_previdencia_social(self):
        print(f"Imposto a ser pago com base no seu salário: R$ {7.5*self.__contrato.get_salario()/100}\n")

    """Exibe os produtos com a quantidade e o valor e também mostra o valor total da compra e o método de pagamento de forma 'estilizada'"""
    def comprovante_de_pagamento(self, compra):
        caracteres = (31-len(" Nota fiscal "))*"="
        print(Fore.YELLOW+Style.BRIGHT+f"{caracteres}x Nota fiscal x{caracteres}")
        print()

        caracteresIniciais = (48-len("NomePreço  Qntd"))*" "
        print(f"Nome{caracteresIniciais}Qntd  Preço")
        for x in compra.get_lista_itens():
            produto = x.get_produto()
            # espaco = len(str(x.get_quantidade()))
            caracteres = (len(produto.get_nome())+len(str("%.2f" % produto.get_preco()))+len(str(x.get_quantidade()))+len("R$ "))
            caracteres = (48-caracteres)*"."
            print(Fore.YELLOW+"{}{}{}  R$ {}".format(produto.get_nome(), caracteres, x.get_quantidade(
            ), str("%.2f" % produto.get_preco()).replace(".", ",")))

        print()
        print(50*"=")

        caracteres = len("Valor total{}R$ ".format("%.2f" % compra.get_valor_total()))
        caracteres = (50-caracteres)*"."
        
        print(Fore.YELLOW + Style.BRIGHT + "Valor total{}R$ {}".format(caracteres,str("%.2f" % compra.get_valor_total()).replace(".", ",")))

        caracteres = len(f"Método de pagamento{compra.get_metodoPagamento()}")
        caracteres = (50-caracteres)*"."
        
        print(Fore.YELLOW + Style.BRIGHT + f"Método de pagamento{caracteres}{compra.get_metodoPagamento()}"+Fore.RESET+Style.RESET_ALL)
        
    '''Metodo onde o atendente recebe um valor do cliente, verifica se e suficiente, da troco caso necesssario e informa quanto de debito ficou restante'''
    def pagar_conta(self, conta, valor):
        conta.set_data_ultimo_pagamento(datetime.now())

        if valor <= conta.get_valor_a_pagar():
            conta.set_valor_a_pagar(conta.get_valor_a_pagar() - valor)
            print("Pagamento realizado\n")
        else:
            conta.set_valor_a_pagar(0)
            print(Fore.GREEN+Style.BRIGHT+f"Conta paga! Troco de R$ {valor - conta.get_valor_a_pagar()}"+Fore.RESET+Style.RESET_ALL)

    """Atraves desse metodo, as compras sao efetuadas, elas sao adicionadas no 
    resgistro de compras realizadas, o processo de pagamento é realizado, com 
    base no metodo de pagamento da compra e os dados que envolvem a realização 
    de compras são atualizados"""
    def editar_produto(self, produto):
        escolha = input("1- Nome \n2- Preço \n3- Data de validade \n4- Data de Fabricação\n\n Escolha: ")
        if(escolha == 1):
            novo_nome = input("Digite o novo nome: ")
            produto.set_nome(novo_nome)
            print("Nome alterado!")
        elif(escolha == 2):
            novo_Preco = input("Digite o novo Preço: ")
            produto.set_preco(novo_Preco)
            print("Preço alterado!")
        elif(escolha == 3):
            nova_dataVal = input("Digite a nova data de validade: ")
            produto.set_data_validade(nova_dataVal)
            print("data de validade alterado!")
        elif(escolha == 4):
            nova_dataFab = input("Digite a nova data de fabricação: ")
            produto._data_fabricacao(nova_dataFab)
            print("Data de fabricação alterado!")
        else:
            print("Opção inválida")
        
    def registrarCompra(self, compra, conta, valor=None):
        conta.set_data_ultima_compra(datetime.now())

        if compra.get_metodoPagamento() == "add_na_conta":
            historico_conta = []
            if self.__compras_realizadas.get(conta.get_titular().get_id()) != None:
                historico_conta = self.__compras_realizadas[conta.get_titular().get_id()]

            historico_conta.append(compra)
            conta.set_valor_a_pagar(
                conta.get_valor_a_pagar() + compra.get_valor_total())

            self.__compras_realizadas[conta.get_titular().get_id()] = historico_conta
        elif compra.get_metodoPagamento() == "Especie":

            if compra.get_valor_total() == valor:
                print("Pagamento realizado, obrigado pela preferência")
            elif compra.get_valor_total() < valor:
                print(Fore.RED+Style.BRIGHT+f"[!] Pagamento insuficiente. O valor da compra é R$ {compra.get_valor_total()}")
            else:
                print(Fore.GREEN+f"Pagamento realizado. Seu troco é de R$ {valor - compra.get_valor_total()}"+Fore.RESET)
        else:
            print(Fore.GREEN+"O pagamento de R$ {} foi realizado com sucesso.".format(str("%.2f" % compra.get_valor_total()).replace(".", ","))+Fore.RESET)

        print(Fore.GREEN+"[✓] Compra registrada")

    def get_compras_realizadas(self):
        return self.__compras_realizadas

""""Classe filha, herdando de funcionario, recebe todos os atributos da classe mae"""
class Entregador(Funcionario):

    """Os atributos herdados são passados no metodo construtor"""

    def __init__(self, id, nome, cpf, endereco, sexo, contrato):
        Funcionario.__init__(self, id, nome, cpf, endereco, sexo, contrato)

    """Metodo sobrescrito"""
    def calculo_previdencia_social(self):
        print(f"Imposto a ser pago com base no seu salário: R$ {9.5*self.__contrato.get_salario()/100}")

    """Metodo onde a entrega dos produtos comprados é realizada, para isso, sao 
    forcecidos os dados da compra, ainda nesse metodo o frete da entrega é calculado"""

    def iniciar_entrega(self, compra):
        print(Fore.YELLOW+"=========================================")
        print("  ↪ Entrega sendo realizada para o endereço: ")
        print(compra.get_conta().get_titular().get_endereco())
        print("========================================="+Fore.RESET)
