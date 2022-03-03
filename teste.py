from tkinter import *


class Main:

    def __init__(self, window):

        janela.title("Título da janela")
        janela.geometry('1000x500')

        self.container = Frame(window)
        self.container.pack()

        self.containerText = Label(self.container, text="Texto do container")
        self.containerText.pack()

        self.containerButton = Button(
            self.container, text="Clique aqui", background='green')
        self.containerButton.pack()


janela = Tk()
Main(janela)
janela.mainloop()
