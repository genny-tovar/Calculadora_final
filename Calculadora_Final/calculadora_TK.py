from Tkinter import *
from calculadora import *
from threading import *

class InterfazCalculadora(Thread):

    def __init__(self):
        self.root = Tk()
        self.calculadora = Calculadora()
        self.frame = Frame(self.root)
        self.frame.pack()
        self.operador = ""

        foreground = "red"
        foreground2 = "blue"
        background = "blue"

        #Etiqueta display de calculadora
        self.inicio = StringVar()
        self.inicio.set ("0")
        self.display = Label(self.frame, textvariable = self.inicio, font=("arial", 30))
        self.display.grid(row=0, column=0, columnspan=4)


        self.boton_7 = Button(self.frame, text=" 7 ", font=("arial", 20),  height=1 , width=3 , command= lambda:self.manejar_numeros("7"))
        self.boton_7.grid(row=1, column=0)
        
        self.boton_8 = Button(self.frame, text=" 8 ", font=("arial", 20),  height=1 , width=3 , command= lambda:self.manejar_numeros("8"))
        self.boton_8.grid(row=1, column=1)

        self.boton_9 = Button(self.frame, text=" 9 ", font=("arial", 20),  height=1 , width=3 , command= lambda:self.manejar_numeros("9"))
        self.boton_9.grid(row=1, column=2)

        self.boton_por = Button(self.frame, text=" x ", font=("arial", 20),  height=1 , width=3 , foreground = foreground2, command= lambda:self.manejar_operadores("*"))
        self.boton_por.bind("<Button-1>")
        self.boton_por.grid(row=1, column=3)

        self.boton_4 = Button(self.frame, text=" 4 ", font=("arial", 20),  height=1 , width=3 , command= lambda:self.manejar_numeros("4"))
        self.boton_4.grid(row=2, column=0)

        self.boton_5 = Button(self.frame, text=" 5 ", font=("arial", 20),  height=1 , width=3 , command= lambda:self.manejar_numeros("5"))
        self.boton_5.grid(row=2, column=1)

        self.boton_6 = Button(self.frame, text=" 6 ", font=("arial", 20),  height=1 , width=3 , command= lambda:self.manejar_numeros("6"))
        self.boton_6.grid(row=2, column=2)

        self.boton_men = Button(self.frame, text=" - ", font=("arial", 20),  height=1 , width=3 , foreground = foreground2, command= lambda:self.manejar_operadores("-"))
        self.boton_men.bind("<Button-1>")
        self.boton_men.grid(row=2, column=3)

        self.boton_1 = Button(self.frame, text=" 1 ", font=("arial", 20),  height=1 , width=3 , command= lambda:self.manejar_numeros("1"))
        self.boton_1.grid(row=3, column=0)

        self.boton_2 = Button(self.frame, text=" 2 ", font=("arial", 20),  height=1 , width=3 , command= lambda:self.manejar_numeros("2"))
        self.boton_2.grid(row=3, column=1)

        self.boton_3 = Button(self.frame, text=" 3 ", font=("arial", 20),  height=1 , width=3 , command= lambda:self.manejar_numeros("3"))
        self.boton_3.grid(row=3, column=2)

        self.boton_mas = Button(self.frame, text=" + ", font=("arial", 20),  height=1 , width=3 , foreground = foreground2, command= lambda:self.manejar_operadores("+"))
        self.boton_mas.bind("<Button-1>")
        self.boton_mas.grid(row=3, column=3)

        self.boton_cero = Button(self.frame, text=" 0 ", font=("arial", 20),  height=1 , width=3 , command= lambda:self.manejar_numeros("0"))
        self.boton_cero.grid(row=4, column=1, )

        self.boton_uno = Button(self.frame, text=" CE ", font=("arial", 20), height=1 , width=3 , foreground = foreground, command= lambda:self.manejar_operadores("CE"))
        self.boton_uno.grid(row=4, column=0, )

        self.boton_igual = Button(self.frame, text=" = ", font=("arial", 20),  height=1 , width=3 , foreground = foreground2, command= lambda:self.manejar_operadores("="))
        self.boton_igual.bind("<Button-1>", )
        self.boton_igual.grid(row=4, column=3,)

        self.boton_dos = Button(self.frame, text=" / ", font=("arial", 20), height=1 , width=3 , foreground = foreground2, command= lambda:self.manejar_operadores("/"))
        self.boton_dos.bind("<Button-1>")
        self.boton_dos.grid(row=4, column=2, )
        
        self.root.geometry('250x300')
        self.root.mainloop()
        
    def manejar_numeros(self, valor):
        if self.inicio.get() == "0" :
            self.inicio.set(valor)
        else:
             self.inicio.set(self.inicio.get() + valor)

    def manejar_operadores(self, opera):
        if opera in "+-*/":
            self.calculadora.valor1 = int(self.inicio.get())
            self.inicio.set("0")
            self.operador = opera
        if opera == "=":
            self.calculadora.valor2 = int(self.inicio.get())
        
            
            if self.operador == "+":
                self.calculadora.suma()
                
            if self.operador == "-":
                self.calculadora.resta()
                
            if self.operador == "*":
                self.calculadora.multiplicacion()
                
            if self.operador == "/":
                self.calculadora.division()
                
            self.inicio.set(str(self.calculadora.mostrar_resultado()))

        if opera == "CE":
            
            self.inicio.set("0")
            self.calculadora.valor1 = "0"
            self.calculadora.valor2 = "0"
        
        
    
            

        
            
        

        
    


app = InterfazCalculadora()
