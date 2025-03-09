from Sucursal import Sucursal


class Super(Sucursal):
    def __init__(self, numero, superficie, facturacion, es_mayorista):
        super().__init__(numero, superficie, facturacion)
        self.es_mayorista = es_mayorista

    def __str__(self):
        mant_str = super().__str__()
        str = f"<< SUPER >> {mant_str} -> Es mayorista: {self.es_mayorista} >>"
        return str

    def get_resultado_comercial(self):
        return self.facturacion


    def get_indice_rentabilidad(self):
        return self.get_resultado_comercial() / self.superficie

    def get_tipo(self):
        return "Super"

    def es_rentable(self):
        if self.es_mayorista == 1.0:
            if self.get_indice_rentabilidad() > 45:
                return True
            if self.es_mayorista == 0.0:
                if self.get_indice_rentabilidad() > 40:
                    return True
