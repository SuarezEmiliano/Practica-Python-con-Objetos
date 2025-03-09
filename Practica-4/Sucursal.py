class Sucursal:
    def __init__(self, numero, superficie, facturacion):
        self.numero = numero
        self.superficie = superficie
        self.facturacion = facturacion

    def __str__(self):
        return f"SUCURSAL: {self.numero} - SUPERFICIE: {self.superficie} - FACTURACIÓN: {self.facturacion}"