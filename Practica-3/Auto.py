from Vehiculo import Vehiculo


class Auto(Vehiculo):
    def __init__(self, matricula, marca, modelo, costo_base, kilometraje):
        super().__init__(matricula, marca, modelo, costo_base)
        self.kilometraje = kilometraje

    def __str__(self):
        txt_super = super().__str__()
        txt = f" ==AUTO== {txt_super} KILOMETRAJE: {self.kilometraje} COSTO FINAL: {self.get_costo()}"
        return txt

    def get_costo(self):
        costo = self.costo_base
        if self.kilometraje > 100000:
            costo *= 1.1
        return costo