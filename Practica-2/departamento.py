from inmueble import Inmueble


class Departamento(Inmueble):
    def __init__(self, codigo, nombre_propietario, superficie, importe_base, importe_expensas, numero_piso):
        super().__init__(codigo, nombre_propietario, superficie, importe_base)
        self.importe_expensas = importe_expensas
        self.numero_piso = numero_piso

    def __str__(self):
        txt_super = super().__str__()
        txt = f"==DEPARTAMENTO== {txt_super} EXPENSAS: {self.importe_expensas} N°PISO: {self.numero_piso}"
        return txt

    def get_importe_alquiler(self):
        importe_alquiler = self.importe_base + self.importe_expensas
        if self.numero_piso < 3:
            importe_alquiler += 20000
        return importe_alquiler



