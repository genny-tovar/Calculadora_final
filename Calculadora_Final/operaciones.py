
class Calculadora:

    def __init__(self):

        self.valor1 = 0
        self.valor2 = 0
        self.resultado = 0

    def suma (self):
        self.resultado = (self.valor1 + self.valor2)

    def resta (self):

        self.resultado = (self.valor1 - self.valor2)

    def multiplicacion(self):

        self.resultado = (self.valor1 * self.valor2)

    def division(self):

        self.resultado = (self.valor1 / self.valor2)

    def mostrar_resultado(self):

        return str(self.resultado)

    

    
    
    
