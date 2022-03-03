from ctypes import alignment
from tkinter import *


class Main:

    def __init__(self, window=None):
        janela.title("Periquita da Juliana Bonde")
        janela.geometry('1000x1000')
        self.container = Frame(window)
        self.container.pack()
        self.containerText = Label(
            self.container, text="Quem vai querer, a minha periquita")
        self.containerText.pack()
        self.containerButton = Button(
            self.container, text="Dar a periquita", background='red')
        self.containerButton.pack()


janela = Tk()
Main(janela)
janela.mainloop()
