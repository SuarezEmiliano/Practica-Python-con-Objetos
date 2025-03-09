class Inmueble():
    def __init__(self, codigo, nombre_propietario, superficie, importe_base):
        self.codigo = codigo
        self.nombre_propietario = nombre_propietario
        self.superficie = superficie
        self.importe_base = importe_base

    def __str__(self):
        return f"CÓDIGO: {self.codigo} PROPIETARIO: {self.nombre_propietario} SUPERFICIE: {self.superficie} IMPORTE BASE: {self.importe_base}"