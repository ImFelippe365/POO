from datetime import datetime
from mimetypes import init


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


class Cliente:

    def __init__(self, id, nome, data_nascimento, endereco, conta):
        self.__id = id
        self.__nome = nome
        self.__data_nascimento = datetime.strptime(
        data_nascimento, '%d/%m/%Y').date()
        self.__endereco = endereco
        self.__conta = conta

    # GETS
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_data_nascimento(self):
        return self.__data_nascimento
    def get_endereco(self):
        return self.__edereco
    def get_conta(self):
        return self.__conta

    # SETS
    def set_id(self, id):
        self.__id = id
    def set_nome(self, nome):
        self.__nome = nome
    def set_data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento
    def set_endereco(self, endereco):
        self.__endereco = endereco
    def set_conta(self, conta):
        self.__conta = conta

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


class Conta:

    def __init__(self, titular, valor_a_pagar, data_ultimo_pagamento, data_ultima_compra):
        self.__titular = titular
        self.__valor_a_pagar = valor_a_pagar
        self.__data_ultimo_pagamento = datetime.strptime(data_ultimo_pagamento, '%d/%m/%Y').date()
        self.__data_ultima_compra = datetime.strptime(data_ultima_compra, '%d/%m/%Y').date()
        
    # GETS
    def get_titular(self):
        return self.__titular
    def get_valor_a_pagar(self):
        return self.__valor_a_pagar
    def get_data_ultimo_pagamento(self):
        return self.__data_ultimo_pagamento
    def get_data_ultima_compra(self):
        return self.__data_ultima_compra
  

    # SETS
    def set_titular(self, nova_titular):
        self.__titular = nova_titular
    def set_valor_a_pagar(self, nova_valor_a_pagar):
        self.__valor_a_pagar = nova_valor_a_pagar    
    def set_data_ultimo_pagamento(self, nova_data_ultimo_pagamento):
        self.__data_ultimo_pagamento = nova_data_ultimo_pagamento
    def set_data_ultima_compra(self, nova_data_ultima_compra):
        self.__data_ultima_compra = nova_data_ultima_compra

class Compra:

    def __init__(self, id, lista_itens, valor_total):
        self.__id = id
        self.__lista_itens = []
        self.__valor_total = float(valor_total)
        
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

class Contrato:

    def __init__(self, id, data_inicio, data_fim, salario, horario_entrada, horario_saida):
        self.__id = id
        self.__data_inicio = datetime.strptime(data_inicio, '%d/%m/%Y').date()
        self.__data_fim = datetime.strptime(data_fim, '%d/%m/%Y').date()
        self.__salario = salario
        self.__horario_entrada = datetime.strptime(horario_entrada, '%H/%M').date()
        self.__horario_saida = datetime.strptime(horario_saida, '%H/%M').date()

    # GETS
    def get_id(self):
        return self.__id
    def get_data_inicio(self):
        return self.__data_inicio
    def get_data_fim(self):
        return self.__data_fim
    def get_salario(self):
        return self.__salario
    def get_horario_entrada(self):
        return self.__horario_entrada
    def get_horario_saida(self):
        return self.__horario_saida

    # SETS
    def set_id(self, id):
        self.__id = id
    def set_data_inicio(self, data_inicio):
        self.__data_inicio = data_inicio
    def set_data_fim(self, data_fim):
        self.__data_fim = data_fim
    def set_salario(self, salario):
        self.__salario = salario
    def set_horario_entrada(self, horario_entrada):
        self.__horario_entrada = horario_entrada
    def set_horario_saida(self, horario_saida):
        self.__horario_saida = horario_saida
    def reajustarSalario(self, novoSalario):
        self.__salario = novoSalario


class Endereco:

    def __init__(self, rua, numero, bairro, cep, cidade, estado):
        self.__rua = rua
        self.__numero = numero
        self.__bairro = bairro
        self.__cep = cep
        self.__cidade = cidade
        self.__estado = estado

    # GETS
    def get_rua(self):
        return self.__rua
    def get_numero(self):
        return self.__numero
    def get_bairro(self):
        return self.__bairro
    def get_cep(self):
        return self.__cep
    def get_cidade(self):
        return self.__cidade
    def get_estado(self):
        return self.__estado

    # SETS
    def set_rua(self, nova_rua):
        self.__rua = nova_rua
    def set_numero(self, novo_numero):
        self.__numero = novo_numero
    def set_bairro(self, novo_bairro):
        self.__bairro = novo_bairro
    def set_cep(self, novo_cep):
        self.__cep = novo_cep
    def set_cidade(self, novo_cidade):
        self.__cidade = novo_cidade
    def set_estado(self, novo_estado):
        self.__estado = novo_estado

class Estoque:
    def __init__(self, produtos, id, nome, preco, data_validade, data_fabricacao, quantidade_estoque):
        self.__produtos = produtos

    def adicionarNovoProduto(self,produto):
        self.__produtos.append(produto)
    def reabastecerEstoque(self, produto, quantidade):
        for i in range(len(self.__produtos)):
            if(produto == self.__produtos[i]):
                self.__quantidade_estoque += quantidade
        

class Funcionario:

    def __init__(self, id, nome, cpf, endereco, sexo, contrato):
        self.__id = id
        self.__nome = nome
        self.__cpf = cpf
        self.__endereco = endereco
        self.__sexo = sexo
        self.__contrato = contrat
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

    def __init__(self, id, nome, cpf, endereco, sexo, contrato, forma_pagamento):
        Funcionario.__init__(id, nome, cpf, endereco, sexo, contrato)
        self.__forma_pagamento = forma_pagamento

    def set_forma_pagamento(self, forma_pagamento):
        self.__forma_pagamento = forma_pagamento
        
    def get_forma_pagamento(self):
        return self.__forma_pagamento

    def registrarCompra(compra, conta):
        pass

class Entregador:
    def __init__(self, destino):
        self.__destino = destino

    def iniciar_entrega(self, valor_total_compra, conta):
        if (valor_total_compra >= 100):
            print("Como o valor da compra foi acima de R$ 100,00, você foi isento da taxa para entrega.")
        else:
            conta.set_
    
    def status(self, local):
        return local
