from Mantenimiento import Mantenimiento


class Preventivo(Mantenimiento):
    def __init__(self, nombreOperario, fecha, importeRespuestos, resultado, importeInsumos):
        super().__init__(nombreOperario, fecha, importeRespuestos)
        self.importeInsumos = importeInsumos
        self.resultado = resultado

    def __str__(self):
        mant_str = super().__str__()
        str = f"<< PREVENTIVO >> {mant_str} -> INSUMOS:{self.importeInsumos} - RESULTADO:{self.resultado}"
        return str

    def get_gastos(self):
        return self.importeInsumos + self.importeRespuestos

