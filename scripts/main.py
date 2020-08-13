from tkinter import *


janela = Tk()


#DEFININDO A COORDENADA DO ELEMENTO
lb = Label(janela, text="Hello World")
lb.place(x=10, y=20)

#DEFININDO O TAMANHO DA JANELA 
janela.geometry("300x300+200+200")
janela.mainloop()