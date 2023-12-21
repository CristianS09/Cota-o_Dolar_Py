from tkinter import *
import requests



def calcular():
    
    request = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    dolarCt = request.json()
    text1.config(text=f"O valor do dolar atual é:  {dolarCt['USDBRL']['bid']} R$")
    
def apagar():
    text1.config(text='')

janela = Tk()
janela.geometry("500x100")
janela.title("Cotação Dolar")

text = Label(janela,text="Cotação do Dolar")

text.pack()

butao = Button(janela,text="Calcular",command=calcular)
butao.pack()

butao2 = Button(janela,text='Apagar',command=apagar)
butao2.pack()

text1 = Label(janela,text='')
text1.pack()

text2 = Label(janela,text='')


janela.mainloop()