"""
articulo
cliente
venta
venta_det
"""
class Articulo:
    def __init__(self, cod, des, pre, sto):
        self.codigo = code
        self.descripcon = des
        self.precio = pre
        self.stock = sto

class Cliente:
    def __init__(self, cedu, nom, direc, tel):
        self.cedula = cedu
        self.nombre = nom
        self.direccion = direc
        self.telefono = tel

class Venta:
    def __init__(self, fac, fech, cliente, tot):#detalle
        self.factura = fac
        self.fecha = fech
        self.cliente = cliente
        self.total = tot
        #self.detalle = detalle[] en caso de que sea una lista
#detalle contiene venta_det
class Venta_Det:
    def __init__(self, venta, producto, precio, cantidad):
        self.venta = venta
        self.producto = producto
        self.precio = pre
        self.cantidad = cantidad
        