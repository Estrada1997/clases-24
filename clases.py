class Operaciones:
    def __init__(self, num_1, nuum_2):
        self.numero_1 = num_1
        self.numero_2 = num_2
    
    def suma(self):
        suma = self.numero_1 + self.numero_2
        return suma

    def resta(self):
        #if self.numero_1 >= numero_2:
        #    resta = self.numero_1 - self.numero_2
        #return 0
        return  self.numero_1 - self.numero_2

    def multiplicacion(self):
        return  self.numero_1 * self.numero_2
        

    def division(self):
        if self.numero_2 != 0:
            return  self.numero_1 / self.numero_2
        return 0
    
    def divisionEntera(self):
        if self.numero_2 != 0: return  self.numero_1 // self.numero_2
        return 0

    def reciduo(self):
        return  self.numero_1 % self.numero_2

    def exponente(self):
        return  self.numero_1 ** self.numero_2

    def mostrar(self):
        print("Operando_1 = {}, Operando_2 {}".format(self.numero_1, self.numero_2))
#operacion = Operaciones()
#x = operacion.suma()
#print(operacion.suma())
# print(operacion.division())
#y = operacion.resta()
#z = x ** y
#print(z)
#operacion.mostrar()
print("Menu Operaciones Matematicas")
print("1) Suma/n 2)resta/n 3)Multiplicacion ")
ocp = "0"
while opc != "8":
    ocp = input("Elija opcion[1...8]: ")
    num_1 = int(input("Ingrese un numero 1: "))
    num_2 = int(input("Ingrese un numero 2: "))
    ope = Operaciones(num_1, num_2)
    if opc == "1":
        print("{} + {} = {}".format(ope.numero_1, ope.numero_2, ope.suma()))
    elif opc == "2":
        print("{} - {} = {}".format(ope.numero_1, ope.numero_2, ope.resta()))
    elif opc == "3":
        print("{} * {} = {}".format(ope.numero_1, ope.numero_2, ope.multplicacion()))


print("Gracias por su visita::!!!")