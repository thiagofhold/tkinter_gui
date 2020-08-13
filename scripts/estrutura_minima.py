import tkinter as tk


janela = tk.Tk()
janela.title("Janela Principal")

#ALTERANDO O BACKGROUND
janela["background"] = "green"

#DEFINIÇÃO DO TAMANDO DA JANELA EM PIXELS
#larguraXaltura+distancia_do_lado_esquerdo+distancia_do_topo
janela.geometry("500x500+300+300")
 
janela.mainloop()