from tkinter import *
from classes.Persons.Cliente import Cliente
from classes.Finances.Compra import Compra
from classes.Finances.Conta import Conta
from classes.Utilities.Contrato import Contrato
from classes.Utilities.Endereco import Endereco
from classes.Produtcs.Estoque import Estoque
from classes.Persons.Funcionarios import Atendente, Entregador
from classes.Produtcs.Item import Item
from classes.Produtcs.Produto import Produto


class Main:

    def __init__(self, window):
        self.janela = janela
        self.janela.title("Estoque")

        largura = 1280
        altura = 720

        largura_screen = self.janela.winfo_screenwidth()
        altura_screen = self.janela.winfo_screenheight()

        posx = largura_screen/2 - largura/2
        posy = altura_screen/2 - altura/2

        self.janela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
        self.janela.iconbitmap("assets/images/shopping-cart-icon.ico")

        self.container = Frame(self.janela)
        self.container.grid(row=1, column=0)

        self.button2 = Button(self.janela, text="adicionar um produto",
                         bg="orange", fg="white", pady="10px")
        self.button2.grid(column=0, row=1)

        self.label = Label(self.container, text="Nome", bg='lightgreen', width=1)
        self.label.grid(row=2, column=0, padx=15, pady=5)

        self.label = Label(self.container, text="Preço")
        self.label.grid(row=2, column=1, padx=15, pady=5)

        self.label = Label(self.container, text="Data de validade", bg='lightgreen',)
        self.label.grid(row=2, column=2, padx=15, pady=5)

        self.label = Label(self.container, text="Data de fabricação")
        self.label.grid(row=2, column=3, padx=15, pady=5)

        self.label = Label(self.container, text="Quantidade no estoque",
                      bg='lightgreen',)
        self.label.grid(row=2, column=4, padx=15, pady=5)
        

        self.updateStorage()

        buttonRemove = Button(
            self.janela, text="Remover um Produto", command=self.removerProduto, bg="orange", fg="white", pady="10px")
        buttonRemove.grid(row=20, column=0)
        buttonRestock = Button(
            self.janela, text="Reabastecer um Produto", bg="orange", fg="white", pady="10px")
        buttonRemove.grid(row=20, column=1)

        button2 = Button(self.janela, text="adicionar um produto",
                         command=self.adicionarNovoProduto, bg="orange", fg="white", pady="10px")
        button2.grid(column=0, row=1)

    def updateStorage(self):
        for x in range(len(estoque.get_produtos())):
            self.label = Label(self.container, text=estoque.get_produtos()[
                          x].get_nome(), bg='lightgreen', width=10)
            self.label.grid(row=x+3, column=0)

            self.label = Label(self.container, text=estoque.get_produtos()[
                          x].get_preco(), bg='white', width=10)
            self.label.grid(row=x+3, column=1)

            self.label = Label(self.container, text=estoque.get_produtos()[
                          x].get_data_validade(), bg='lightgreen', width=10)
            self.label.grid(row=x+3, column=2)

            self.label = Label(self.container, text=estoque.get_produtos()[
                          x].get_data_fabricacao(), bg='white', width=10)
            self.label.grid(row=x+3, column=3)

            self.label = Label(self.container, text=estoque.get_produtos()[
                          x].get_quantidade_estoque(), bg='lightgreen', width=10)
            self.label.grid(row=x+3, column=4)
            

    def removerProduto(self):
        self.view = Tk()
        self.view.title("Adicionar Produto")

        largura = 1280
        altura = 720

        largura_screen = self.view.winfo_screenwidth()
        altura_screen = self.view.winfo_screenheight()

        posx = largura_screen/2 - largura/2
        posy = altura_screen/2 - altura/2

        self.view.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
        self.view.iconbitmap("assets/images/shopping-cart-icon.ico")

        labelNome = Label(self.view, text="Nome do produto: ",
                               font=("sans-serif", 16))
        labelNome.grid(row=0, column=0)

        self.inputNome = Text(self.view, width=60, pady="8px",
                              padx="8px", height=1, font=("sans-serif", 16))
        self.inputNome.grid(row=0, column=1)

        labelId = Label(self.view, text="Id do produto: ",
                        font=("sans-serif", 16))
        labelId.grid(row=1, column=0)

        self.inputId = Text(self.view, width=60, pady="8px",
                       padx="8px", height=1, font=("sans-serif", 16))
        self.inputId.grid(row=1, column=1)

        labelPreco = Label(
            self.view, text="Preço do produto: ", font=("sans-serif", 16))
        labelPreco.grid(row=2, column=0)

        self.inputPreco = Text(self.view, width=60, pady="8px",
                          padx="8px", height=1, font=("sans-serif", 16))
        self.inputPreco.grid(row=2, column=1)

        labelDataFab = Label(
            self.view, text="Data de fabricação do produto: ", font=("sans-serif", 16))
        labelDataFab.grid(row=3, column=0)

        self.inputDataFab = Text(self.view, width=60, pady="8px",
                            padx="8px", height=1, font=("sans-serif", 16))
        self.inputDataFab.grid(row=3, column=1)

        labelDataVal = Label(
            self.view, text="Data de validade do produto: ", font=("sans-serif", 16))
        labelDataVal.grid(row=4, column=0)

        self.inputDataVal = Text(self.view, width=60, pady="8px",
                            padx="8px", height=1, font=("sans-serif", 16))
        self.inputDataVal.grid(row=4, column=1)
        self.self.labelQtdNoEstoque= Label(
            self.view, text="Quantidade no estoque: ", font=("sans-serif", 16))
        self.labelQtdNoEstoque.grid(row=5, column=0)
        self.inputQtdNoEstoque = Text(self.view, width=60, pady="8px",
                            padx="8px", height=1, font=("sans-serif", 16))
        self.inputQtdNoEstoque.grid(row=5, column=1)
        self.button1 = Button(self.view, text="Adicionar",
                         bg="orange", fg="white", pady="10px")
        self.button1.grid(column=10, row=7)
        

    

        self.view.mainloop()

    def createNewProduct(self):
        # print(self.inputId.get("1.0", END), self.inputNome.get("1.0", END), self.inputPreco.get("1.0", END), self.inputDataVal.get("1.0", END), self.inputDataFab.get("1.0", END))
        newProduct = Produto(self.inputId.get("1.0", END), self.inputNome.get("1.0", END), self.inputPreco.get("1.0", END), self.inputDataVal.get("1.0", END), self.inputDataFab.get("1.0", END))
        estoque.adicionarNovoProduto(newProduct)
        self.updateStorage()

    def adicionarNovoProduto(self):
        self.view = Tk()
        self.view.title("Adicionar Produto")

        largura = 1280
        altura = 720

        largura_screen = self.view.winfo_screenwidth()
        altura_screen = self.view.winfo_screenheight()

        posx = largura_screen/2 - largura/2
        posy = altura_screen/2 - altura/2

        self.view.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
        self.view.iconbitmap("assets/images/shopping-cart-icon.ico")

        labelNome = Label(self.view, text="Nome do produto: ",
                               font=("sans-serif", 16))
        labelNome.grid(row=0, column=0)

        self.inputNome = Text(self.view, width=60, pady="8px",
                              padx="8px", height=1, font=("sans-serif", 16))
        self.inputNome.grid(row=0, column=1)

        labelId = Label(self.view, text="Id do produto: ",
                        font=("sans-serif", 16))
        labelId.grid(row=1, column=0)

        self.inputId = Text(self.view, width=60, pady="8px",
                       padx="8px", height=1, font=("sans-serif", 16))
        self.inputId.grid(row=1, column=1)

        labelPreco = Label(
            self.view, text="Preço do produto: ", font=("sans-serif", 16))
        labelPreco.grid(row=2, column=0)

        self.inputPreco = Text(self.view, width=60, pady="8px",
                          padx="8px", height=1, font=("sans-serif", 16))
        self.inputPreco.grid(row=2, column=1)

        labelDataFab = Label(
            self.view, text="Data de fabricação do produto: ", font=("sans-serif", 16))
        labelDataFab.grid(row=3, column=0)

        self.inputDataFab = Text(self.view, width=60, pady="8px",
                            padx="8px", height=1, font=("sans-serif", 16))
        self.inputDataFab.grid(row=3, column=1)

        labelDataVal = Label(
            self.view, text="Data de validade do produto: ", font=("sans-serif", 16))
        labelDataVal.grid(row=4, column=0)

        self.inputDataVal = Text(self.view, width=60, pady="8px",
                            padx="8px", height=1, font=("sans-serif", 16))
        self.inputDataVal.grid(row=4, column=1)
        self.self.labelQtdNoEstoque= Label(
            self.view, text="Quantidade no estoque: ", font=("sans-serif", 16))
        self.labelQtdNoEstoque.grid(row=5, column=0)
        self.inputQtdNoEstoque = Text(self.view, width=60, pady="8px",
                            padx="8px", height=1, font=("sans-serif", 16))
        self.inputQtdNoEstoque.grid(row=5, column=1)
        # print(self.createNewProduct(inputId.get("1.0", END), inputNome.get("1.0", END), inputPreco.get(
        #     "1.0", END), inputDataVal.get("1.0", END), inputDataFab.get("1.0", END)))
        # print(inputId.get("1.0", END), inputNome.get("1.0", END), inputPreco.get("1.0", END), inputDataVal.get("1.0", END), inputDataFab.get("1.0", END))

        button1 = Button(self.view, text="Adicionar", command=self.createNewProduct, bg="orange", fg="white", pady="10px")
        button1.grid(column=11, row=8)

        self.view.mainloop()


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

estoque.reabastecerEstoque(produto2, 13)
print(estoque)


janela = Tk()
Main(janela)
janela.mainloop()
