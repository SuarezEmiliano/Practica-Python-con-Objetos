from Vehiculo import Vehiculo


class Camioneta(Vehiculo):
    def __init__(self, matricula, marca, modelo, costo_base, capacidad_carga):
        super().__init__(matricula, marca, modelo, costo_base)
        self.capacidad_carga = capacidad_carga

    def __str__(self):
        txt_super = super().__str__()
        txt = f" ==CAMIONETA== {txt_super} CAPACIDAD DE CARGA: {self.capacidad_carga}"
        return txt

    def get_costo(self):
        costo = self.costo_base
        if self.capacidad_carga > 1000:
            costo *= 1.15
        return costo