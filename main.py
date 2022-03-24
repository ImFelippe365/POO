"""Imports de todas as classes que usaremos"""

from colorama import Fore, Style
import os
import uuid
from threading import Timer
from classes.Persons.Cliente import Cliente
from classes.Finances.Compra import Compra
from classes.Finances.Conta import Conta
from classes.Utilities.Contrato import Contrato
from classes.Utilities.Endereco import Endereco
from classes.Produtcs.Estoque import Estoque
from classes.Persons.Funcionarios import Atendente, Entregador
from classes.Produtcs.Item import Item
from classes.Produtcs.Produto import Produto

"""Imports usados para gerar IDs aleatorios
manipular e customizar o terminal"""

'''instâncias para que não precise instanciar toda vez que rodar o código, para ser apresentado mais facilmente'''
produto2 = Produto(2, "Leite 1L", 5, "16/09/2022", "16/07/2022", 20)
produto3 = Produto(3, "Toddynho", 2.49, "16/09/2022", "16/07/2022", 20)
produto4 = Produto(4, 'feijao', 8.79, '05/02/2023', '10/10/2022', 120)
produto5 = Produto(5, 'sal', 0.79, '05/02/2023', '05/02/2022', 45)
produto6 = Produto(6, 'Cuscuz', 2.65, '18/11/2021', '10/06/2022', 80)


item2 = Item(produto2, 3)
item3 = Item(produto3, 4)
item4 = Item(produto4, 12)
item5 = Item(produto5, 7)
item6 = Item(produto6, 1)

estoque = Estoque()
'''métodos para que os produtos sejam adicionados no estoque, poupando tempo da apresentação'''
estoque.adicionarNovoProduto(produto2)
estoque.adicionarNovoProduto(produto3)
estoque.adicionarNovoProduto(produto4)
estoque.adicionarNovoProduto(produto5)
estoque.adicionarNovoProduto(produto6)

estoque.reabastecerEstoque(produto2, 13)

contrato1 = Contrato(1, '12/09/2021', '12/09/2022',
                     1200.00, '08/00', '17/00', "08:00")
contrato2 = Contrato(2, '12/09/2021', '12/09/2023',
                     1500.00, '08/00', '17/00', "08:00")
endereco1 = Endereco("Rua Maria das Flores", "129",
                     "Centro", "599000-000", "Mossoro", "RN")
endereco2 = Endereco("Rua Maria das Flores", "129",
                     "Centro", "599000-000", "Mossoro", "RN")
atendente = Atendente(1, "Jose de Sousa", "123.456.789-01",
                      endereco1, "M", contrato1)
entregador = Entregador(
    2, "Felippe Rian", "012-345-678-90", endereco2, "M", contrato2)

cliente = Cliente(uuid.uuid4(), "Breno", '08/02/2003', endereco1)
conta = Conta(cliente)

"""Metodo que usamos em diversas ações, ele 
basicamente lista os elementos de uma lista e
seleciona um deles"""


def escolher_opcao_listagem(lista=[]):
    for index in range(len(lista)):
        print(Fore.GREEN+f"{index+1}- {lista[index]}")

    escolha = int(input("\nEscolha a opção desejada: " +
                  Fore.RESET+Style.RESET_ALL))

    return lista[escolha-1]


"""Inicio do funcionamento do sistema, aqui é selecionado 
qual funcionario esta usando o sistema, pois cada um deles
pode realizar açoes diferentes"""
escolha = int(input(
    "Escolhas: \n1- Sou Atendente \n2- Sou Entregador \n3- Encerrar programa\n\nInforme a opção desejada: "))
os.system('cls' if os.name == 'nt' else 'clear')

"""Lista para armazenar as instancias de clientes e contas"""
lista_clientes = []
lista_contas = []

"""Algumas instancias sendo adicionadas nas listas, para acelerar o processo"""
lista_clientes.append(cliente)
lista_contas.append(conta)

