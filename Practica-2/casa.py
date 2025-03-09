from inmueble import Inmueble


class Casa(Inmueble):
    def __init__(self, codigo, nombre_propietario, superficie, importe_base, cantidad_habitaciones, tiene_pileta):
        super().__init__(codigo, nombre_propietario, superficie, importe_base)
        self.cantidad_habitaciones = cantidad_habitaciones
        self.tiene_pileta = tiene_pileta

    def __str__(self):
        txt_super = super().__str__()
        txt = f"==CASA== {txt_super} HABITACIONES: {self.cantidad_habitaciones} PILETA: {self.tiene_pileta}"
        return txt

    def get_importe_alquiler(self):
        importe_alquiler = self.importe_base + (30000 * self.cantidad_habitaciones)
        if self.tiene_pileta == 1:
            importe_alquiler += 100000
        return importe_alquiler

    def es_casa_premium(self):
        if self.superficie > 150 and self.cantidad_habitaciones > 2 and self.tiene_pileta == 1:
            return True
        return False