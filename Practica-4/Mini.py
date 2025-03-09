from Sucursal import Sucursal


class Mini(Sucursal):
    def __init__(self, numero, superficie, facturacion, importe_pagado_alquiler):
        super().__init__(numero, superficie, facturacion)
        self.importe_pagado_alquiler = importe_pagado_alquiler

    def __str__(self):
        mant_str = super().__str__()
        str = f"<< MINI >> {mant_str} -> IMPORTE PAGADO POR ALQUILER: {self.importe_pagado_alquiler}"
        return str

    def get_resultado_comercial(self):
        return self.facturacion - self.importe_pagado_alquiler


    def get_indice_rentabilidad(self):
        return self.get_resultado_comercial() / self.superficie

    def get_tipo(self):
        return "Mini"

    def es_rentable(self):
        if self.get_indice_rentabilidad() > 35:
            return True