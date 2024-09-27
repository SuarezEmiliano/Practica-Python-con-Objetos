
class Vehiculo:
    def __init__(self, matricula, marca, modelo, costo_base):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.costo_base = costo_base

    def __str__(self):
        return f"MATRICULA: {self.matricula}  MARCA: {self.marca}  MODELO: {self.modelo} COSTO BASE: {self.costo_base}"