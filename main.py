from datetime import datetime
from mimetypes import init

from classes.Persons.Cliente import Cliente
from classes.Finances.Compra import Compra
from classes.Finances.Conta import Conta
from classes.Utilities.Contrato import Contrato
from classes.Utilities.Endereco import Endereco
from classes.Produtcs.Estoque import Estoque
from classes.Persons.Funcionarios import Atendente, Entregador
from classes.Produtcs.Item import Item
from classes.Produtcs.Produto import Produto


# mande pix pfv

endereco1 = Endereco("Rua das flores", "16","Bairro das larangeiras", "07787-003", "Sousa", "PB")
endereco2 = Endereco("Rua Fagundes Lopes", "sem numero","Bairro das larangeiras", "07787-003", "Sousa", "PB")
cliente = Cliente(218376, "Josefina", "12/02/1970", endereco1)
conta = Conta(cliente, 120)

produto1 = Produto(1, 'arroz', 2.50, '15/09/2024', '12/09/2022', 50)
produto2 = Produto(2, "Leite 1L", 5, "16/09/2022", "16/07/2022", 20)
produto3 = Produto(3, "Toddynho", 2.49, "16/09/2022", "16/07/2022", 20)
produto4 = Produto(4, 'feijao', 8.79, '05/02/2023', '10/10/2022', 120)
produto5 = Produto(5, 'sal', 0.79, '05/02/2023', '05/02/2022', 45)
produto6 = Produto(6, 'Cuscuz', 2.65, '18/11/2021', '10/06/2022', 80)

item1 = Item(produto1, 10)
item2 = Item(produto2, 3)
item3 = Item(produto3, 4)
item4 = Item(produto4, 12)
item5 = Item(produto5, 7)
item6 = Item(produto6, 1)

print("----------------------------ESTOQUE TESTE----------------------------\n")
estoque = Estoque()
estoque.adicionarNovoProduto(produto1)
print(estoque)
estoque.adicionarNovoProduto(produto2)
estoque.adicionarNovoProduto(produto3)
estoque.adicionarNovoProduto(produto4)
estoque.adicionarNovoProduto(produto5)
estoque.adicionarNovoProduto(produto6)
print(estoque)

estoque.reabastecerEstoque(produto2,13)
print(estoque)

compra1=Compra(1, "add_na_conta")

contrato1=Contrato(1, '12/09/2021', '12/09/2022', 1200.00, '08/00', '17/00')
contrato2=Contrato(1, '12/09/2021', '12/09/2023', 1500.00, '08/00', '17/00')

atendente=Atendente(1, "Jose de Sousa", "123.456.789-01", endereco1, "M", contrato1)
entregador=Entregador(2, "Felippe Rian", "012-345-678-90", endereco2, "M", contrato2)

print("----------------------------COMPRA TESTE----------------------------\n")
compra1.adicionar_item_na_lista(item2)
compra1.adicionar_item_na_lista(item4)
compra1.adicionar_item_na_lista(item1)
print(compra1)
compra1.remover_item_da_lista(item1)
print(compra1)

print("----------------------------CONTA TESTE----------------------------\n")
print(conta)
atendente.registrarCompra(compra1, conta)
print(conta)

atendente.pagar_conta(conta, 20)
print(conta)
print("-----------------------------------------")

entregador.iniciar_entrega(cliente, compra1)