if __name__ == "__main__":

    '''while criado para sempre ficar perguntando ao funcionario o que deseja fazer'''
    while True:

        if(escolha == 1):

            print(Fore.LIGHTCYAN_EX+30*"=")
            print("Bem vindo atendente!\nO que deseja fazer? \n\n1- Calcular Previdência Social \n2- Pagamento de débito \n3- Realizar compra \n4- Acessar estoque \n5- Acessar clientes \n6- Trocar usuário")
            print(Fore.RED+Style.BRIGHT+"\n0- Sair do sistema" +
                  Fore.RESET+Style.RESET_ALL)
            print(Fore.LIGHTCYAN_EX+30*"="+Fore.RESET)
            escolha_atendente = int(
                input(Fore.LIGHTCYAN_EX+"Escolha a opção desejada: "+Fore.RESET))

            os.system('cls' if os.name == 'nt' else 'clear')
            '''Escolha para apresentar o resultado do calculo da previdencia social do(a) atendente'''
            if(escolha_atendente == 1):
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\nCalculando previdência social")
                atendente.calculo_previdencia_social()

                '''Escolha para que o cliente possa pagar seu debito na conta'''
            elif(escolha_atendente == 2):
                os.system('cls' if os.name == 'nt' else 'clear')
                cliente = escolher_opcao_listagem(lista_clientes)
                conta = None
                for x in lista_contas:
                    if (cliente.get_id() == x.get_titular().get_id()):
                        conta = x
                if x.get_valor_a_pagar() == 0:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(Fore.RED+Style.BRIGHT +
                          "\n[!] O cliente em questão nao possui nenhuma divida!\n"+Fore.RESET+Style.RESET_ALL)
                else:
                    valor = float(
                        input(Fore.GREEN+"Quanto ele pretende pagar? "+Fore.RESET))
                    os.system('cls' if os.name == 'nt' else 'clear')
                    atendente.pagar_conta(conta, valor)
                    """Opção usada para realizar compras, onde escolhemos o cliente que vai fazer a compra"""
            elif(escolha_atendente == 3):
                os.system('cls' if os.name == 'nt' else 'clear')
                cliente = escolher_opcao_listagem(lista_clientes)
                conta = None

                for x in lista_contas:
                    if (cliente.get_id() == x.get_titular().get_id()):
                        conta = x

                lista_metodos = {
                    "Débito em conta": "add_na_conta",
                    "Espécie": "especie",
                    "PIX": 'pix',
                    "Cartão de crédito": 'cartao_de_credito',
                    "Cartão de débito": 'cartao_de_debito'
                }

                compra = Compra(uuid.uuid4(), "", conta)

                os.system('cls' if os.name == 'nt' else 'clear')
                print("\nSelecionando itens da compra...", end=" ")
                while True:

                    if len(estoque.get_produtos()) == 0:
                        print(Fore.RED+Style.BRIGHT+"\n[!] O estoque está vazio" +Fore.RESET+Style.RESET_ALL+"\nOpções disponíveis:\n")
                        escolha_compra = int(input(
                            "\n1- Adicionar item na lista\n3- Finalizar seleção de produtos\n\nSelecione a opção desejada: "))
                    else:
                        print(Fore.GREEN+f"{estoque}"+Fore.RESET)
                        escolha_compra = int(input(
                            Fore.LIGHTCYAN_EX+"Opções disponiveis:\n\n1- Adicionar item na lista\n2- Remover item da lista\n3- Finalizar seleção de produtos\n\nSelecione a opção desejada: "+Fore.RESET))

                    if escolha_compra == 1:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        produto = escolher_opcao_listagem(estoque.get_produtos())
                        quantidade = int(
                            input(Fore.GREEN+"Digite a quantidade do produto: "+Fore.RESET))
                        item = Item(produto, quantidade)
                        compra.adicionar_item_na_lista(item)

                    elif escolha_compra == 2:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        if len(compra.get_lista_itens()) == 0:
                            print(Fore.RED+Style.BRIGHT+"[!] Nenhum item foi adicionado a compra"+Fore.RESET+Style.RESET_ALL)
                        else:
                            item_a_ser_removido = escolher_opcao_listagem(
                                compra.get_lista_itens())
                            compra.remover_item_da_lista(item_a_ser_removido)
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Item removido da lista!")
                    elif escolha_compra == 3:
                        if len(compra.get_lista_itens()) == 0:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(Fore.RED+Style.BRIGHT+"[!] Nenhum item foi adicionado a compra, portanto, não é possível finalizar."+Fore.RESET+Style.RESET_ALL)
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            break
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Opção inválida")

                print(Fore.GREEN+"Forma de pagamento\n")
                metodo = escolher_opcao_listagem(list(lista_metodos.keys()))
                metodo_data = lista_metodos[metodo]
                compra.set_metodoPagamento(metodo_data)
                os.system('cls' if os.name == 'nt' else 'clear')
                atendente.registrarCompra(compra, conta)
                compra.set_metodoPagamento(metodo)
                atendente.comprovante_de_pagamento(compra)
                print()
                """Opção para que o atendente possa acessar o armazém e suas funções, ex.: adiconar produto no estoque, reabastecer, editar e remover. """
            elif(escolha_atendente == 4):
                while True:

                    produtos_estoque = estoque.get_produtos()
                    if (len(produtos_estoque) == 0):
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("\nEstoque vazio...\n")

                        opc = int(
                            input("\nO que deseja fazer? \n\n1 -Adicionar produto \n5- Sair...\n\nEscolha: "))
                        os.system('cls' if os.name == 'nt' else 'clear')
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("\n---------------Estoque---------------\n")
                        print(estoque)
                        opc = int(input(
                            "\nO que deseja fazer? \n\n1- Adicionar produto \n2- Remover produto \n3- Reabastecer Produto\n4- Alterar dados de um produto\n5- Sair...\n\nEscolha: "))
                        os.system('cls' if os.name == 'nt' else 'clear')

                    if(opc == 1):
                        print("Produto: ")
                        nome_produto = input("Digite o nome do produto: ")
                        preco_produto = float(
                            input("Digite o preço do produto: "))
                        data_validade_produto = input(
                            "Digite a data de validade do produto(dia/mes/ano): ")
                        data_fabricacao_produto = input(
                            "Digite a data de fabricação do produto(dia/mes/ano): ")
                        quantidade_produto = int(
                            input("Digite a quantidade: "))

                        produto = Produto(uuid.uuid4(), nome_produto, preco_produto,
                                          data_validade_produto, data_fabricacao_produto, quantidade_produto)
                        estoque.adicionarNovoProduto(produto)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Seu produto foi adicionado com sucesso!\n\n")

                        """Chamada de remoção dos produtos do estoque"""
                    elif(opc == 2):
                        print("\n---------------Estoque---------------\n")
                        at = escolher_opcao_listagem(estoque.get_produtos())
                        estoque.removerProduto(at)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(Fore.RED+"\nProduto removido com sucesso!"+Fore.RESET)

                        """Chamada de abastecimento dos produtos do estoque"""
                    elif(opc == 3):
                        print("\n---------------Estoque---------------\n")
                        at = escolher_opcao_listagem(estoque.get_produtos())
                        quantidade_produto = int(
                            input("Digite a quantidade: "))
                        estoque.reabastecerEstoque(at, quantidade_produto)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(Fore.GREEN+"Reabastecido com sucesso!"+Fore.RESET)

                        """Acesso ao estoque, aqui é realizada a alteração de dados dos produtos """
                    elif opc == 4:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Determine qual produto será alterado...\n")
                        print("\n---------------Estoque---------------\n")
                        at = escolher_opcao_listagem(estoque.get_produtos())
                        os.system('cls' if os.name == 'nt' else 'clear')

                        while True:
                            opc = int(input(
                                "\nQual atributo desse produto deverá ser alterado?\n\n1- Nome\n2- Preço\n3- Data de validade\n4- Data de fabricação\n5- Finalizar alterações...\n\nEscolha: "))

                            if opc == 1:
                                os.system('cls' if os.name ==
                                          'nt' else 'clear')
                                new_nome = input("Novo nome: ")
                                at.set_nome(new_nome)
                                os.system('cls' if os.name ==
                                          'nt' else 'clear')
                                print("Alteração realizada!")
                            elif opc == 2:
                                os.system('cls' if os.name ==
                                          'nt' else 'clear')
                                new_preco = float(input("Novo preço: "))
                                at.set_preco(new_preco)
                                os.system('cls' if os.name ==
                                          'nt' else 'clear')
                                print("Alteração realizada!")
                            elif opc == 3:
                                os.system('cls' if os.name ==
                                          'nt' else 'clear')
                                new_dataVal = input("Nova data de validade: ")
                                at.set_data_validade(new_dataVal)
                                os.system('cls' if os.name ==
                                          'nt' else 'clear')
                                print("Alteração realizada!")
                            elif opc == 4:
                                os.system('cls' if os.name ==
                                          'nt' else 'clear')
                                new_dataFab = input(
                                    "Nova data de fabricação: ")
                                at.set_data_fabricacao(new_dataFab)
                                os.system('cls' if os.name ==
                                          'nt' else 'clear')
                                print("Alteração realizada!")
                            elif opc == 5:
                                os.system('cls' if os.name ==
                                          'nt' else 'clear')
                                break
                            else:
                                os.system('cls' if os.name ==
                                          'nt' else 'clear')
                                print("\nOpção invalida...")
                    elif(opc == 5):
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break

                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Número inválido")
                '''Opção para acessar os clientes, com basicamente as mesmas funcionalidades de estoque, no caso são adicionar, remover e editar'''
            elif(escolha_atendente == 5):

                while True:
                    print(
                        "\n------------------Registro de clientes---------------------\n\n")
                    if len(lista_clientes) == 0:
                        print("Nenhum cliente cadastrado...\n")
                    else:
                        for i in range(len(lista_clientes)):
                            print(lista_clientes[i], "\n")

                    opc = int(input(
                        "\nO que deseja fazer?\n\n1- Cadastrar cliente\n2- Cancelar cadastro de um cliente\n3- Alterar dados de um cliente\n4- Sair...\n\nEscolha a opção desejada: "))

                    if opc == 1:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        nome_cliente = input("Digite o nome do cliente: ")
                        data_nascimento_cliente = input(
                            "Digite a data de nascimento do cliente(YYYY-MM-DD): ")
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f"Endereço do(a) {nome_cliente}: ")
                        rua_cliente = input(
                            f"Digite o nome da rua do(a) {nome_cliente}: ")
                        numero_cliente = input(
                            f"Digite o número da casa do(a) {nome_cliente}: ")
                        bairro_cliente = input(
                            f"Digite o nome do bairro do(a) {nome_cliente}: ")
                        cep_cliente = input(
                            f"Digite o número do CEP do(a) {nome_cliente}: ")
                        cidade_cliente = input(
                            f"Digite a cidade do(a) {nome_cliente}: ")
                        estado_cliente = input(
                            f"Digite o nome do estado do(a) {nome_cliente}: ")
                        endereco = Endereco(rua_cliente, numero_cliente, bairro_cliente,
                                            cep_cliente, cidade_cliente, estado_cliente)
                        cliente = Cliente(
                            uuid.uuid4(), nome_cliente, data_nascimento_cliente, endereco)
                        lista_clientes.append(nome_cliente)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("\nCliente cadastrado com sucesso!")
                        conta = Conta(cliente)
                        lista_contas.append(conta)
                        print("\nFoi criada tambem uma conta para ele!\n\n")

                    elif opc == 2:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("\nQual cliente será removido?\n")
                        x = escolher_opcao_listagem(lista_clientes)
                        lista_clientes.remove(x)
                        print("\nCliente removido com sucesso!")

                    elif opc == 3:
                        print("\nOs dados de qual cliente serão modificados?\n")
                        x = escolher_opcao_listagem(lista_clientes)
                        while True:
                            opc = int(input(
                                "\nQual dado vai ser alterado?\n\n1 - Alterar nome\n2 - Alterar data de nascimento\n3 - Alterar endereço\n4 - Finalizar alterações\n\nEscolha: "))

                            if opc == 1:
                                new_name = input(
                                    "\nInforme o nome que irá substituir: ")
                                x.set_nome(new_name)
                                os.system('cls' if os.name ==
                                          'nt' else 'clear')
                                print("\nAlteração realizada!")
                            elif opc == 2:
                                new_data = input(
                                    "\nInforme a data de nascimento que irá substituir (formato: dia/mes/ano): ")
                                x.set_data_nascimento(new_data)
                                os.system('cls' if os.name ==
                                          'nt' else 'clear')
                                print("\nAlteração realizada!")
                            elif opc == 3:
                                print("\nReinformando endereço...\n\n")
                                new_rua = input("\nInforme a rua: ")
                                new_numero = input("\nInforme o numero: ")
                                new_bairro = input("\nInforme o bairro: ")
                                new_CEP = input("\nInforme o CEP: ")
                                new_cidade = input("\nInforme a cidade: ")
                                new_estado = input("\nInforme o estado: ")

                                novoEndereco = Endereco(
                                    new_rua, new_numero, new_bairro, new_CEP, new_cidade, new_estado)
                                x.set_endereco(novoEndereco)
                                os.system('cls' if os.name ==
                                          'nt' else 'clear')
                                print("\nEndereço atualizado com sucesso!")

                            elif opc == 4:
                                os.system('cls' if os.name ==
                                          'nt' else 'clear')
                                break
                            else:
                                os.system('cls' if os.name ==
                                          'nt' else 'clear')
                                print("\nOpção invalida!")

                    elif opc == 4:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break

                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("\nOpção invalida!")
                '''Opção para que troque de usuário, ex.: de atendente vai para entregador'''
            elif(escolha_atendente == 6):
                escolha = 2
                '''Opção para sair do programa'''
            elif(escolha_atendente == 0):
                os.system('cls' if os.name == 'nt' else 'clear')
                print(Fore.RED+Style.BRIGHT+"[!] Desligando", end="")
                turnOff1 = Timer(1.0, lambda: print(".", end=""))
                turnOff2 = Timer(1.8, lambda: print(".", end=""))
                turnOff3 = Timer(2.3, lambda: print(
                    "."+Fore.RESET+Style.RESET_ALL, end=""))
                turnOff1.start()
                turnOff2.start()
                turnOff3.start()

                break

            """Sistema do entregador"""
        elif escolha == 2:

            """escolha de açoes do entregador"""
            print(Fore.LIGHTCYAN_EX+30*"=")
            print("Bem vindo Entregador!\nO que deseja fazer?\n\n1- Calcular Previdência Social \n2- Iniciar entrega\n3- Trocar usuario")
            print(Fore.RED+Style.BRIGHT+"\n0- Sair do sistema" +
                  Fore.RESET+Style.RESET_ALL)
            print(Fore.LIGHTCYAN_EX+30*"="+Fore.RESET)
            escolha_entregador = int(
                input(Fore.LIGHTCYAN_EX+"Escolha a opção desejada: "+Fore.RESET))

            """Chamada do metodo de calculo de Previdência Social do entregador"""
            if(escolha_entregador == 1):
                os.system('cls' if os.name == 'nt' else 'clear')
                entregador.calculo_previdencia_social()

                """Chamada do metodo de realizar compra do entregador"""
            elif(escolha_entregador == 2):
                os.system('cls' if os.name == 'nt' else 'clear')
                compras_realizadas = list(
                    atendente.get_compras_realizadas().values())

                if (len(compras_realizadas) > 0):
                    for x in range(len(compras_realizadas)):
                        print(Fore.GREEN+f"{x+1}- {compras_realizadas[x][0]}")

                        escolha = int(
                            input(Style.BRIGHT+"\nEscolha a opção desejada: "+Fore.RESET))
                        classe_compra = compras_realizadas[escolha-1][0]

                        entregador.iniciar_entrega(classe_compra)
                else:
                    print()

                """Alterar para o acesso de um atendente"""
            elif escolha_entregador == 3:
                escolha = 1

                """Finalização do codigo"""
            elif(escolha_entregador == 0):
                os.system('cls' if os.name == 'nt' else 'clear')
                print(Fore.RED+Style.BRIGHT+"[!] Desligando", end="")
                turnOff1 = Timer(1.0, lambda: print(".", end=""))
                turnOff2 = Timer(1.8, lambda: print(".", end=""))
                turnOff3 = Timer(2.3, lambda: print(
                    "."+Fore.RESET+Style.RESET_ALL, end=""))
                turnOff1.start()
                turnOff2.start()
                turnOff3.start()

                break
                """Chamada de opção errada do entregador"""
            else:
                print("Opção inválida...")

            """Chamada de opção errada"""
        else:
            print("Opção inválida...")
            break
