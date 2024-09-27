from Vehiculo import Vehiculo


class Moto(Vehiculo):
    def __init__(self, matricula, marca, modelo, costo_base, cilindrica):
        super().__init__(matricula, marca, modelo, costo_base)
        self.cilindrica = cilindrica

    def __str__(self):
        txt_super = super().__str__()
        txt = f" ==MOTO== {txt_super} CILINDRICA: {self.cilindrica}"
        return txt

    def get_costo(self):
        costo = self.costo_base
        if self.cilindrica > 500:
            costo *= 1.20
        return costo