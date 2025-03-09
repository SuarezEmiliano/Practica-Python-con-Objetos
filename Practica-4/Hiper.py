from Sucursal import Sucursal


class Hiper(Sucursal):
    def __init__(self, numero, superficie, facturacion, importe_ganado_alquiler):
        super().__init__(numero, superficie, facturacion)
        self.importe_ganado_alquiler = importe_ganado_alquiler

    def __str__(self):
        mant_str = super().__str__()
        str = f"<< HIPER >> {mant_str} -> IMPORTE GANADO POR ALQUILER: {self.importe_ganado_alquiler} >>"
        return str

    def get_resultado_comercial(self):
        return self.facturacion + self.importe_ganado_alquiler


    def get_indice_rentabilidad(self):
        return self.get_resultado_comercial() / self.superficie

    def get_tipo(self):
        return "Hiper"

    def es_rentable(self):
        if self.get_indice_rentabilidad() > 50:
            return True